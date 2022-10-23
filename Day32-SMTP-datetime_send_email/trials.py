import smtplib

sender = 'karennsample228@gmail.com'
receivers = ['smaple.karen@yahoo.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 80)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")