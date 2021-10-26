
""" Everything with $ need to be replaced"""

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html_file = Template(Path('index.html').read_text())  #index.html is a file we are using to make our mail specific
email = EmailMessage()
email['from'] = '$YOUR_NAME'
email['to'] = '$EMAIL_OF_RECEIVER'
email['subject'] = '$SUBJECT'

email.set_content(html_file.substitute(name ='$NAME_HERE'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()  
	smtp.starttls() 
	smtp.login('$YOUR_GMAIL_HERE', '$PASSWORD_HERE')
	smtp.send_message(email)
	print('Mail sended')