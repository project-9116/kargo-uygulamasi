# Generated by Django 5.2 on 2025-04-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='agirlik',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='urun',
            name='boy',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='urun',
            name='en',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='urun',
            name='yukseklik',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
