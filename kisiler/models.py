from django.db import models

# KisiTuru ve TuzelTuru modelleri
class KisiTuru(models.Model):
    adi = models.CharField(max_length=100)

    def __str__(self):
        return self.adi

class TuzelTuru(models.Model):
    adi = models.CharField(max_length=100)

    def __str__(self):
        return self.adi

# Kisi modelini güncelleme
class Kisi(models.Model):
    kisi_turu = models.ForeignKey(KisiTuru, on_delete=models.CASCADE, null=True, blank=True)
    
    # Gerçek Kişi alanları
    ad = models.CharField(max_length=100, blank=True, null=True)
    soyad = models.CharField(max_length=100, blank=True, null=True)
    tc_kimlik_no = models.CharField(max_length=11, blank=True, null=True)
    
    # Tüzel Kişi alanları
    sirket_adi = models.CharField(max_length=255, blank=True, null=True)
    vergi_no = models.CharField(max_length=10, blank=True, null=True)
    tuzel_turu = models.ForeignKey(TuzelTuru, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.ad} {self.soyad}" if self.kisi_turu.adi == 'Gerçek Kişi' else self.sirket_adi