# Instantly.ai Campaign Automation Script

**Automates campaign setup for Voxable lead generation.**

## What It Does

✅ Logs into Instantly.ai  
✅ Creates new campaign  
✅ Uploads your CSV leads  
✅ Guides you through adding email sequences  
✅ Configures campaign settings  
✅ Launches the campaign  

## Prerequisites

1. **Python 3.7+** (already installed on this system)
2. **Playwright** (script will auto-install if missing)

## How to Run

### Step 1: Make sure you have your credentials ready
- Instantly.ai email
- Instantly.ai password

### Step 2: Run the script

```bash
cd /root/clawd/automation
python3 instantly-campaign-setup.py
```

### Step 3: Follow the prompts

The script will:
1. Ask for your email and password
2. Ask for CSV path (default: your exported leads file)
3. Open a browser window
4. Automate the login and campaign creation
5. Pause for you to manually add email sequences (copy/paste from terminal)
6. Confirm launch

## Expected Runtime

**Total time:** ~5-10 minutes (mostly automated)

**Manual steps:**
- Enter credentials (30 seconds)
- Add 3 email sequences (3 minutes)
- Verify settings (1 minute)
- Confirm launch (5 seconds)

## Troubleshooting

### "Playwright not installed"
The script will auto-install it. Just run the script again after installation completes.

### "Login failed or took too long"
- **CAPTCHA:** If Instantly shows a CAPTCHA, solve it manually in the browser
- **2FA:** If you have 2-factor auth, complete it manually when prompted
- Script will wait for you to complete manual steps

### "Could not find button"
Instantly.ai's UI may have changed. The script will pause and show you what to do manually.

### Browser closes immediately
Check for errors in the terminal. The script keeps the browser open until you press Enter.

## What Gets Automated

| Step | Automation Level |
|------|-----------------|
| Login | ✅ Fully automated |
| Create campaign | ✅ Fully automated |
| Upload CSV | ✅ Fully automated |
| Add sequences | ⚠️ Semi-automated (copy/paste) |
| Configure settings | ⚠️ Manual verification |
| Launch | ✅ Automated (with confirmation) |

## Files Used

- **Script:** `/root/clawd/automation/instantly-campaign-setup.py`
- **Leads CSV:** `/root/clawd/projects/voxable-cold-outreach/voxable-leads-instantly-export.csv`
- **Email sequences:** Built into script (will be displayed)

## Security Notes

🔐 Your password is **not** saved anywhere  
🔐 Script runs locally on your machine  
🔐 Browser runs in visible mode (you can see what it's doing)  

## Advanced Options

### Run in headless mode (no visible browser)
Edit the script and change:
```python
headless=False  # Change to True
```

### Use different CSV
When prompted, enter the full path to your CSV file.

### Customize sequences
Edit the `sequences` array in the script (lines ~155-210).

## Support

If the script fails:
1. Check the error message in terminal
2. Try running manually (follow MANUAL-LAUNCH-GUIDE.md)
3. Ping Portifoy with the error details

---

**Ready to launch?** Run the script! 🚀
