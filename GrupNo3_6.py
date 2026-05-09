import numpy as np
import matplotlib.pyplot as plt


class OtonomFrenAnalizSistemi:
    

    def __init__(self):
        # Ödev-6 kriterlerine uygun parametreler
        self.senaryolar = {
            "Kuru Asfalt": {"k": 0.07, "color": "#2ecc71"},  # [cite: 45]
            "Islak Yol": {"k": 0.10, "color": "#f1c40f"},  # [cite: 46]
            "Buzlu Yol": {"k": 0.15, "color": "#e74c3c"}  # [cite: 47]
        }
        self.reaksiyon_sureleri = {"Standart": 1.0, "Gecikmeli": 1.5}  # [cite: 49, 50]
        self.guvenlik_payi = 1.10  # %10 Emniyet marjı [cite: 62, 90]

    def birim_donustur(self, v_kmh):
        """Hızı fiziksel modelleme için km/h -> m/s birimine çevirir."""
        return v_kmh / 3.6

    def hesapla_bilesenler(self, v_kmh, k, tr):
        """
        Matematiksel Model: d(v) = v*tr + k*v^2 [cite: 86, 75]
        """
        v_ms = self.birim_donustur(v_kmh)
        reaksiyon_m = v_ms * tr  # Reaksiyon mesafesi (doğrusal) [cite: 86]
        fren_m = k * (v_ms ** 2)  # Frenleme mesafesi (karesel) [cite: 75]
        toplam_m = (reaksiyon_m + fren_m) * self.guvenlik_payi  #
        return reaksiyon_m, fren_m, toplam_m

    def hesapla_turev(self, v_kmh, k, tr):
        """
        Türevsel Hassasiyet: d'(v) = (tr + 2kv) * güvenlik_payı [cite: 57, 81]
        """
        v_ms = self.birim_donustur(v_kmh)
        # Türev, hızdaki birim artışın mesafeye etkisini gösterir
        return (tr + 2 * k * v_ms) * self.guvenlik_payi

    def simulasyon_calistir(self):
        # 0-140 km/h arası hız dizisi oluşturma [cite: 42]
        hizlar_kmh = np.linspace(20, 140, 100)

        # Grafik Kurulumu
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle("Otonom Araç Fren Mesafesi ve Bileşen Analizi", fontsize=18, fontweight='bold')

        # --- GRAFİK 1: Tüm Senaryolar (Toplam Durma Mesafesi) ---
        ax1 = axes[0, 0]
        tr_std = self.reaksiyon_sureleri["Standart"]
        for isim, veri in self.senaryolar.items():
            _, _, toplam_m = self.hesapla_bilesenler(hizlar_kmh, veri["k"], tr_std)
            ax1.plot(hizlar_kmh, toplam_m, label=f"{isim} (k={veri['k']})", color=veri["color"], lw=2.5)

        ax1.set_title("Farklı Yol Koşullarında Toplam Durma Mesafesi", fontsize=13)
        ax1.set_ylabel("Mesafe (metre)")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # --- GRAFİK 2: Reaksiyon vs Fren Mesafesi (Alan Grafiği) ---
        ax2 = axes[0, 1]
        k_islak = self.senaryolar["Islak Yol"]["k"]
        r_list, f_list, _ = self.hesapla_bilesenler(hizlar_kmh, k_islak, tr_std)

        # 'r' prefixi (raw string) LaTeX hatalarını (\cdot) önler
        ax2.fill_between(hizlar_kmh, 0, r_list, label=r'Reaksiyon Mesafesi ($v \cdot t_r$)', color='#3498db', alpha=0.6)
        ax2.fill_between(hizlar_kmh, r_list, r_list + f_list,
                         label=r'Frenleme Mesafesi ($k \cdot v^2$)', color='#95a5a6', alpha=0.6)

        ax2.set_title("Mesafe Bileşenlerinin Dağılımı (Islak Yol)", fontsize=13)
        ax2.set_ylabel("Mesafe (metre)")
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.2)

        # --- GRAFİK 3: Türevsel Hassasiyet (d'(v)) ---
        ax3 = axes[1, 0]
        for isim, veri in self.senaryolar.items():
            turevler = self.hesapla_turev(hizlar_kmh, veri["k"], tr_std)
            ax3.plot(hizlar_kmh, turevler, label=f"{isim} Hassasiyet", color=veri["color"], linestyle='--')

        ax3.set_title(r"Hassasiyet Analizi: Hız Artışının Mesafeye Etkisi $d'(v)$", fontsize=13)
        ax3.set_xlabel("Hız (km/h)")
        ax3.set_ylabel("Değişim Oranı (m / km/h)")
        ax3.legend()
        ax3.grid(True, alpha=0.3)

        # --- GRAFİK 4: Reaksiyon Süresinin Etkisi ---
        ax4 = axes[1, 1]
        k_kuru = self.senaryolar["Kuru Asfalt"]["k"]
        for t_isim, t_sure in self.reaksiyon_sureleri.items():
            _, _, toplam_m = self.hesapla_bilesenler(hizlar_kmh, k_kuru, t_sure)
            ax4.plot(hizlar_kmh, toplam_m, label=f"{t_isim} Reaksiyon ({t_sure}s)")

        ax4.set_title("Sistem Reaksiyon Süresinin Durma Mesafesine Etkisi", fontsize=13)
        ax4.set_xlabel("Hız (km/h)")
        ax4.legend()
        ax4.grid(True, alpha=0.3)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    def bulgulari_yazdir(self, test_hizlari=[30, 70, 110, 130]):
        """Raporun 'Bulgular' bölümü için sayısal tablo çıktısı verir."""
        print(f"\n{'YOL KOŞULU':<15} | {'HIZ':<6} | {'REAKSIYON':<12} | {'FREN':<12} | {'TOPLAM'}")
        print("-" * 65)
        for isim, veri in self.senaryolar.items():
            for hiz in test_hizlari:
                r, f, t = self.hesapla_bilesenler(hiz, veri["k"], 1.0)
                print(f"{isim:<15} | {hiz:<6} | {r:>10.2f} m | {f:>10.2f} m | {t:>10.2f} m")


if __name__ == "__main__":
    analiz = OtonomFrenAnalizSistemi()
    analiz.bulgulari_yazdir()  # Rapor için sayısal veriler
    analiz.simulasyon_calistir()  # Görsel analizler