from django.contrib import admin
from .models import Kisi, KisiTuru, TuzelTuru
from .forms import KisiForm

class KisiAdmin(admin.ModelAdmin):
    form = KisiForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Yeni kişi ekleniyorsa
        if not obj:
            kisi_turu_field = form.base_fields.get('kisi_turu')
            if kisi_turu_field:
                try:
                    # Varsayılan olarak 'Gerçek Kişi'yi seçili yap
                    kisi_turu_field.initial = KisiTuru.objects.get(adi="Gerçek Kişi")
                except KisiTuru.DoesNotExist:
                    pass  # 'Gerçek Kişi' türü yoksa hiçbir şey yapma

        return form

    class Media:
        js = ('kisiler/js/kisi_admin.js',)

admin.site.register(Kisi, KisiAdmin)
admin.site.register(KisiTuru)
admin.site.register(TuzelTuru)
