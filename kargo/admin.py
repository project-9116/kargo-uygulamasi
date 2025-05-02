from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(KargoUcreti)
class KargoUcretiAdmin(admin.ModelAdmin):
    list_display = ['pazaryeri', 'kargo_firmasi', 'desi', 'ucret']

    @admin.display(description="Kargo Bilgisi")
    def kargo_bilgisi(self, obj):
        return str(obj)


admin.site.register(KargoFirmasi)
admin.site.register(KargoVergiOrani)
admin.site.register(Pazaryeri)
