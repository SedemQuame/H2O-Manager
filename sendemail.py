# Try running this locally.
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "sedem.amekpewu.3@gmail.com",
              "to": ["sedem.amekpewu.3@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})
