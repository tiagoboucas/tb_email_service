import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send_email(to_email, subject, content, content_type="plain"):
    """
    Send an email with either plain text or HTML content.

    :param to_email: Recipient's email address
    :param subject: Email subject
    :param content: Email content (plain text or HTML)
    :param content_type: Content type ("plain" or "html")
    :return: True if the email was sent successfully, False otherwise
    """
    msg = MIMEMultipart()
    msg['From'] = Config.MAIL_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the content as plain text or HTML
    if content_type == "html":
        msg.attach(MIMEText(content, 'html'))
    else:
        msg.attach(MIMEText(content, 'plain'))

    try:
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        if Config.MAIL_USE_TLS:
            server.starttls()
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        server.sendmail(Config.MAIL_USERNAME, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
