import numpy as np
     #k sabiti 
k_sabiti = 0.072835

     #Fren mesafesi fonksiyonu,
def fren_mesafesi_hesapla(v_kmh):
    """Aracın km/h cinsinden hızı için fren mesafesini (metre) hesaplar."""
    v_ms = v_kmh / 3.6  # km/h'den m/s'ye dönüşüm
    return k_sabiti * (v_ms ** 2)

     #Değişim hızı fonksiyonu,
def anlik_degisim_hizi_hesapla(v_kmh):
    """Aracın hızı için durma mesafesindeki anlık değişim hızını (türev) hesaplar."""
    v_ms = v_kmh / 3.6
    return 2 * k_sabiti * v_ms


#Ödevimize göre 2 farklı örnek girdi için hesaplamalar:
ornek_hizlar = [50, 80]

print(" Otonom Araç Fren Analizi İlk Hesaplamalar")
for hiz in ornek_hizlar:
    mesafe = fren_mesafesi_hesapla(hiz)
    turev = anlik_degisim_hizi_hesapla(hiz)

    print(f"Girdi Hızı: {hiz} km/h")
    print(f"Hesaplanan Fren Mesafesi: {mesafe:.2f} metre")
    print(f"Anlık Değişim Hızı (Türev Değeri): {turev:.2f}")
    print("-" * 45)
    