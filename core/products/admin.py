from django.contrib import admin
from .models import Product,Categorie,Gender


admin.site.register([Gender,Product,Categorie])