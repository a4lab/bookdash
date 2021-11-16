from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
# from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True,null=True)
    # install pillow to manage images
    # pip install Pillow
    photo=models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    
    def __str__(self):
        return f'Profile for user {self.user.username}'




class Contact(models.Model):
    user_from=models.ForeignKey("auth.User",related_name="rel_from_set",on_delete=models.CASCADE)
    user_to=models.ForeignKey("auth.User",related_name="rel_to_set",on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_from} started following {self.user_to}' 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


user_model=get_user_model()
user_model.add_to_class("following",models.ManyToManyField('self',through=Contact,related_name='followers',symmetrical=False))