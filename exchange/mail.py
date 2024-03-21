from email.mime.text import MIMEText
import smtplib
# from config import EMAIL_RECEIVER
from localsettings import MAILTRAP_APIKEY

def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "from@example.com"
    msg['To'] = "to@example.com"

    with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as mail_server:
        mail_server.login('cc99a85da372c1', MAILTRAP_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()
