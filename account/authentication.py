from django.contrib.auth.models import User

class EmailAuthBackend(object):
    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
    def get_user(self,uid):
        try:
            return User.objects.get(id=uid)
        except User.DoesNotExist:
            return None
