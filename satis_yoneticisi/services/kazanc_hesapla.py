def kar_belirleyici(alis_fiyati, kar_oran, sabit_kar_degeri):
    # Kar belirleyici fonksiyonu
    # Alış fiyatı, kar oranı ve sabit kar değerine göre kar hesaplar

    # Kar hesaplama
    kar = alis_fiyati * (kar_oran / 100) + sabit_kar_degeri

    return kar
