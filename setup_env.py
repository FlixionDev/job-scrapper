#!/usr/bin/env python3
"""
Helper script to set up the .env file for the job scraper.
This will guide you through the process of configuring your email settings.
"""

import os
import getpass

def create_env_file():
    """Create a .env file with user input."""
    
    print("🔧 Job Scraper Email Configuration Setup")
    print("=" * 50)
    print()
    
    print("To fix the SMTP authentication error, you need to:")
    print("1. Enable 2-Factor Authentication on your Google account")
    print("2. Generate an App Password")
    print("3. Configure your .env file")
    print()
    
    # Check if .env already exists
    if os.path.exists('.env'):
        overwrite = input("⚠️  .env file already exists. Overwrite? (y/N): ").lower()
        if overwrite != 'y':
            print("Setup cancelled.")
            return
    
    print("📧 Email Configuration")
    print("-" * 30)
    
    # Get email configuration
    sender_email = input("Enter your Gmail address: ").strip()
    if not sender_email.endswith('@gmail.com'):
        print("⚠️  Warning: This script is configured for Gmail. Other providers may require different settings.")
    
    print("\n🔐 App Password Setup")
    print("-" * 30)
    print("You need to generate an App Password:")
    print("1. Go to: https://myaccount.google.com/apppasswords")
    print("2. Select 'Mail' and your device")
    print("3. Copy the 16-character password (without spaces)")
    print()
    
    sender_password = getpass.getpass("Enter your 16-character App Password: ").strip()
    
    if len(sender_password) != 16:
        print("⚠️  Warning: App Password should be exactly 16 characters. Please double-check.")
    
    receiver_email = input("Enter recipient email address: ").strip()
    
    # Create .env content
    env_content = f"""# Email Configuration for Job Scraper
SENDER_EMAIL={sender_email}
SENDER_PASSWORD={sender_password}
RECEIVER_EMAIL={receiver_email}
"""
    
    # Write to .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("\n✅ .env file created successfully!")
        print("\n📋 Next Steps:")
        print("1. Test your configuration by running: python job_scraper.py")
        print("2. If you still get authentication errors, verify your App Password")
        print("3. Make sure 2-Factor Authentication is enabled on your Google account")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

if __name__ == "__main__":
    create_env_file() 
