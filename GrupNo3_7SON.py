
"""
PROJE: Otonom Araçlarda Fren Mesafesi: Türev ve Değişim Hızı Analizi
GRUP NO: 3
ÖĞRENCİLER: İlayda ŞEN, Fatma AKINCI, Gülenaz BAYLAN
"""

import numpy as np
import matplotlib.pyplot as plt


def birim_donustur(hiz_kmh):
    """Hızı km/h biriminden m/s birimine dönüştürür."""
    return hiz_kmh / 3.6


def reaksiyon_mesafesi_hesapla(v_ms, t_reaksiyon=0.5):
    """Otonom sistemin karar sürecindeki doğrusal yolu hesaplar (d = v * t)."""
    return v_ms * t_reaksiyon


def fren_mesafesi_hesapla(v_ms, k=0.072835):
    """Fiziksel frenleme anındaki karesel yolu hesaplar (d = k * v^2)."""
    return k * (v_ms ** 2)


def anlik_degisim_hizi_hesapla(v_ms, t_reaksiyon=0.5, k=0.072835):
    """Toplam durma mesafesinin hıza göre türevini hesaplar: D'(v) = t_r + 2kv."""
    return t_reaksiyon + (2 * k * v_ms)


def otonom_surus_simulasyonu(hiz_listesi):
    """Yasal hız sınırları için analiz yapar ve sonuçları tablo halinde basar."""
    k_sabiti = 0.072835
    t_r = 0.5
    hata_payi = 0.10  # %10 emniyet marjı

    print("\n" + "=" * 84)
    print(f"{'TABLO 1: YASAL HIZ SINIRLARINA GÖRE ANALİZ VE TÜREV SONUÇLARI':^84}")
    print("=" * 84)
    print(
        f"{'Hız (km/h)':<12} | {'Hız (m/s)':<10} | {'Toplam Mesafe (m)':<18} | {'Emniyetli Mesafe (m)':<22} | {'Türev (Hassasiyet)':<18}")
    print("-" * 84)

    for hiz in hiz_listesi:
        v = birim_donustur(hiz)
        d_r = reaksiyon_mesafesi_hesapla(v, t_r)
        d_f = fren_mesafesi_hesapla(v, k_sabiti)
        d_toplam = d_r + d_f
        d_emniyet = d_toplam * (1 + hata_payi)
        turev = anlik_degisim_hizi_hesapla(v, t_r, k_sabiti)

        print(f"{hiz:<12} | {v:<10.2f} | {d_toplam:<18.2f} | {d_emniyet:<22.2f} | {turev:<18.2f}")
    print("=" * 84 + "\n")


def sunum_senaryosu_calistir(senaryo_hizi=100):
    """Sunumda jüriye anlatılacak kritik durum senaryosunun adımları."""
    k_sabiti = 0.072835
    t_r = 0.5
    hata_payi = 0.10

    v = birim_donustur(senaryo_hizi)
    d_r = reaksiyon_mesafesi_hesapla(v, t_r)
    d_f = fren_mesafesi_hesapla(v, k_sabiti)
    d_toplam = d_r + d_f
    d_emniyet = d_toplam * (1 + hata_payi)
    turev = anlik_degisim_hizi_hesapla(v, t_r, k_sabiti)

    print("=" * 84)
    print(f"{'SUNUM İÇİN ÖRNEK ÇALIŞMA SENARYOSU (KRİTİK DURUM ANALİZİ)':^84}")
    print("=" * 84)
    print(f"Senaryo: Otonom aracımız otobanda {senaryo_hizi} km/h sabit hızla ilerlemektedir.")
    print("-" * 84)
    print(f"1. Birim Dönüşümü          : v = {v:.2f} m/s")
    print(f"2. Reaksiyon Mesafesi (d_r): d_r = {d_r:.2f} metre (Doğrusal bileşen)")
    print(f"3. Fiziksel Frenleme (d_f) : d_f = {d_f:.2f} metre (Karesel bileşen)")
    print(f"4. Net Durma Mesafesi (D)  : D = {d_toplam:.2f} metre")
    print(f"5. Dinamik Emniyet Payı    : D_emniyet = {d_emniyet:.2f} metre")
    print(f"6. Anlık Değişim Hızı (Türev): D'(v) = {turev:.2f}")
    print("-" * 84)



