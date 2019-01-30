from django.contrib import admin

# Register your models here.
from .models import Call, Type

admin.site.register(Call)
admin.site.register(Type)
