from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField(max_length=200, null=True)
    zip_code = models.IntegerField(null = True)    

    class Meta:
        unique_together = (("name", "zip_code"),)