import smtplib
from email.message import EmailMessage
from app.config.settings import get_settings

def send_email(subject: str, body: str, to_email: str):
    settings = get_settings()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.email_sender
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(settings.smtp_server, settings.smtp_port) as smtp:
        smtp.login(settings.smtp_username, settings.smtp_password)
        smtp.send_message(msg)
