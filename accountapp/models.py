from django.db import models

class HelloWorld(models.Model):
    objects = None
    text = models.CharField(max_length=255, null=False)