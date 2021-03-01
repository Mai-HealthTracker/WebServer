from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.TextField(max_length = 50) 
    email_id = models.EmailField( max_length=254)
    gender = models.TextField(max_length = 10)
    device_token = models.TextField(max_length = 200)
    def __str__(self):
        return self.name+" - "+self.email_id
