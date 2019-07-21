# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
ACCOUNT_SID = 'AC214c46532167b2de9f4bfb537a3191cf'
AUTH_TOKEN  = 'ad480870f128c2e3bbddf02f3a914ef5'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms():
	""" Simple function that sends sms using the twilio api."""
	message = client.messages \
        	        .create(
                	     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
	                     from_='+19166190482',
        	             to='+233546744163'
                	 )
	print(message.sid)
	return(message.sid)

send_sms()

