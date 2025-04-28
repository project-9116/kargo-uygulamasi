from django.db import models


class Urun(models.Model):
    ad = models.CharField(max_length=255, unique=True)
    en = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    boy = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    yukseklik = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    agirlik = models.DecimalField(max_digits=10, decimal_places=2, default=1)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = 'Ürünler'

    def __str__(self):
        return self.ad
