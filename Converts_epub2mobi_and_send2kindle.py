#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
# Código creado por https://telegram.me/alfiles #
#################################################

#------------------------------------------------
# Programas necesarios                          #
#------------------------------------------------
# sudo apt install calibre --upgrade -y

import sys
from os import remove

def send_to_email(file):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.mime.base import MIMEBase
	from email import encoders
	 
	fromaddr = "Tu correo de gmail"
	toaddr = "El correo de tu kindle"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = file
	 
	body=""
	 
	msg.attach(MIMEText(body, 'plain'))
	 
	filename = file
	attachment = open(file, "rb")
	 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	msg.attach(part)
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "Contraseña de tu gmail") #<---------- Escribe la contraseña de tu gmail
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
  print ('El documento '+file+' se ha enviado correctamente')

def epub_mobi(file):
	from subprocess import call
	call(['ebook-convert', file, file[:-4]+'mobi'])
	send_an_email(file[:-4]+'mobi')
  try:
    remove(file)
  except:
    pass  
  remove(file[:-4]+'mobi')   

epub_mobi(sys.argv[1])
