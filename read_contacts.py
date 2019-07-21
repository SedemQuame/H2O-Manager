""" Add a database and then create method to read usernames and emails."""

#Function to read the contacs from a given contact file and return a
#list of names and email addresses.

def get_contacts(filename):
	#create lists to hold the various names and emails.
	names = []
	emails = []
	with open(filename, mode='r', encoding='utf-8') as contacts_file:
		for contact in contacts_file:
			names.append(contact.split()[0])
			emails.append(contact.split()[1])
		return names, emails
