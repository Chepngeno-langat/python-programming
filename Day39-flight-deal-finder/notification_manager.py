from twilio.rest import Client

TWILIO_AUTH_TOKEN = "xxxxxxxx"
TWILIO_SID = "xxxxxxx"
TWILIO_NUMBER = "xxxxxxxx"
MY_NUMBER = "xxxxxxxx"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self,message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )

        print(message.sid)