from decimal import Decimal
from kargo.models import *
from urunler.models import Urun


def desi_heapla(urun: Urun, desi_bolme_faktoru):
    """
    Ürünün desisini hesaplar.
    """
    # Hacimsel desi hesaplama
    hacim_desi = (urun.en * urun.boy * urun.yukseklik) / desi_bolme_faktoru
    # En yüksek değer ağırlık ve hacimsel desinin karşılaştırılmasıyla belirlenir
    desi = max(hacim_desi, urun.agirlik)
    return desi


def kargo_hesapla(kargo_ucreti, vergili_kargo_ucreti, urun: Urun, kargo_firmalari: list[KargoFirmasi]):

    # Kargo ücretini hesaplar.
    ucretler = []

    # Kargo firmalarına göre ücret hesaplama
    for firma_adi in kargo_firmalari:
        try:
            firma = KargoFirmasi.objects.get(ad=firma_adi, etkin_mi=True)
            desi = desi_heapla(urun, firma.desi_bolme_faktoru)
            ucret_kaydi = KargoUcreti.objects.get(
                kargo_firmasi=firma, desi__gte=desi)
            ucretler.append({
                "firma_adi": firma_adi,
                "ucret": float(ucret_kaydi.ucret)
            })
        except KargoFirmasi.DoesNotExist:
            ucretler.append({
                "firma_adi": firma_adi,
                "ucret": None
            })
        except KargoUcreti.DoesNotExist:
            ucretler.append({
                "firma_adi": firma_adi,
                "ucret": None
            })

    return {
        "kargo_ucretleri": ucretler,
    }
