import numpy as np
import matplotlib.pyplot as plt

def fren_hesapla(hiz_kmh, k, tr):
    # Teknik Sorun Çözümü: Birim dönüşümü (km/h -> m/s)
    v = hiz_kmh / 3.6
    d_reaksiyon = v * tr
    d_frenleme = k * (v**2) # Karesel artış
    # %10 Güvenlik payı eklenmiş toplam mesafe
    d_toplam = (d_reaksiyon + d_frenleme) * 1.10
    return d_reaksiyon, d_frenleme, d_toplam

# Parametreler
hizlar = np.arange(20, 141, 5)
senaryolar = [
    {"ad": "S1: Kuru Asfalt", "k": 0.07, "tr": 1.0, "renk": "g"},
    {"ad": "S2: Islak Yol", "k": 0.10, "tr": 1.0, "renk": "orange"},
    {"ad": "S3: Buzlu Yol", "k": 0.15, "tr": 1.5, "renk": "r"}
]

# --- 1. ÇIKTI EKRANI (TABLO) ---
print("-" * 85)
print(f"{'Hız (km/h)':<12} | {'Senaryo':<18} | {'Reaksiyon (m)':<15} | {'Fren (m)':<10} | {'Toplam (m)':<10}")
print("-" * 85)
test_limitleri = [30, 70, 110, 130] # Örnek hızlar
for h in test_limitleri:
    for s in senaryolar:
        r, f, t = fren_hesapla(h, s["k"], s["tr"])
        print(f"{h:<12} | {s['ad']:<18} | {r:<15.2f} | {f:<10.2f} | {t:<10.2f}")
    print("-" * 85)

# Veri Hazırlama
grafik_verisi = {s["ad"]: {"t": [], "r": [], "f": [], "h": hizlar} for s in senaryolar}
for s in senaryolar:
    for h in hizlar:
        r, f, t = fren_hesapla(h, s["k"], s["tr"])
        grafik_verisi[s["ad"]]["t"].append(t)
        grafik_verisi[s["ad"]]["r"].append(r)
        grafik_verisi[s["ad"]]["f"].append(f)

# --- 2. GRAFİKLER ---

# GRAFİK 1: Karşılaştırmalı Toplam Durma Mesafesi (Senaryo Analizi)
plt.figure(figsize=(10, 5))
for s in senaryolar:
    plt.plot(hizlar, grafik_verisi[s["ad"]]["t"], label=s["ad"], color=s["renk"], linewidth=2)
plt.title("Grafik 1: Senaryolara Göre Toplam Durma Mesafesi Karşılaştırması")
plt.xlabel("Hız (km/h)")
plt.ylabel("Mesafe (metre)")
plt.legend()
plt.grid(True, alpha=0.3)

# GRAFİK 2: Buzlu Yolda Mesafe Dağılımı (Reaksiyon vs Frenleme)
# Görseldeki "reaksiyon bölgesinin ayrıştırılması" isteği için
plt.figure(figsize=(10, 5))
s3_ad = "S3: Buzlu Yol"
plt.stackplot(hizlar, grafik_verisi[s3_ad]["r"], grafik_verisi[s3_ad]["f"],
              labels=['Reaksiyon Mesafesi', 'Frenleme Mesafesi'], colors=['skyblue', 'salmon'])
plt.title("Grafik 2: Buzlu Yolda Mesafe Bileşenleri Analizi (Karesel Etki)")
plt.xlabel("Hız (km/h)")
plt.ylabel("Mesafe (metre)")
plt.legend(loc='upper left')
plt.grid(axis='y', alpha=0.3)

# GRAFİK 3: Hassasiyet Analizi (Türev Analizi - d'/dv)
# Görseldeki "hızdaki değişim şiddeti" yorumu için
plt.figure(figsize=(10, 5))
for s in senaryolar:
    hassasiyet = np.gradient(grafik_verisi[s["ad"]]["t"], hizlar)
    plt.plot(hizlar, hassasiyet, label=f"{s['ad']} Hassasiyet", color=s["renk"], linestyle='--')
plt.title("Grafik 3: Hassasiyet Analizi (Hız Artışının Mesafeye Etki Şiddeti)")
plt.xlabel("Hız (km/h)")
plt.ylabel("Ek Mesafe Artışı (m / km/h)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()