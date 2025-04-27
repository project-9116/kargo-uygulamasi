from django.db import models


class KargoFirmasi(models.Model):
    ad = models.CharField(max_length=255, unique=True)
    etkin_mi = models.BooleanField(default=True)

    def __str__(self):
        return self.ad


class KargoUcreti(models.Model):
    kargo_firmasi = models.ForeignKey(
        KargoFirmasi, on_delete=models.CASCADE, related_name='ucretler')
    desi = models.PositiveIntegerField()
    ucret = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('kargo_firmasi', 'desi')
        ordering = ['kargo_firmasi', 'desi']

    def __str__(self):
        return f"{self.kargo_firmasi.ad} - {self.desi} desi: {self.ucret} TL"


class KargoVergiOrani(models.Model):
    vergi_orani = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Vergi Oranı: {self.vergi_orani}%"
