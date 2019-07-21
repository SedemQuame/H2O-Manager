""" Sending emails using MIME technology. """

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#For each contact, send the email

for name, email in zip(names, emails):
	msg = MIMEMultipart()		#Create a message.

	# adding actual person to the message template
	message = message_template.substitute(PERSON_NAME=name.title())

	#setup the parameters of the message.
	msg['From'] = address
	msg['To']   = email
	msg['Subject'] = "This is a simple test"

	#add in the message body
	msg.attach(MIMEText(message, 'plain'))

	#send the message via the server set up earlier.
	s.send_message(msg)

	del msg
