import random
import tkinter as tk
from tkinter import messagebox

class Kart:  # Kalıtım için temel sınıf
    def __init__(self, isim, hasar):
        self.__isim = isim
        self.__hasar = hasar

    def get_isim(self):
        return self.__isim

    def get_hasar(self):
        return self.__hasar

    def set_isim(self, isim):
        self.__isim = isim

    def set_hasar(self, hasar):
        self.__hasar = hasar

    isim = property(get_isim, set_isim)
    hasar = property(get_hasar, set_hasar)

    def __str__(self):
        return f"{self.__isim} (Hasar: {self.__hasar})"

class PokemonKarti(Kart):  # Kart'tan türetilmiş
    def __init__(self, isim, hasar):
        super().__init__(isim, hasar)

class Oyuncu:
    def __init__(self, isim):
        self.__isim = isim
        self.__eldeki_kartlar = []
        self.__puan = 0

    def get_isim(self):
        return self.__isim

    def get_eldeki_kartlar(self):
        return self.__eldeki_kartlar

    def get_puan(self):
        return self.__puan

    def set_isim(self, isim):
        self.__isim = isim

    def set_eldeki_kartlar(self, eldeki_kartlar):
        self.__eldeki_kartlar = eldeki_kartlar

    def set_puan(self, puan):
        self.__puan = puan

    isim = property(get_isim, set_isim)
    eldeki_kartlar = property(get_eldeki_kartlar, set_eldeki_kartlar)
    puan = property(get_puan, set_puan)

    def karta_elde_ekle(self, kart):
        self.__eldeki_kartlar.append(kart)

    def eldeki_karttan_kaldir(self, kart):
        self.__eldeki_kartlar.remove(kart)

    def puan_ekle(self, puan):
        self.__puan += puan

    def __str__(self):
        return f"{self.__isim} (Puan: {self.__puan})"

class Oyun:
    def __init__(self, oyuncu1, oyuncu2, mod='otomatik'):
        self.__desteler = [
            PokemonKarti("Bulbasaur", 45), PokemonKarti("Charmander", 52),
            PokemonKarti("Squirtle", 44), PokemonKarti("Pikachu", 50),
            PokemonKarti("Jigglypuff", 20), PokemonKarti("Meowth", 35),
            PokemonKarti("Psyduck", 25), PokemonKarti("Snorlax", 30),
            PokemonKarti("Dragonite", 70), PokemonKarti("Mewtwo", 60)
        ]
        self.__oyuncu1 = oyuncu1
        self.__oyuncu2 = oyuncu2
        self.__mod = mod

    def get_desteler(self):
        return self.__desteler

    def get_oyuncu1(self):
        return self.__oyuncu1

    def get_oyuncu2(self):
        return self.__oyuncu2

    def set_desteler(self, desteler):
        self.__desteler = desteler

    def set_oyuncu1(self, oyuncu1):
        self.__oyuncu1 = oyuncu1

    def set_oyuncu2(self, oyuncu2):
        self.__oyuncu2 = oyuncu2

    desteler = property(get_desteler, set_desteler)
    oyuncu1 = property(get_oyuncu1, set_oyuncu1)
    oyuncu2 = property(get_oyuncu2, set_oyuncu2)

    def kartlari_dagit(self):
        random.shuffle(self.__desteler)
        self.__oyuncu1.eldeki_kartlar.extend(self.__desteler[:3])
        self.__oyuncu2.eldeki_kartlar.extend(self.__desteler[3:6])
        self.__desteler = self.__desteler[6:]

    def oyuncu_kart_sec(self, secim):
        return self.__oyuncu1.eldeki_kartlar[secim]

    def bilgisayar_kartlarini_goster(self):
        return [str(kart) for kart in self.__oyuncu2.eldeki_kartlar]

    def turu_oyna(self, oyuncu1_kart_index=None):
        if self.__mod == 'manuel':
            oyuncu1_karti = self.__oyuncu1.eldeki_kartlar[oyuncu1_kart_index]
        else:
            oyuncu1_karti = random.choice(self.__oyuncu1.eldeki_kartlar)

        oyuncu2_karti = random.choice(self.__oyuncu2.eldeki_kartlar)

        if oyuncu1_karti.hasar > oyuncu2_karti.hasar:
            self.__oyuncu1.puan_ekle(5)
            sonuc = f"{self.__oyuncu1.isim} turu kazandı!"
        elif oyuncu1_karti.hasar < oyuncu2_karti.hasar:
            self.__oyuncu2.puan_ekle(5)
            sonuc = f"{self.__oyuncu2.isim} turu kazandı!"
        else:
            sonuc = "Berabere!"

        self.__oyuncu1.eldeki_karttan_kaldir(oyuncu1_karti)
        self.__oyuncu2.eldeki_karttan_kaldir(oyuncu2_karti)

        if self.__desteler:
            yeni_kart1 = self.__desteler.pop(0)
            yeni_kart2 = self.__desteler.pop(0)
            self.__oyuncu1.karta_elde_ekle(yeni_kart1)
            self.__oyuncu2.karta_elde_ekle(yeni_kart2)

        return oyuncu1_karti, oyuncu2_karti, sonuc

    def oyun_bitti_mi(self):
        return not (self.__oyuncu1.eldeki_kartlar and self.__oyuncu2.eldeki_kartlar)

    def kazanan(self):
        if self.__oyuncu1.puan > self.__oyuncu2.puan:
            return self.__oyuncu1.isim
        elif self.__oyuncu1.puan < self.__oyuncu2.puan:
            return self.__oyuncu2.isim
        else:
            return "Berabere!"

class OyunUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Kart Oyunu")

        self.oyuncu1 = Oyuncu("Oyuncu 1")
        self.oyuncu2 = Oyuncu("Bilgisayar")
        self.oyun = None

        self.bilgisayar_kartlarini_goster = tk.BooleanVar()
        self.widgetleri_olustur()
        self.ana_menuyu_goster()

    def widgetleri_olustur(self):
        self.ana_menu_cercevesi = tk.Frame(self.root)
        self.manuel_buton = tk.Button(self.ana_menu_cercevesi, text="Manuel Mod", command=self.manuel_oyun_baslat)
        self.manuel_buton.grid(row=0, column=0, padx=10, pady=10)
        self.otomatik_buton = tk.Button(self.ana_menu_cercevesi, text="Otomatik Mod", command=self.otomatik_oyun_baslat)
        self.otomatik_buton.grid(row=0, column=1, padx=10, pady=10)

        self.oyuncu1_cercevesi = tk.LabelFrame(self.root, text="Oyuncu 1")
        self.oyuncu1_etiket = tk.Label(self.oyuncu1_cercevesi)
        self.oyuncu1_etiket.grid(padx=10, pady=10)

        self.bilgisayar_cercevesi = tk.LabelFrame(self.root, text="Bilgisayar")
        self.bilgisayar_etiket = tk.Label(self.bilgisayar_cercevesi)
        self.bilgisayar_etiket.grid(padx=10, pady=10)

        self.kartlar_cercevesi = tk.Frame(self.root)

        self.secim_degiskeni = tk.IntVar()
        self.secim_degiskeni.set(0)
        self.kart_butonlari = [tk.Radiobutton(self.kartlar_cercevesi, variable=self.secim_degiskeni, value=i) for i in range(3)]
        for i, buton in enumerate(self.kart_butonlari):
            buton.grid(row=0, column=i, padx=5)

        self.oyna_butonu = tk.Button(self.root, text="Tur Oyna", command=self.manuel_turu_oyna)

        self.sonuc_degiskeni = tk.StringVar()
        self.sonuc_etiketi = tk.Label(self.root, textvariable=self.sonuc_degiskeni)

        self.bilgisayar_kartlari_goster_butonu = tk.Checkbutton(self.root, text="Bilgisayarın Kartlarını Göster", variable=self.bilgisayar_kartlarini_goster, command=self.el_gorunumunu_guncelle)

        self.oyuncu1_puan_etiketi = tk.Label(self.root, text="Oyuncu 1 Puan: 0")
        self.bilgisayar_puan_etiketi = tk.Label(self.root, text="Bilgisayar Puan: 0")

    def ana_menuyu_goster(self):
        self.ana_menu_cercevesi.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def manuel_oyun_baslat(self):
        self.ana_menu_cercevesi.grid_forget()
        self.oyunu_ayarla('manuel')

    def otomatik_oyun_baslat(self):
        self.ana_menu_cercevesi.grid_forget()
        self.oyunu_ayarla('otomatik')
        self.otomatik_oyunu_oyna()

    def oyunu_ayarla(self, mod):
        self.oyuncu1_cercevesi.grid(row=0, column=0, padx=10, pady=10)
        self.bilgisayar_cercevesi.grid(row=0, column=1, padx=10, pady=10)
        self.kartlar_cercevesi.grid(row=1, column=0, columnspan=2, pady=10)
        self.oyna_butonu.grid(row=2, column=0, columnspan=2, pady=10)
        self.sonuc_etiketi.grid(row=3, column=0, columnspan=2, pady=10)
        self.oyuncu1_puan_etiketi.grid(row=4, column=0, padx=10, pady=10)
        self.bilgisayar_puan_etiketi.grid(row=4, column=1, padx=10, pady=10)

        self.oyun = Oyun(self.oyuncu1, self.oyuncu2, mod)
        self.oyun.kartlari_dagit()
        self.el_gorunumunu_guncelle()

        if mod == 'manuel':
            for i, buton in enumerate(self.kart_butonlari):
                buton.config(text=f"Kart {i + 1}")
            self.oyna_butonu.config(text="Tur Oyna", command=self.manuel_turu_oyna)
            self.kartlar_cercevesi.grid()
            self.oyna_butonu.grid()
            self.bilgisayar_kartlari_goster_butonu.grid(row=5, column=0, columnspan=2, pady=10)
        else:
            self.kartlar_cercevesi.grid_forget()
            self.oyna_butonu.grid_forget()
            self.bilgisayar_kartlari_goster_butonu.grid_forget()

    def otomatik_oyunu_oyna(self):
        self.otomatik_turu_oyna()

    def otomatik_turu_oyna(self):
        if not self.oyun.oyun_bitti_mi():
            oyuncu1_karti, oyuncu2_karti, sonuc = self.oyun.turu_oyna()
            self.sonuc_degiskeni.set(f"Oyuncu 1 {oyuncu1_karti} oynadı, Bilgisayar {oyuncu2_karti} oynadı. {sonuc}")
            self.el_gorunumunu_guncelle()

            self.root.after(1000, self.otomatik_turu_oyna)
        else:
            kazanan = self.oyun.kazanan()
            messagebox.showinfo("Oyun Bitti", f"Oyun bitti! {kazanan} kazandı!")
            self.root.quit()

    def manuel_turu_oyna(self):
        if not self.oyun.oyun_bitti_mi():
            secim = self.secim_degiskeni.get()
            oyuncu1_karti, oyuncu2_karti, sonuc = self.oyun.turu_oyna(oyuncu1_kart_index=secim)
            self.sonuc_degiskeni.set(f"Oyuncu 1 {oyuncu1_karti} oynadı, Bilgisayar {oyuncu2_karti} oynadı. {sonuc}")
            self.el_gorunumunu_guncelle()

            if self.oyun.oyun_bitti_mi():
                kazanan = self.oyun.kazanan()
                messagebox.showinfo("Oyun Bitti", f"Oyun bitti! {kazanan} kazandı!")
                self.root.quit()

    def el_gorunumunu_guncelle(self):
        self.oyuncu1_etiket.config(text="\n".join(str(kart) for kart in self.oyuncu1.eldeki_kartlar))
        if self.bilgisayar_kartlarini_goster.get() or self.oyun._Oyun__mod == 'otomatik':
            self.bilgisayar_etiket.config(text="\n".join(str(kart) for kart in self.oyuncu2.eldeki_kartlar))
        else:
            self.bilgisayar_etiket.config(text="Kartlar Gizli")

        if self.oyun._Oyun__mod == 'manuel':
            for i, buton in enumerate(self.kart_butonlari):
                if i < len(self.oyuncu1.eldeki_kartlar):
                    buton.config(text=str(self.oyuncu1.eldeki_kartlar[i]), state=tk.NORMAL)
                else:
                    buton.config(text="", state=tk.DISABLED)

        self.oyuncu1_puan_etiketi.config(text=f"Oyuncu 1 Puan: {self.oyuncu1.puan}")
        self.bilgisayar_puan_etiketi.config(text=f"Bilgisayar Puan: {self.oyuncu2.puan}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OyunUI(root)
    root.mainloop()
