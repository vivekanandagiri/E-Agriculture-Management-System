from django.contrib.auth.backends import BaseBackend
from .models import Profile,User

class OTPBackend(BaseBackend):
    def authenticate(self, request, mobile=None, otp=None):
        try:
            profiles = Profile.objects.filter(mobile=mobile, otp=otp)
            if profiles.exists() and otp and request.session['otp'] == otp:
                return profiles.first().user  # Returns the user of the first matching profile
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
