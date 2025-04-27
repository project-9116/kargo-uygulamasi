from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(KargoFirmasi)
admin.site.register(KargoUcreti)
admin.site.register(KargoVergiOrani)
