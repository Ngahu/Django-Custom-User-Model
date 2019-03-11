from django.db import models


from django.contrib.auth.models import BaseUserManager,AbstractBaseUser







class User(AbstractBaseUser):
    """
    Description:This is going to be the main User Model.\n
    """
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    full_name = models.CharField(max_length=200,blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' 


    def __str__(self):
        return self.email

    
    def get_full_name(self):
        # The user is identified by their email address or full name
        pass    