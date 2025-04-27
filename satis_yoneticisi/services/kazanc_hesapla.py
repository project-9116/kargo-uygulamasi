def kar_belirleyici(alis_fiyati, kar_orani, sabit_kar_degeri, vergi_orani):
    # Kar belirleyici fonksiyonu
    # Alış fiyatı, kar oranı ve sabit kar değerine göre kar hesaplar

    # Kar hesaplama
    kar = alis_fiyati * (kar_orani / 100) + sabit_kar_degeri

    brut_kar = kar * vergi_orani

    return kar, brut_kar
