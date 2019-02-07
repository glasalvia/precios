import smtplib
from email.mime.text import MIMEText as text

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("glasalviacalio@gmail.com", "leviatan01")

desde = 'Gonzalo'
para = 'glasalviacalio@gmail.com'


asunto = 'Prueba'
texto = 'Prueba'
mensaje = 'Subject: {}\n\n{}'.format(asunto, texto)


server.sendmail(desde, para, mensaje)