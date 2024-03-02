from django.db import models


class Profile(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    profile_image = models.ImageField(blank=False)


class User(models.Model):
    login = models.CharField(max_length=20)
    email = models.EmailField()

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.login
    

    class Meta:
        ordering = ['login']


