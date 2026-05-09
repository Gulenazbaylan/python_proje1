# OTONOM ARAÇLARDA FREN MESAFESİ VE DEĞİŞİM ORANI ANALİZİ

Bu proje, otonom araçların farklı senaryolar altındaki frenleme performansını ve ivme değişimlerini Python kullanarak analiz etmek amacı ile geliştirilmiştir.

## PROJE EKİBİ
* Gülenaz BAYLAN
* **Fatma AKINCI
* İlayda ŞEN

## Deney / Test Düzeni
Proje kapsamında, aracın durma mesafesini etkileyen fiziksel değişkenler simüle edilmiştir.

* Hangi örnekler denenmiştir?: Şehir içi (50 km/h), otoyol (90 km/h) ve yüksek hız (120 km/h) limitleri test edilmiştir.
* Hangi parametreler seçilmiştir?:
    * Başlangıç hızı 
    * Sürtünme katsayısı  
    * Sistem tepki süresi 

## Ön Bulgular
Simülasyon sonucunda elde edilen ilk veriler şunları göstermektedir:
* Hız Etkisi: Fren mesafesi, hızın karesiyle doğru orantılı olarak artmaktadır.
* Zemin Etkisi: Islak zeminde sürtünme katsayısının düşmesi, durma mesafesini yaklaşık %40 oranında artırmıştır.
* Beklenen vs. Beklenmeyen: Sabit bir yavaşlama eğrisi beklenirken, yüksek hızlarda ivme değişim oranındaki ani artışların sürüş konforunu olumsuz etkilediği gözlemlenmiştir.

## Karşılaşılan Sorunlar ve Çözüm Planı
Proje sürecinde karşılaşılan teknik zorluklar ve uygulanan çözümler şunlardır:
* Kod ve Grafik: Grafiklerdeki verilerin üst üste binmesi sorunu, Matplotlib kütüphanesindeki subplots ve legend özellikleri optimize edilerek çözülmüştür.
* Model ve Veri: Bazı ekstrem hız değerlerinde fiziksel olarak imkansız sonuçlar oluşmuş; bu durum, matematiksel modele sınırlayıcı fonksiyonlar eklenerek düzeltilmiştir.
* Yorumlama: Verilerin grafiksel dağılımının analizi sırasında oluşan karmaşıklık, verileri standardize ederek giderilmiştir.

## Teknik Ayrıntılar
* En az 3 farklı senaryo test edildi.
* Sonuçlar grafiklerle gösterildi.
* Hata ve sınırlılık örnekleri simülasyona dahil edildi.

## Kullanılan Teknolojiler
* Dil: Python
* Kütüphaneler: Matplotlib, NumPy
