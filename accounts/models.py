from django.db import models


from django.contrib.auth.models import BaseUserManager,AbstractBaseUser







class User(AbstractBaseUser):
    """
    Description:This is going to be the main User Model.\n
        So you can either choose to use the email as the unique identifier or the username field.
        Default:email field 
        first_name:  default blank allowed
        last_name: default blank allowed
        active:True #Whether  user can login or not
        staff:a superuser
        admin:non super user
        timestamp:When user was created
    """
    email = models.EmailField(db_index=True,verbose_name='email address',max_length=255,unique=True)
    # email_confirmed = models.BooleanField(default=False)
    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    active = models.BooleanField(default=True)  #can login or not
    staff = models.BooleanField(default=False) # a superuser
    admin = models.BooleanField(default=False) # a admin user; non super-user
    timestamp = models.DateTimeField(auto_now_add=True)
    # notice the absence of a "Password field", that's built in.


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []






    def __str__(self):
        return self.email

    
    def get_full_name(self):
        # The user is identified by their email address or full name
        pass    