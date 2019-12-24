from django.db import models

# Create your models here.

class Data(models.Model):
    key = models.CharField(max_length = 100)
    value = models.CharField(max_length = 1000)

    def __str__(self):
        return '{}:{}'.format(self.key, self.value)
    