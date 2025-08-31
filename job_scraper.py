import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Email Config from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # This should be an App Password, not your regular password
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

print(f"SENDER_EMAIL: {SENDER_EMAIL}")
print(f"SENDER_PASSWORD: {SENDER_PASSWORD}")
print(f"RECEIVER_EMAIL: {RECEIVER_EMAIL}")

# Job Search Config
QUERY = "Frontend Developer React Vue"
LOCATION = "India"

def fetch_indeed():
    url = f"https://in.indeed.com/jobs?q={QUERY.replace(' ', '+')}&l={LOCATION}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for job_card in soup.find_all("div", class_="job_seen_beacon")[:5]:
        title = job_card.find("h2").text.strip() if job_card.find("h2") else "No Title"
        company = job_card.find("span", class_="companyName").text.strip() if job_card.find("span", class_="companyName") else "Unknown"
        link = "https://in.indeed.com" + job_card.find("a")["href"]
        jobs.append(("Indeed", title, company, link))
    return jobs

def fetch_linkedin():
    url = f"https://www.linkedin.com/jobs/search?keywords={QUERY.replace(' ', '%20')}&location={LOCATION}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for job_card in soup.find_all("div", class_="base-card")[:5]:
        title = job_card.find("h3").text.strip() if job_card.find("h3") else "No Title"
        company = job_card.find("h4").text.strip() if job_card.find("h4") else "Unknown"
        link = job_card.find("a")["href"]
        jobs.append(("LinkedIn", title, company, link))
    return jobs

def fetch_wellfound():
    url = f"https://wellfound.com/jobs?keywords={QUERY.replace(' ', '%20')}&location={LOCATION}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for job_card in soup.find_all("div", class_="styles_component__d6dnR")[:5]:
        title = job_card.find("a").text.strip() if job_card.find("a") else "No Title"
        company = job_card.find("div", class_="styles_subline__gUciY").text.strip() if job_card.find("div", class_="styles_subline__gUciY") else "Unknown"
        link = "https://wellfound.com" + job_card.find("a")["href"]
        jobs.append(("Wellfound", title, company, link))
    return jobs

def fetch_naukri():
    url = f"https://www.naukri.com/frontend-developer-react-vue-jobs-in-{LOCATION.lower()}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for job_card in soup.find_all("article", class_="jobTuple")[:5]:
        title = job_card.find("a").text.strip() if job_card.find("a") else "No Title"
        company = job_card.find("div", class_="companyInfo").text.strip() if job_card.find("div", class_="companyInfo") else "Unknown"
        link = job_card.find("a")["href"]
        jobs.append(("Naukri", title, company, link))
    return jobs

def send_email(jobs):
    today = datetime.date.today().strftime("%d %b %Y")
    subject = f"Daily Job Digest - Frontend Developer Roles ({today})"
    
    if jobs:
        rows = ""
        for source, title, company, link in jobs:
            rows += f"""
                <tr>
                    <td>{source}</td>
                    <td><a href="{link}" target="_blank">{title}</a></td>
                    <td>{company}</td>
                </tr>
            """
        body = f"""
        <html>
        <body>
            <h2>Daily Job Digest - {today}</h2>
            <table border="1" cellspacing="0" cellpadding="8" style="border-collapse: collapse; font-family: Arial, sans-serif; font-size: 14px;">
                <tr style="background-color: #f2f2f2;">
                    <th>Source</th>
                    <th>Job Title</th>
                    <th>Company</th>
                </tr>
                {rows}
            </table>
        </body>
        </html>
        """
    else:
        body = f"<p>No jobs found for {today}.</p>"

    msg = MIMEMultipart("alternative")
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("✅ HTML Job digest sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("❌ SMTP Authentication Error!")
        print("\nTo fix this issue, follow these steps:")
        print("1. Enable 2-Factor Authentication on your Google account")
        print("2. Generate an App Password:")
        print("   - Go to https://myaccount.google.com/apppasswords")
        print("   - Select 'Mail' and your device")
        print("   - Copy the 16-character password")
        print("3. Update your .env file with the App Password")
        print("4. Make sure your .env file contains:")
        print("   SENDER_EMAIL=your-email@gmail.com")
        print("   SENDER_PASSWORD=your-16-char-app-password")
        print("   RECEIVER_EMAIL=recipient-email@example.com")
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")

if __name__ == "__main__":
    all_jobs = []
    all_jobs.extend(fetch_indeed())
    all_jobs.extend(fetch_linkedin())
    all_jobs.extend(fetch_wellfound())
    all_jobs.extend(fetch_naukri())
    
    send_email(all_jobs)
    print("✅ HTML Job digest sent!")
