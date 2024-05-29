from django.db import models

class Ankete(models.Model):
    ankete_id = models.AutoField(primary_key=True)
    login = models.TextField(unique=True, default="")
    password = models.TextField(default="")

    def __str__(self) -> str:
        return self.ankete_id


class Invitation(models.Model):
    invitation_id = models.AutoField(primary_key=True)
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    description = models.TextField()
    photo = models.TextField()

class OpenInfo(models.Model):
    ankete_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    description = models.TextField()

class ProfilePicture(models.Model):
    ankete_id = models.IntegerField(primary_key=True)
    profile_picture = models.TextField()

class ClosedInfo(models.Model):
    ankete_id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=20)

class PasswordRestoration(models.Model):
    ankete_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=10)

class Keywords(models.Model):
    ankete_id = models.IntegerField(primary_key=True)
    hobby = models.CharField(max_length=100)
    alcohol = models.CharField(max_length=100)
    smoking = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    zodiac_sign = models.CharField(max_length=20)
    height = models.IntegerField()
    why_here = models.TextField()
    marital_status = models.CharField(max_length=20)