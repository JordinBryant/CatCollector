from django.contrib import admin
from main_app.models import Cat
from .models import Cat, Feeding

# Register your models here.
admin.site.register(Cat)
admin.site.register(Feeding)