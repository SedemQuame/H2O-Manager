# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from soilmoisture import read_soil_moisture
import os


#MailGun Api Credentials.
#TODO: Change these values and make them environment variables.
MY_ADDRESS = 'postmaster@sandboxcc627e3c927541b881e3578abb398416.mailgun.org'
PASSWORD = 'be3af757e851e10a61d491b307150549-fd0269a6-ccdf32a0'
SMTP_HOST = "smtp.mailgun.org"

status = read_soil_moisture()
currentTime = status[0]
levelIndicator = status[1]

#Twilio Api Credentials.
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = os.environ['ACC_SID']
AUTH_TOKEN  = os.environ['AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(phones, message_template, names):
    #Simple function that sends sms using the twilio api
    for name, num in zip(names, phones):
            message = message_template.substitute(PERSON_NAME=name.title(), CAPACITY=(str(levelIndicator)+"%").title())
            message = client.messages \
                    .create(
                         body = message,
                         from_= TWILIO_NUMBER,
                         to = str(num)
                     )
    return(message.sid)



def send_email(names,message_template, emails):
    # set up the SMTP server
    s = smtplib.SMTP(host= SMTP_HOST, port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), CAPACITY=(str(levelIndicator)+"%").title())

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()



def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    phones = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(",")[0])
            emails.append(a_contact.split(",")[1])
            phones.append("+233" + str(a_contact.split(",")[2])[1:])
    return names, emails, phones

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def notifications():
    names, emails, phones = get_contacts('contacts.txt') # read contacts
    message_template = read_template('message.txt')
 
    #Send SMS using the twilio api.
    send_sms(phones, message_template, names)

    #Send EMAIL using the MailGun api.
    #send_email(names,message_template, emails)
