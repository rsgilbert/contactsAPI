from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    tel1 = models.CharField(max_length=255)
    tel2 = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    job = models.CharField(max_length=255, blank=True, default=",")
    sitename = models.CharField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return f'{self.firstname} {self.lastname}'



class Finance(models.Model):
    name = models.CharField(max_length=255)
    duty = models.CharField(max_length=255, blank=True, default=",")
    room = models.CharField(max_length=255, blank=True, default="")
    contact = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.name}'

