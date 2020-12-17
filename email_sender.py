import smtplib
from email.message import EmailMessage
from config import gmail_password

def send_email(email_bits):
    email = EmailMessage()
    email['from'] = email_bits['from']
    email['to'] = email_bits['to']
    email['subject'] = email_bits['subject']

    email.set_content(email_bits['message'])

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('svalenti@gmail.com', gmail_password)
        smtp.send_message(email)
