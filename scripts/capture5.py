"""Re-capture screenshot #5 — approval scanner — with viewport-only screenshot."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

URL = "https://gyoomei.github.io/mimoaudit/"
OUT = Path("/root/mimoaudit/screenshots")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900},
                                         device_scale_factor=2)
        page = await ctx.new_page()
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_timeout(1500)
        await page.evaluate("switchTab('approvals')")
        await page.wait_for_timeout(500)
        await page.fill("#walletInput", "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        await page.select_option("#approvalChain", "eth")
        await page.click('button[onclick="scanApprovals()"]')
        try:
            await page.wait_for_function(
                "document.getElementById('approvalsResult').innerHTML.length > 200",
                timeout=30000,
            )
        except Exception:
            pass
        await page.wait_for_timeout(2500)
        # Scroll the result into view
        await page.evaluate("document.getElementById('approvalsResult').scrollIntoView({block:'start'})")
        await page.wait_for_timeout(800)
        # viewport-only screenshot to avoid the captureScreenshot size limit
        await page.screenshot(path=str(OUT / "05_approval_scanner.png"), full_page=False)
        await browser.close()
    f = OUT / "05_approval_scanner.png"
    print(f"Saved {f.name}: {f.stat().st_size//1024} KB")

asyncio.run(main())
