from django.db import models


# Create your models here.

class Project(models.Model):
    objects = None
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    # 파이썬 내부 함수 (string 치환..?)
    def __str__(self):
        return f'{self.pk} : {self.title}'

