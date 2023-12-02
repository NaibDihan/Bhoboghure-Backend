from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=11)

    def __str_(self):
        return self.name 