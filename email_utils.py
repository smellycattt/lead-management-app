from email.message import EmailMessage
import aiosmtplib

async def send_email(subject: str, body: str, to: str):
    message = EmailMessage()
    message["From"] = "no-reply@alma.com"
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(message, hostname="sandbox.smtp.mailtrap.io", port=587, username="6a41084c156f09", password="bed0aa7afd71c4")
