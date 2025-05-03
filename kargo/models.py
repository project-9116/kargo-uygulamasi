from django.db import models

class KargoVergiOrani(models.Model):
    vergi_orani = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Kargo Vergisi Oranı"
        verbose_name_plural = 'Kargo Vergisi Oranları'

    def __str__(self):
        return f"Vergi Oranı: {self.vergi_orani}%"

class KargoFirmasi(models.Model):
    ad = models.CharField(max_length=255, unique=True)
    etkin_mi = models.BooleanField(default=True)

    desi_bolme_faktoru = models.DecimalField(
        max_digits=10, decimal_places=2, default=3000.00, blank=True, null=True)  # Varsayılan 3000

    class Meta:
        verbose_name = "Kargo İşletmesi"
        verbose_name_plural = 'Kargo İşletmeleri'

    def __str__(self):
        return self.ad

class Pazaryeri(models.Model):
    ad = models.CharField(max_length=255, unique=True)
    etkin_mi = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Pazaryeri"
        verbose_name_plural = 'Pazaryerleri'

    def __str__(self):
        return self.ad


class KargoUcreti(models.Model):
    kargo_firmasi = models.ForeignKey(
        KargoFirmasi, on_delete=models.CASCADE, related_name='kargo_ucretleri')
    pazaryeri = models.ForeignKey(
        Pazaryeri, on_delete=models.CASCADE, related_name='pazaryeri_ucretleri', blank=True, null=True)
    desi = models.PositiveIntegerField()
    ucret = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('kargo_firmasi', 'desi', 'pazaryeri')
        ordering = ['kargo_firmasi', 'desi']
        verbose_name = "Kargo Ücreti"
        verbose_name_plural = 'Kargo Ücretleri'

    def __str__(self):
        return f"{self.kargo_firmasi.ad} - {self.desi} desi: {self.ucret} TL"





