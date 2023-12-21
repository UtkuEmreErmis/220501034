import csv
from collections import defaultdict

class TIR:
    def __init__(self, plaka):
        self.plaka = plaka
        self.yukler = []

class Gemi:
    def __init__(self, gemi_numarasi, kapasite, ulke):
        self.gemi_numarasi = gemi_numarasi
        self.kapasite = kapasite
        self.ulke = ulke
        self.yukler = []

def liman_simulasyonu(gemiler, tirlar):
    istif_alani = 750
    vinc_kapasitesi = 20
    liman_takvimi = defaultdict(list)

    for t in range(1, max(max(gemiler.keys()), max(tirlar.keys())) + 1):
        # TIR'ları indir
        if t in tirlar:
            tirlar_tiralar = sorted(tirlar[t], key=lambda tir: tir.plaka)
            for tir in tirlar_tiralar:
                # İstif alanı doluysa bekle
                if istif_alani == 0:
                    print(f"{t}. zaman: İstif alanı dolu, TIR {tir.plaka} bekliyor.")
                    continue

                # İstif alanına yük ekle
                tir_yuk = tir.yukler.pop(0)
                istif_alani -= tir_yuk['yük_miktarı']
                print(f"{t}. zaman: TIR {tir.plaka} indiriliyor - {tir_yuk}")

        # Gemiye yük yükle
        if t in gemiler:
            gemiler_geliyor = sorted(gemiler[t], key=lambda gemi: gemi.gemi_numarasi)
            for gemi in gemiler_geliyor:
                # İstif alanı boşsa bekle
                if istif_alani == 750:
                    print(f"{t}. zaman: İstif alanı boş, Gemi {gemi.gemi_numarasi} bekliyor.")
                    continue

                # Gemiye yük ekle
                gemi_yuk = {'ülke': gemi.ulke, 'kapasite': gemi.kapasite, 'yükler': []}
                toplam_yuk_miktari = 0

                while toplam_yuk_miktari < gemi.kapasite * 0.95 and istif_alani > 0:
                    # Vinç işlemi
                    vinc_yuk_miktari = min(vinc_kapasitesi, istif_alani)
                    istif_alani -= vinc_yuk_miktari

                    # Gemi yük bilgisine ekle
                    gemi_yuk['yükler'].append({'yük_miktarı': vinc_yuk_miktari})

                    # Toplam yük miktarını güncelle
                    toplam_yuk_miktari += vinc_yuk_miktari

                # Gemi yük bilgisini güncelle
                gemi.yukler.append(gemi_yuk)
                print(f"{t}. zaman: Gemi {gemi.gemi_numarasi} yükleniyor - {gemi_yuk}")

    print("Simülasyon tamamlandı.")

def dosyadan_veri_oku(dosya_adi):
    veri = defaultdict(list)
    with open(dosya_adi, newline='', encoding="utf-8") as dosya:
        reader = csv.DictReader(dosya)
        for row in reader:
            zaman = int(row['geliş_zamanı'])
            if 'tır_plakası' in row:
                plaka = row['tır_plakası']
                ulke = row['ülke']
                ton20_adet = int(row['20_ton_adet'])
                ton30_adet = int(row['30_ton_adet'])
                yuk_miktar = int(row['yük_miktarı'])
                maliyet = int(row['maliyet'])
                tir = TIR(plaka)
                tir.yukler.append({'ülke': ulke, 'kapasite': 20, 'yük_miktarı': ton20_adet * 20, 'maliyet': maliyet})
                tir.yukler.append({'ülke': ulke, 'kapasite': 30, 'yük_miktarı': ton30_adet * 30, 'maliyet': maliyet})
                veri[zaman].append(tir)
            elif 'gemi_adı' in row:
                gemi_numarasi = int(row['gemi_adı'])
                kapasite = int(row['kapasite'])
                ulke = row['gidecek_ülke']
                gemi = Gemi(gemi_numarasi, kapasite, ulke)
                veri[zaman].append(gemi)
    return veri

if __name__ == "__main__":
    gemiler = dosyadan_veri_oku("gemiler.csv")
    tirlar = dosyadan_veri_oku("olaylar.csv")
    liman_simulasyonu(gemiler, tirlar)
