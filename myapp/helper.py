from django.conf import settings
from twilio.rest import Client


class MessageHandler:
    mobile=None
    otp=None
    def __init__(self,mobile,otp) -> None:
        self.mobile=mobile
        self.otp=otp
    def send_otp_via_message(self):    
        client= Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
        message=client.messages.create(body=f'ନମସ୍କାର ଆପଣଙ୍କୁ AgriAi କୁ ସ୍ଵାଗତ। Your Agrai OTP Verification code is: {self.otp}.Please do not share with anyone.-AgriAi Team',from_=f'{settings.TWILIO_PHONE_NUMBER}',to=f' {settings.COUNTRY_CODE}{self.mobile}')
    