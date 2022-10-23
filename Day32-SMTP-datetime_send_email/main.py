import smtplib

my_email = "karennsample228@gmail.com"
password = "chep09012002"

connection = smtplib.SMTP("smtp.gmail.com")
#connection.connect()
#connection.ehlo()
connection.starttls()
#connection.ehlo()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="smaple.karen@yahoo.com", msg="Hello")
connection.close()
