from django.db import models

# Create your models here.


class Payer(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
