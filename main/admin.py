from django.contrib import admin
from .models import *

# Register your models here.


model_classes = [User, Category, Photo]

for model in model_classes:
    admin.site.register(model)
    