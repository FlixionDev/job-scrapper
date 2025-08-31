# Job Scraper

A Python script that scrapes job listings from multiple platforms (Indeed, LinkedIn, Wellfound, Naukri) and sends daily email digests.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Email Configuration (Required to fix SMTP Authentication Error)

To resolve the SMTP authentication error, you need to set up Gmail App Passwords:

#### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings: https://myaccount.google.com/
2. Navigate to Security → 2-Step Verification
3. Enable 2-Factor Authentication if not already enabled

#### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select "Mail" from the dropdown
3. Select your device (or choose "Other" and name it "Job Scraper")
4. Click "Generate"
5. Copy the 16-character password (without spaces)

#### Step 3: Create .env File
Create a `.env` file in the project root with the following content:

```
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-16-character-app-password
RECEIVER_EMAIL=recipient-email@example.com
```

**Important Notes:**
- Use your regular Gmail address for `SENDER_EMAIL`
- Use the 16-character App Password (not your regular Gmail password) for `SENDER_PASSWORD`
- The App Password should not contain spaces
- Make sure to add `.env` to your `.gitignore` file to keep credentials secure

### 3. Run the Script
```bash
python job_scraper.py
```

## Features
- Scrapes job listings from Indeed, LinkedIn, Wellfound, and Naukri
- Sends formatted HTML email with job details
- Includes job title, company name, and direct links
- Daily digest format with current date

## Troubleshooting

### SMTP Authentication Error
If you see "Username and Password not accepted" error:
1. Make sure you're using an App Password, not your regular Gmail password
2. Verify that 2-Factor Authentication is enabled on your Google account
3. Check that the App Password is exactly 16 characters (no spaces)
4. Ensure your `.env` file is in the correct location and format

### Other Issues
- Make sure all required packages are installed: `pip install -r requirements.txt`
- Check that your internet connection is stable
- Verify that the job search query and location are valid

## 🚀 GitHub Actions Setup

To run this job scraper automatically on GitHub Actions (recommended for scheduled jobs):

1. **Follow the detailed setup guide**: [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)
2. **Key requirements**:
   - Generate a Gmail App Password (not regular password)
   - Set up GitHub Secrets with your email credentials
   - The workflow will run daily at 9:00 AM UTC

**Benefits of GitHub Actions:**
- ✅ Free tier with generous limits
- ✅ Scheduled execution (cron jobs)
- ✅ No need to keep your computer running
- ✅ Automatic email delivery
- ✅ Easy monitoring and debugging
