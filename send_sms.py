# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC214c46532167b2de9f4bfb537a3191cf'
auth_token = 'ad480870f128c2e3bbddf02f3a914ef5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19166190482',
                     to='+233546744163'
                 )

print(message.sid)

