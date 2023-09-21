from django.contrib import admin
from .models import User, Owner, UserProgress, Product, ProductCompound, Lesson, Access

myModels = [User, Owner, UserProgress, Product, ProductCompound, Lesson, Access]
admin.site.register(myModels)
