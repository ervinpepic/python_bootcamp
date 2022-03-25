import os
from twilio.rest import Client

TWILIO_SID = ""
AUTH_TOKEN = ""
NUMBER = ""
VERIFIED_NUMBER = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=NUMBER,
            to=VERIFIED_NUMBER
        )
        print(message.sid)
