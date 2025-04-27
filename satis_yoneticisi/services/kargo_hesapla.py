KARGO_FIYAT_LISTESI = {
    "PTT": {0: 66.49, 1: 66.49, 2: 71.50, 3: 80.10},
}


def kargo_hesapla(kargo_ucreti, vergili_kargo_ucreti, alis_fiyati, kar_orani, sabit_kar_degeri):
    """
    Kargo ücretini hesaplar.
    """
    net_kar = alis_fiyati * kar_orani + sabit_kar_degeri
    satis_fiyati = alis_fiyati + net_kar + kargo_ucreti
    vergili_satis_fiyati = satis_fiyati * (1 + vergili_kargo_ucreti)
    toplam_vergi = vergili_satis_f
