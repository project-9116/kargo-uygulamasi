def kar_belirleyici(alis_fiyati, kar_orani, sabit_kar_degeri, vergi_orani):
    # Kar belirleyici fonksiyonu
    # Alış fiyatı, kar oranı ve sabit kar değerine göre kar hesaplar

    # Kar hesaplama
    net_kar = alis_fiyati * (kar_orani / 100) + sabit_kar_degeri

    brut_kar = net_kar * vergi_orani

    return net_kar, brut_kar
