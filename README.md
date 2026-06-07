# OTONOM ARAÇLARDA FREN MESAFESİ VE DEĞİŞİM ORANI ANALİZİ

Bu proje, otonom araçların farklı senaryolar altındaki frenleme performansını ve ivme değişimlerini Python kullanarak analiz etmek amacı ile geliştirilmiştir.

## PROJE EKİBİ
* Gülenaz BAYLAN
* Fatma AKINCI
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
* Dil:
  Python:Projenin mantıksal altyapısının kurulması ve simülasyon süreçlerinin yürütülmesi için temel programlama dili olarak kullanılmıştır.
* Kütüphaneler:
  Matplotlib:Simülasyonlardan elde edilen verilerin görselleştirilmesi, hız ve durma mesafesi arasındaki ilişkinin grafiksel olarak sunulması ve analizlerin doğruluğunun test edilmesi amacıyla kullanılmıştır.
  NumPy:Fren mesafesi analizi, hız değişimlerinin türevsel hesaplamaları ve karesel durma mesafesi fonksiyonlarının modellenmesi süreçlerinde, yüksek performanslı sayısal veri işlemleri için kullanılmıştır.

### Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırabilmek için aşağıdaki adımları izleyebilirsiniz:

**Repoyu Klonlayın:**
   Terminal üzerinden şu komutu kullanarak projeyi bilgisayarınıza kopyalayın:
   `git clone (https://github.com/Gulenazbaylan/python_proje1)`

**Çalıştırma:**
Gerekli kütüphaneler yüklendikten sonra, ana kod dosyanızı terminal veya bir Python IDE'si üzerinden çalıştırarak simülasyonu başlatabilirsiniz.

**Gerekli Kütüphaneleri Yükleyin:**
   Projenin düzgün çalışması için terminalde şu komutu çalıştırarak bağımlılıkları yükleyin:
```bash
   pip install numpy matplotlib


