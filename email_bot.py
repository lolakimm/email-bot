import smtplib

sender_email = ""
app_password = ""

recipient_email = ""

message = ""

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.startls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_email, message)

print("Email sent!")