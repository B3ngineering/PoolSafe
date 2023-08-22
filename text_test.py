import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
sender = 'bengeorgeyoung@gmail.com'
passwd = 'kqgxvlcuzblcilcp'
server.login(sender, passwd)
message = 'Hi'


server.sendmail(sender, 'bengeorgeyoung@gmail.com', message)
