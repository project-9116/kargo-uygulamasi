from .kazanc_hesapla import kar_belirleyici


def trendyol_hesapla(komisyon_orani, vergi_orani, hizmet_degeri, stopaj_orani, kargo_ucreti, vergili_kargo_ucreti, alis_fiyati, kar_orani, sabit_kar_degeri):
    """
    Trendyol'da bir ürünün toplam maliyetini hesaplar.
    """
    net_kar, brut_kar = kar_belirleyici(
        alis_fiyati, kar_orani, sabit_kar_degeri, vergi_orani)

    satis_fiyati = (alis_fiyati + net_kar +
                    hizmet_degeri + kargo_ucreti)

    vergili_satis_fiyati = satis_fiyati * (1 + vergi_orani)

    toplam_vergi = vergili_satis_fiyati - satis_fiyati

    komisyon_degeri = vergili_satis_fiyati - komisyon_orani

    return
