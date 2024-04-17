from django.db import models

# Create your models here.


class Members(models.Model):
    # Represents slacks user_id given
    user_id = models.CharField(max_length=255, null=False)
    # Represents users nickname ->  ( @username )
    username = models.CharField(max_length=255, null=False)
    
