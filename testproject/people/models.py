from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    address = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.address}"