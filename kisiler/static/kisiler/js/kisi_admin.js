document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript dosyası yüklendi!");

    // Kişi türü seçeneğini alıyoruz
    var kisiTuruField = document.querySelector('select[name="kisi_turu"]');
    console.log("Kişi Türü Alanı: ", kisiTuruField);

    // Gerçek kişi alanlarını alıyoruz
    var adSoyadFields = document.querySelectorAll('.field-ad, .field-soyad, .field-tc_kimlik_no');
    console.log("Gerçek Kişi Alanları: ", adSoyadFields);

    // Tüzel kişi alanlarını alıyoruz
    var sirketVergiFields = document.querySelectorAll('.field-sirket_adi, .field-vergi_no, .field-tuzel_turu');
    console.log("Tüzel Kişi Alanları: ", sirketVergiFields);

    // Kişi türüne göre alanları dinamik olarak gösterme
    function toggleFields() {
        var kisiTuruValue = kisiTuruField.options[kisiTuruField.selectedIndex].text;  // Seçilen kişi türünün metni
        console.log("Kişi Türü Seçildi: ", kisiTuruValue);

        // Gerçek Kişi seçildiğinde
        if (kisiTuruValue === 'Gerçek Kişi') {
            adSoyadFields.forEach(function(field) {
                field.style.display = 'block';  // Gerçek kişi alanlarını göster
            });
            sirketVergiFields.forEach(function(field) {
                field.style.display = 'none';  // Tüzel kişi alanlarını gizle
            });
        }
        // Tüzel Kişi seçildiğinde
        else if (kisiTuruValue === 'Tüzel Kişi') {
            adSoyadFields.forEach(function(field) {
                field.style.display = 'none';  // Gerçek kişi alanlarını gizle
            });
            sirketVergiFields.forEach(function(field) {
                field.style.display = 'block';  // Tüzel kişi alanlarını göster
            });
        }
        // Diğer durumlar (varsayılan veya tanımlanmamış türler)
        else {
            adSoyadFields.forEach(function(field) {
                field.style.display = 'none';  // Gerçek kişi alanlarını gizle
            });
            sirketVergiFields.forEach(function(field) {
                field.style.display = 'none';  // Tüzel kişi alanlarını gizle
            });
        }
    }

    // Sayfa yüklendiğinde alanları kontrol et
    toggleFields();

    // Kişi türü değiştiğinde alanları tekrar kontrol et
    kisiTuruField.addEventListener('change', toggleFields);
});
