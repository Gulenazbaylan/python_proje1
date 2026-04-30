import numpy as np
import matplotlib.pyplot as plt


def birim_donustur(hiz_kmh):
    """Hızı km/h biriminden m/s birimine dönüştürür."""
    return hiz_kmh / 3.6


def reaksiyon_mesafesi_hesapla(v_ms, t_reaksiyon=0.5):
    """Otonom sistemin karar sürecindeki doğrusal yolu hesaplar (d = v*t)."""
    return v_ms * t_reaksiyon


def fren_mesafesi_hesapla(v_ms, k=0.072835):
    """Fiziksel frenleme anındaki karesel yolu hesaplar (d = k*v^2)."""
    return k * (v_ms ** 2)


def anlik_degisim_hizi_hesapla(v_ms, t_reaksiyon=0.5, k=0.072835):
    """Toplam durma mesafesinin hıza göre türevini hesaplar: D'(v) = t_r + 2kv."""
    return t_reaksiyon + (2 * k * v_ms)


def otonom_surus_simulasyonu(hiz_listesi):
    """
    Belirlenmiş hızlar için analiz yapar ve sonuçları tablo/grafik olarak sunar.
    Hata payı olarak sisteme %10 emniyet marjı eklenmiştir.
    """
    k_sabiti = 0.072835
    t_r = 0.5
    hata_payi = 0.10  # %10 hata payı/emniyet marjı

    print(f"{'Hız (km/h)':<12} | {'Toplam Mesafe (m)':<18} | {'Emniyetli Mesafe (m)':<22} | {'Türev (Hassasiyet)':<18}")
    print("-" * 80)

    for hiz in hiz_listesi:
        v = birim_donustur(hiz)
        d_r = reaksiyon_mesafesi_hesapla(v, t_r)
        d_f = fren_mesafesi_hesapla(v, k_sabiti)
        d_toplam = d_r + d_f
        d_emniyet = d_toplam * (1 + hata_payi)
        turev = anlik_degisim_hizi_hesapla(v, t_r, k_sabiti)

        print(f"{hiz:<12} | {d_toplam:<18.2f} | {d_emniyet:<22.2f} | {turev:<18.2f}")


def grafik_ciz(hiz_ust_limit=130):
    """Hız ve mesafe arasındaki ilişkiyi türevsel olarak görselleştirir."""
    hizlar_kmh = np.linspace(0, hiz_ust_limit, 100)
    v_ms = birim_donustur(hizlar_kmh)

    # Hesaplamalar
    d_reaksiyon = reaksiyon_mesafesi_hesapla(v_ms)
    d_fren = fren_mesafesi_hesapla(v_ms)
    d_toplam = d_reaksiyon + d_fren

    plt.figure(figsize=(12, 7))

    # Alanları boyayarak görselleştirme
    plt.fill_between(hizlar_kmh, 0, d_reaksiyon, color='skyblue', alpha=0.4, label='Reaksiyon Bölgesi (Doğrusal)')
    plt.fill_between(hizlar_kmh, d_reaksiyon, d_toplam, color='salmon', alpha=0.4, label='Frenleme Bölgesi (Karesel)')

    # Çizgiler
    plt.plot(hizlar_kmh, d_toplam, color='red', linewidth=2, label='Toplam Durma Mesafesi D(v)')

    # Grafik Detayları
    plt.title('Otonom Araçlarda Hız-Mesafe ve Türevsel Değişim Analizi', fontsize=14)
    plt.xlabel('Araç Hızı (km/h)', fontsize=12)
    plt.ylabel('Durma Mesafesi (metre)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Örnek bir kritik hızın işaretlenmesi (Örn: 100 km/h)
    kritik_hiz = 100
    v_kritik = birim_donustur(kritik_hiz)
    d_kritik = reaksiyon_mesafesi_hesapla(v_kritik) + fren_mesafesi_hesapla(v_kritik)
    plt.scatter([kritik_hiz], [d_kritik], color='black', zorder=5)
    plt.text(kritik_hiz + 2, d_kritik, f'{kritik_hiz} km/h -> {d_kritik:.1f}m', fontweight='bold')

    plt.show()


# --- PROGRAMI ÇALIŞTIR ---
test_hizlari = [30, 50, 70, 90, 110, 130]
otonom_surus_simulasyonu(test_hizlari)
grafik_ciz(140)