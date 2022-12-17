from django.contrib.auth.backends import ModelBackend

from .models import MyUser


class EmailorPhoneBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, phone=None, **kwargs):

        user = None
        if email is None:
            phone = phone

            if phone is None:
                return None
            else:

                try:
                    user = MyUser.objects.get(phone=phone)
                except MyUser.DoesNotExist:
                    return None
        else:
            try:
                user = MyUser.objects.get(email__iexact=email)
            except MyUser.DoesNotExist:
                return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            return None
