from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

# Class for the owner of the invoice

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_user = models.CharField(max_length=26,blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField()
    created =  models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of the user: {self.user.username}"

    # add later 
    # avatar = 
    # company_logo = 