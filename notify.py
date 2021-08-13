import smtplib
from email.message import EmailMessage
import imghdr

def sendComic(fromaddr, passwd, recipient, subject):
	msg = EmailMessage()
	msg['subject'] = subject
	msg['from'] = fromaddr
	msg['to'] = recipient
	msg.set_content('Comic Attached')

	with open('comic.png', 'rb') as f:
		fdata = f.read()
		ftype = imghdr.what(f.name)
		fname = f.name

	msg.add_attachment(fdata, maintype='img', subtype=ftype, filename=fname)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

		server.login(user=fromaddr, password=passwd)

		server.send_message(msg)
