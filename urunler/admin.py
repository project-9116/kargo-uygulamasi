from django.contrib import admin
from .models import Urun
from kargo.models import KargoFirmasi
from satis_yoneticisi.services.kargo_hesapla import kargo_hesapla, desi_heapla
from django.core.exceptions import MultipleObjectsReturned


class UrunAdmin(admin.ModelAdmin):
    list_display = ('ad', 'en', 'boy', 'yukseklik', 'agirlik',
                    'get_kargo_fiyatlari', 'get_desi')
    # readonly alan olarak ekle
    readonly_fields = ('get_kargo_fiyatlari', 'get_desi')

    @admin.display(description="Kargo Fiyatları")
    def get_kargo_fiyatlari(self, obj):
        """Ürüne ait kargo ücretlerini listele."""
        firma_adi_listesi = KargoFirmasi.objects.filter(
            etkin_mi=True).values_list('ad', flat=True)
        kargo_firmalari = list(firma_adi_listesi)

        # Kargo ücretlerini ve fiyatları hesapla
        try:
            result = kargo_hesapla(
                kargo_ucreti=0,  # Varsayılan kargo ücreti
                vergili_kargo_ucreti=0,  # Vergili kargo ücreti
                urun=obj,
                kargo_firmalari=kargo_firmalari
            )
        except MultipleObjectsReturned:
            return "Birden fazla KargoUcreti bulundu."

        fiyatlar = result["kargo_ucretleri"]
        return ', '.join([f"{firma}: {fiyat} TL" for firma, fiyat in fiyatlar.items() if fiyat is not None])

    @admin.display(description="Desi")
    def get_desi(self, obj):
        """Ürüne ait desiyi hesapla."""
        # Desi hesaplamak için desi_heapla fonksiyonunu çağırıyoruz
        desi_bolme_faktoru = 6000  # Bu değer genellikle 6000 olur, ihtiyaca göre ayarlanabilir
        desi = desi_heapla(urun=obj, desi_bolme_faktoru=desi_bolme_faktoru)
        return f"{desi:.2f} kg"


admin.site.register(Urun, UrunAdmin)