def ayrilmis_grafikleri_ciz(hiz_ust_limit=140, senaryo_hizi=100):
    """Matematiksel modelin tüm bileşenlerini AYRI AYRI grafiklerde gösterir."""
    hizlar_kmh = np.linspace(0, hiz_ust_limit, 100)
    v_ms = birim_donustur(hizlar_kmh)

    # Veri Hesaplamaları
    d_reaksiyon = reaksiyon_mesafesi_hesapla(v_ms)
    d_fren = fren_mesafesi_hesapla(v_ms)
    d_toplam = d_reaksiyon + d_fren
    d_emniyet = d_toplam * 1.10
    turev_degerleri = anlik_degisim_hizi_hesapla(v_ms)

    v_kritik = birim_donustur(senaryo_hizi)

    # -------------------------------------------------------------
    # GRAFİK 1: Reaksiyon Mesafesi (Doğrusal Değişim)
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(hizlar_kmh, d_reaksiyon, color='skyblue', linewidth=2.5, label='Reaksiyon Mesafesi $d_r(v)$')
    plt.fill_between(hizlar_kmh, 0, d_reaksiyon, color='skyblue', alpha=0.2)
    plt.scatter([senaryo_hizi], [reaksiyon_mesafesi_hesapla(v_kritik)], color='black', zorder=5)
    plt.title(r'1. Reaksiyon Mesafesi Analizi (Doğrusal Model: $v \cdot t_r$)', fontweight='bold')
    plt.xlabel('Araç Hızı (km/h)')
    plt.title(r'1. Reaksiyon Mesafesi Analizi (Doğrusal Model: $v \cdot t_r$)', fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # -------------------------------------------------------------
    # GRAFİK 2: Fiziksel Fren Mesafesi (Karesel Değişim)
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(hizlar_kmh, d_fren, color='salmon', linewidth=2.5, label='Saf Fren Mesafesi $d_f(v)$')
    plt.fill_between(hizlar_kmh, 0, d_fren, color='salmon', alpha=0.2)
    plt.scatter([senaryo_hizi], [fren_mesafesi_hesapla(v_kritik)], color='black', zorder=5)
    plt.title(r'2. Fiziksel Frenleme Mesafesi Analizi (Karesel Model: $k \cdot v^2$)', fontweight='bold')
    plt.xlabel('Araç Hızı (km/h)')
    plt.ylabel('Mesafe (metre)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # -------------------------------------------------------------
    # GRAFİK 3: Toplam Durma Mesafesi ve Emniyet Sınırı
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(hizlar_kmh, d_toplam, color='red', linewidth=2, label='Toplam Durma Mesafesi $D(v)$')
    plt.plot(hizlar_kmh, d_emniyet, color='darkred', linestyle='--', linewidth=2,
             label='Emniyetli Takip Mesafesi (%10 Marjlı)')
    d_kritik = reaksiyon_mesafesi_hesapla(v_kritik) + fren_mesafesi_hesapla(v_kritik)
    plt.scatter([senaryo_hizi], [d_kritik], color='black', s=80, zorder=5)
    plt.text(senaryo_hizi - 25, d_kritik + 10, f'{senaryo_hizi} km/h -> {d_kritik:.1f} metre', fontweight='bold',
             bbox=dict(facecolor='white', alpha=0.8))
    plt.title('3. Toplam Durma ve Emniyetli Takip Mesafesi Modeli', fontweight='bold')
    plt.xlabel('Araç Hızı (km/h)')
    plt.ylabel('Toplam Mesafe (metre)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # -------------------------------------------------------------
    # GRAFİK 4: Anlık Değişim Hızı (TÜREV GRAFİĞİ)
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(hizlar_kmh, turev_degerleri, color='purple', linewidth=2.5, label="Anlık Değişim Hızı $D'(v) = t_r + 2kv$")
    plt.fill_between(hizlar_kmh, 0, turev_degerleri, color='purple', alpha=0.1)
    t_kritik = anlik_degisim_hizi_hesapla(v_kritik)
    plt.scatter([senaryo_hizi], [t_kritik], color='black', s=80, zorder=5)
    plt.text(senaryo_hizi - 25, t_kritik + 0.4, f'Tüv. Hassasiyeti: {t_kritik:.2f}', fontweight='bold',
             bbox=dict(facecolor='white', alpha=0.8))
    plt.title("4. Diferansiyel Analiz: Durma Mesafesinin Hıza Göre Türevi", fontweight='bold')
    plt.xlabel('Araç Hızı (km/h)')
    plt.ylabel("Değişim Şiddeti ($dD/dv$)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Tüm grafikleri ekranda ayrı pencereler halinde patlatır
    plt.show()


# --- ANA PROGRAM ÇALIŞTIRMA ---
if __name__ == "__main__":
    test_hizlari = [30, 50, 70, 90, 110, 130]

    # 1. Akademik Veri Tablosu
    otonom_surus_simulasyonu(test_hizlari)

    # 2. Özel Sunum Senaryosu Metni
    sunum_senaryosu_calistir(senaryo_hizi=100)

    # 3. Bağımsız 4 Grafik Penceresi
    ayrilmis_grafikleri_ciz(hiz_ust_limit=140, senaryo_hizi=100)