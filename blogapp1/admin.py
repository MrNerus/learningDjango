from django.contrib import admin
from . models import *
# Register your models here.

class ContactView(admin.ModelAdmin):
    list_display=['id','name','email','address','message']
admin.site.register(Contact, ContactView)

