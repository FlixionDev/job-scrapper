# GitHub Actions Setup Guide

This guide will help you set up the job scraper to run automatically on GitHub Actions.

## 🚀 Quick Setup

### 1. Generate Gmail App Password

**IMPORTANT**: You need an App Password, not your regular Gmail password!

1. **Enable 2-Factor Authentication** (if not already enabled):
   - Go to: https://myaccount.google.com/
   - Security → 2-Step Verification → Enable

2. **Generate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" from the dropdown
   - Select "Other" and name it "GitHub Actions Job Scraper"
   - Click "Generate"
   - **Copy the 16-character password** (e.g., `abcd efgh ijkl mnop`)

### 2. Set Up GitHub Secrets

1. Go to your GitHub repository
2. Click on **Settings** tab
3. Click on **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add these three secrets:

| Secret Name | Value |
|-------------|-------|
| `SENDER_EMAIL` | `your-gmail@gmail.com` |
| `SENDER_PASSWORD` | `your-16-char-app-password` (no spaces) |
| `RECEIVER_EMAIL` | `recipient-email@example.com` |

**Example:**
- `SENDER_EMAIL`: `tvlogin22558800@gmail.com`
- `SENDER_PASSWORD`: `abcd efgh ijkl mnop` (remove spaces)
- `RECEIVER_EMAIL`: `adityasingh200141@gmail.com`

### 3. Test the Workflow

1. Go to **Actions** tab in your repository
2. Click on **Daily Job Scraper** workflow
3. Click **Run workflow** → **Run workflow**

## 🔧 Troubleshooting

### SMTP Authentication Error

If you still get authentication errors:

1. **Verify App Password**:
   - Make sure you're using the 16-character App Password
   - Remove any spaces from the password
   - Don't use your regular Gmail password

2. **Check 2-Factor Authentication**:
   - Ensure 2FA is enabled on your Google account
   - App Passwords only work with 2FA enabled

3. **Verify GitHub Secrets**:
   - Go to Settings → Secrets and variables → Actions
   - Check that all three secrets are set correctly
   - Make sure there are no extra spaces or characters

4. **Test Locally First**:
   ```bash
   # Test with environment variables
   SENDER_EMAIL=your-email@gmail.com SENDER_PASSWORD=your-app-password RECEIVER_EMAIL=recipient@example.com python job_scraper.py
   ```

### Common Issues

1. **"Less secure app access"**: This doesn't work anymore. You must use App Passwords.

2. **"Username and Password not accepted"**: 
   - You're using regular password instead of App Password
   - 2FA is not enabled
   - App Password has spaces or extra characters

3. **Workflow not running**: 
   - Check if the cron schedule is correct
   - GitHub Actions may have delays for scheduled workflows

## 📅 Schedule Configuration

The workflow is set to run daily at 9:00 AM UTC. To change the schedule:

Edit `.github/workflows/job-scraper.yml` and modify the cron expression:

```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # Daily at 9:00 AM UTC
```

**Common cron patterns:**
- `'0 9 * * *'` - Daily at 9:00 AM UTC
- `'0 18 * * *'` - Daily at 6:00 PM UTC  
- `'0 9 * * 1-5'` - Weekdays only at 9:00 AM UTC
- `'0 */6 * * *'` - Every 6 hours

## 🔍 Debugging

To debug issues:

1. **Check workflow logs**:
   - Go to Actions tab
   - Click on the failed workflow run
   - Check the "Run job scraper" step logs

2. **Test manually**:
   - Use the "Run workflow" button to trigger manually
   - This helps isolate if it's a scheduling issue

3. **Verify environment variables**:
   - The workflow uses `${{ secrets.VARIABLE_NAME }}`
   - Make sure secret names match exactly

## ✅ Success Indicators

When everything is working correctly, you should see:
- ✅ Workflow runs successfully in GitHub Actions
- 📧 Email received with job listings
- No SMTP authentication errors in logs 
