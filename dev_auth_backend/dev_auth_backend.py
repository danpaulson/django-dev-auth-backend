from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class DevAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if settings.DEBUG:
            User = get_user_model()
            try:
                # Here we check if the password equals 'dev_password', or any string you want.
                if password == getattr(settings, 'DEV_AUTH_BACKEND_PASSWORD', 'dev_password'):
                    return User.objects.get(username=username)
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
