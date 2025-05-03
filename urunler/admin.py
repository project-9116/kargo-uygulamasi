from django.contrib import admin
from .models import Urun
from kargo.models import *
from satis_yoneticisi.services.kargo_hesapla import kargo_hesapla, desi_heapla
from django.core.exceptions import MultipleObjectsReturned
from django.utils.html import format_html


class UrunAdmin(admin.ModelAdmin):
    list_display = ('ad', 'en', 'boy', 'yukseklik',
                    'agirlik', 'get_desi_ve_ucretler')
    readonly_fields = ('get_desi_ve_ucretler',)

    @admin.display(description="Kargo Firmalarınca Desi Ücreti")
    def get_desi_ve_ucretler(self, obj):
        aktif_firmalar = KargoFirmasi.objects.filter(etkin_mi=True)
        satirlar = []

        for firma in aktif_firmalar:
            desi_bolme_faktoru = firma.desi_bolme_faktoru or 3000
            desi = desi_heapla(urun=obj, desi_bolme_faktoru=desi_bolme_faktoru)
            desi_rounded = int(desi)  # KargoUcreti desi alanı tam sayı

            # Uygun kargo ücretini bul
            ucret_kaydi = KargoUcreti.objects.filter(
                kargo_firmasi=firma, desi__gte=desi_rounded
            ).order_by('desi').first()

            if ucret_kaydi:
                ucret = f"{ucret_kaydi.ucret:.2f} TL"
            else:
                ucret = "Ücret bulunamadı"

            satirlar.append(
                # f"<strong>{ucret_kaydi.pazaryeri} > {firma.ad}:</strong> {desi:.2f} desi ücreti: {ucret} + vergi = <hr>"
                f"<strong>{ucret_kaydi.pazaryeri} & {firma.ad}:</strong> {ucret}<hr>"
            )

        return format_html("{}", format_html("".join(satirlar)))


admin.site.register(Urun, UrunAdmin)
