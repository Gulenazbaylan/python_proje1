# Basit Fren Mesafesi ve Türev Analizi

def analiz_et(hiz_kmh):
    # Sabitler
    g = 9.81  # Yerçekimi ivmesi (m/s^2)
    mu = 0.7  # Sürtünme katsayısı (Kuru asfalt için ortalama)

    # Hızı km/h'den m/s'ye çeviriyoruz
    v = hiz_kmh / 3.6

    # Fren Mesafesi Fonksiyonu: d(v) = v^2 / (2 * mu * g)
    mesafe = (v ** 2) / (2 * mu * g)

    # Değişim Hızı (Türev): d'(v) = v / (mu * g)
    # Bu değer, hız 1 m/s arttığında mesafenin kaç metre artacağını gösterir
    degisim_hizi = v / (mu * g)

    return mesafe, degisim_hizi


# Örnek Kullanım
hiz = 50  # km/h
m, d = analiz_et(hiz)

print(f"Hız: {hiz} km/h")
print(f"Hesaplanan Fren Mesafesi: {m:.2f} metre")
print(f"Anlık Değişim Hızı (Türev): {d:.2f}")