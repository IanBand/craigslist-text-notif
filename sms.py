# https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/dyaguc6/?utm_source=reddit&utm_medium=web2x&context=3
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vzwpix.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = (os.getenv("PHONE_NUMBER") + '{}').format(carriers[os.getenv("CARRIER")])  #os.getenv("PHONE_NUMBER")
	auth = (os.getenv("EMAIL"), os.getenv("PASSWORD")) # must "allow less secure app acces" when using a gmail address

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)