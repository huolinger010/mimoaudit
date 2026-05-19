"""Capture 5 high-impact screenshots of MimoAudit for MiMo 100T submission."""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

URL = "https://gyoomei.github.io/mimoaudit/"
OUT = Path("/root/mimoaudit/screenshots")
OUT.mkdir(parents=True, exist_ok=True)

VULNERABLE_SAMPLE = """pragma solidity ^0.8.0;

contract VulnerableBank {
    mapping(address => uint) public balances;
    address public owner;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // VULN: reentrancy — external call before state update
    function withdraw() public {
        uint amount = balances[msg.sender];
        require(amount > 0);
        (bool ok,) = msg.sender.call{value: amount}("");
        require(ok);
        balances[msg.sender] = 0;
    }

    // VULN: tx.origin auth
    function setOwner(address _o) public {
        require(tx.origin == owner);
        owner = _o;
    }

    // VULN: weak randomness
    function random() public view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.timestamp, msg.sender)));
    }
}
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1440, "height": 900},
                                         device_scale_factor=2)
        page = await ctx.new_page()

        # ===== 1. HOMEPAGE / HERO =====
        print("[1/5] Capturing homepage...")
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_timeout(1500)
        await page.screenshot(path=str(OUT / "01_homepage.png"), full_page=False)

        # ===== 2. AUDIT RESULT (run analyzer on a vulnerable contract) =====
        print("[2/5] Running audit on vulnerable contract...")
        await page.fill("#input", VULNERABLE_SAMPLE)
        await page.click("#btnAnalyze")
        # Wait for result section to appear
        try:
            await page.wait_for_selector("#result:not(.hide)", timeout=15000)
        except Exception:
            pass
        await page.wait_for_timeout(2500)
        await page.screenshot(path=str(OUT / "02_audit_findings.png"), full_page=True)

        # ===== 3. FAMOUS HACKS GALLERY =====
        print("[3/5] Opening Famous Hacks gallery...")
        # Go back to top
        await page.evaluate("window.scrollTo(0,0)")
        await page.wait_for_timeout(500)
        await page.click("button.hacks-btn")
        await page.wait_for_selector("#hacksModal.show", timeout=5000)
        await page.wait_for_timeout(800)
        await page.screenshot(path=str(OUT / "03_famous_hacks.png"), full_page=False)
        # Close
        await page.click("#hacksModal .chat-close")
        await page.wait_for_timeout(400)

        # ===== 4. MIMO AI CHAT =====
        print("[4/5] Opening MiMo Chat assistant...")
        await page.click("#chatFab")
        await page.wait_for_selector("#chatPanel.show", timeout=5000)
        await page.wait_for_timeout(500)
        # Send a question — use offline fallback so it's deterministic
        await page.fill("#chatInput", "What is reentrancy and how to prevent it?")
        await page.click("#chatSendBtn")
        # Wait for fallback or live response
        try:
            await page.wait_for_function(
                "document.querySelectorAll('#chatBody .chat-msg.bot').length >= 2",
                timeout=15000,
            )
        except Exception:
            pass
        await page.wait_for_timeout(1500)
        await page.screenshot(path=str(OUT / "04_mimo_chat.png"), full_page=False)
        # Close chat
        await page.click("#chatPanel .chat-close")
        await page.wait_for_timeout(400)

        # ===== 5. APPROVAL SCANNER (vitalik.eth on Ethereum) =====
        print("[5/5] Running approval scanner...")
        await page.evaluate("switchTab('approvals')")
        await page.wait_for_timeout(500)
        await page.fill("#walletInput", "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        await page.select_option("#approvalChain", "eth")
        await page.click('button[onclick="scanApprovals()"]')
        try:
            await page.wait_for_function(
                "document.getElementById('approvalsResult').innerHTML.length > 100",
                timeout=25000,
            )
        except Exception:
            pass
        await page.wait_for_timeout(2000)
        await page.screenshot(path=str(OUT / "05_approval_scanner.png"), full_page=True)

        await browser.close()
    # Print sizes
    for f in sorted(OUT.glob("*.png")):
        print(f"  {f.name}: {f.stat().st_size//1024} KB")

asyncio.run(main())
