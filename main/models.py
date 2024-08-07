from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title



