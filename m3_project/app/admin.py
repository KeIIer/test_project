from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group, Permission, ContentType
# Register your models here.


@admin.register(Person)
class AdmPerson(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Permission)
class AdmPermission(admin.ModelAdmin):
    list_display = ('id', 'name')
