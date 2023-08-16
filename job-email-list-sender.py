#!/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sample employer data (replace with your actual data)
employer_list = [
    {
        "employer_name": "Company A",
        "employer_email": "employer_a@example.com",
        "job_title": "Food Counter Attendant",
        "cover_letter": "Dear [Employer's Name],\n\n[Customized content based on description].\n\nSincerely,\n[Your Name]"
    },
    # Add more employers and their data
]

your_name = "Your Name"
your_email = "your_email@example.com"

def send_email(subject, body, to_email):
    from_email = your_email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # Update with your SMTP server details
    server.starttls()
    server.login(from_email, 'your_password')  # Provide your email password or use a secure method
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

for employer in employer_list:
    custom_cover_letter = employer["cover_letter"].replace("[Employer's Name]", employer["employer_name"])
    # Add logic to customize cover_letter based on enterprise descriptions

    subject = f"Application for {employer['job_title']} Position"
    send_email(subject, custom_cover_letter, employer["employer_email"])
    print(f"Email sent to {employer['employer_name']} at {employer['employer_email']}")
