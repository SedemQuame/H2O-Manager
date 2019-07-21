""" A program to setup smtp credentials for sending emails. """

#import the smtplib module. It should be included in Python by default.
import smtplib

#set up the SMTP server.
smtp_host = "smtp.mailgun.org"
address = "postmaster@sandboxcc627e3c927541b881e3578abb398416.mailgun.org"
password = "be3af757e851e10a61d491b307150549-fd0269a6-ccdf32a0"

s = smtplib.SMTP(host = smtp_host, port = 587)
s.starttls()
s.login(address, password)
