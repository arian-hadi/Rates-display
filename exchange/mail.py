from email.mime.text import MIMEText
import smtplib
from config import EMAIL_RECEIVER
from localsettings import GMAIL_APIKEY 
import ssl

def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "hadiarian19@gmail.com"
    msg['To'] = EMAIL_RECEIVER
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as mail_server:
        mail_server.login(msg['From'], GMAIL_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()
