import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

message = "Subject: Test Email\n\nThis is a test email!"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_email, message)

print("Email sent!")

# Test output to ensure proper connection to env variables
# print(sender_email)
# print(app_password)
# print(recipient_email)
