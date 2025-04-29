# forms.py

from django import forms
from .models import Kisi, TuzelTuru, KisiTuru

class KisiForm(forms.ModelForm):
    class Meta:
        model = Kisi
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Kişi türü seçildiğinde tüzel kişi türünü göster
        if self.instance and self.instance.kisi_turu and self.instance.kisi_turu.adi == 'Tüzel Kişi':
            self.fields['tuzel_turu'].queryset = TuzelTuru.objects.all()
            self.fields['sirket_adi'].required = True  # Şirket adı zorunlu
            self.fields['vergi_no'].required = True  # Vergi no zorunlu

    def clean(self):
        cleaned_data = super().clean()
        kisi_turu = cleaned_data.get('kisi_turu')

        if kisi_turu and kisi_turu.adi == 'Gerçek Kişi':
            if not cleaned_data.get('ad') or not cleaned_data.get('soyad'):
                raise forms.ValidationError("Gerçek kişi için ad ve soyad zorunludur.")
        elif kisi_turu and kisi_turu.adi == 'Tüzel Kişi':
            if not cleaned_data.get('sirket_adi') or not cleaned_data.get('vergi_no') or not cleaned_data.get('tuzel_turu'):
                raise forms.ValidationError("Tüzel kişi için şirket adı, vergi no ve türü zorunludur.")
        return cleaned_data
