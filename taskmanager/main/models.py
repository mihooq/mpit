from django.db import models


class Logins(models.Model):
    log = models.CharField(max_length=200)

    def __str__(self):
        return self.log

class Passwords(models.Model):
    logins = models.ForeignKey(Logins, on_delete=models.CASCADE)
    pword = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.pword

# Create your models here.
