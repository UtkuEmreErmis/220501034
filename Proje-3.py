import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
from Proje2 import *
import subprocess
import os
import time

def ana_menu():
    for widget in root.winfo_children():
        widget.destroy()

    ana_baslik = tk.Label(root, text="Ana Menü", font=("Arial", 24))
    ana_baslik.pack(pady=20)

    btn_program_secimi = tk.Button(root, text="Program Seçimi", font=("Arial", 16), command=program_secimi)
    btn_program_secimi.pack(pady=10)

    btn_cikis = tk.Button(root, text="Çıkış", font=("Arial", 16), command=root.quit)
    btn_cikis.pack(pady=10)

def program_secimi():
    for widget in root.winfo_children():
        widget.destroy()

    program_baslik = tk.Label(root, text="Program Seçimi", font=("Arial", 24))
    program_baslik.pack(pady=20)

    try:
        btn_bm = tk.Button(root, text="Bilgisayar Mühendisliği Bölümü", font=("Arial", 16), command=lambda: bolum_secimi("Bilgisayar Mühendisliği"))
        btn_bm.pack(pady=10)
        
        btn_bm = tk.Button(root, text="Yazılım Mühendisliği Bölümü", font=("Arial", 16), command=lambda: bolum_secimi("Yazılım Mühendisliği"))
        btn_bm.config(state="disabled")  
        btn_bm.pack(pady=10)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=ana_menu)
    btn_geri.pack(pady=10)

def bolum_secimi(bolum):
    for widget in root.winfo_children():
        widget.destroy()

    bolum_baslik = tk.Label(root, text=f"{bolum}", font=("Arial", 24))
    bolum_baslik.pack(pady=20)

    btn_ders_secimi = tk.Button(root, text="Ders Seçimi", font=("Arial", 16), command=ders_secimi)
    btn_ders_secimi.pack(pady=10)

    btn_program_ciktisi = tk.Button(root, text="Program Çıktısı", font=("Arial", 16), command=program_ciktisi)
    btn_program_ciktisi.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=program_secimi)
    btn_geri.pack(pady=10)

def ders_secimi():
    for widget in root.winfo_children():
        widget.destroy()

    ders_baslik = tk.Label(root, text="Ders Seçimi", font=("Arial", 24))
    ders_baslik.pack(pady=20)

    dersler_bilgisayar = ["BLM 313 - Yazılım Mühendisliği", "BLM 315 - Yapay Zeka", "BLM 317 - Bilgisayar Ağları"]

    for ders in dersler_bilgisayar:
        btn_ders = tk.Button(root, text=ders, font=("Arial", 16), command=lambda d=ders: ders_detay(d))
        btn_ders.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=lambda: bolum_secimi("Bilgisayar Mühendisliği"))
    btn_geri.pack(pady=10)

def ders_detay(ders):
    for widget in root.winfo_children():
        widget.destroy()

    ders_baslik = tk.Label(root, text=f"{ders} Detayları", font=("Arial", 24))
    ders_baslik.pack(pady=20)

    btn_notlar = tk.Button(root, text="Notlar", font=("Arial", 16), command=lambda: notlar_goster(ders))
    btn_notlar.pack(pady=10)

    btn_degerlendirme = tk.Button(root, text="Değerlendirmeler", font=("Arial", 16), command=lambda: degerlendirmeler_goster(ders))
    btn_degerlendirme.pack(pady=10)

    btn_agirlikli_notlar = tk.Button(root, text="Ağırlıklı Öğrenci Notları", font=("Arial", 16), command=lambda: agirlikli_notlar_goster(ders))
    btn_agirlikli_notlar.pack(pady=10)

    btn_agirlikli_ilişki = tk.Button(root, text="Program Çıktısı ve Ağırlıklı Öğrenci Notları İlişkisi", font=("Arial", 16), command=lambda: agirlikli_ilişki_goster(ders))
    btn_agirlikli_ilişki.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=ders_secimi)
    btn_geri.pack(pady=10)



def degerlendirmeler_goster(ders):
    for widget in root.winfo_children():
        widget.destroy()

    degerlendirme_baslik = tk.Label(root, text=f"{ders} Değerlendirmeleri", font=("Arial", 24))
    degerlendirme_baslik.pack(pady=20)

    

    btn_goruntule = tk.Button(root, text="Değerlendirmeyi Görüntüle ve Düzenle", font=("Arial", 16), command=lambda: degerlendirme_goruntule_ve_duzenle(ders))
    btn_goruntule.pack(pady=10)


    btn_olustur = tk.Button(root, text="Değerlendirme Ekle", font=("Arial", 16), command=lambda: degerlendirme_ekle(ders))
    btn_olustur.pack(pady=10)

    btn_sil = tk.Button(root, text="Değerlendirmeyi Sil", font=("Arial", 16), command=lambda: degerlendirme_sil(ders))
    btn_sil.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=lambda: ders_detay(ders))
    btn_geri.pack(pady=10)

def agirlikli_notlar_goster(ders):
    for widget in root.winfo_children():
        widget.destroy()

    agirlikli_notlar_baslik = tk.Label(root, text=f"{ders} Ağırlıklı Öğrenci Notları", font=("Arial", 24))
    agirlikli_notlar_baslik.pack(pady=20)

    

    btn_goruntule = tk.Button(root, text="Ağırlıklı Notları Görüntüle", font=("Arial", 16), command=lambda: agirlikli_notlar_goruntule(ders))
    btn_goruntule.pack(pady=10)


    btn_sil = tk.Button(root, text="Ağırlıklı Notları Sil", font=("Arial", 16), command=lambda: agirlikli_notlar_sil(ders))
    btn_sil.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=lambda: ders_detay(ders))
    btn_geri.pack(pady=10)


def agirlikli_ilişki_goster(ders):
    for widget in root.winfo_children():
        widget.destroy()

    agirlikli_ilişki_baslik = tk.Label(root, text=f"{ders} Program Çıktısı ve Ağırlıklı Öğrenci Notları İlişkisi", font=("Arial", 24))
    agirlikli_ilişki_baslik.pack(pady=20)

    btn_goruntule = tk.Button(root, text="İlişkileri Görüntüle", font=("Arial", 16), command=lambda: agirlikli_iliski_goruntule(ders))
    btn_goruntule.pack(pady=10)


    btn_sil = tk.Button(root, text="İlişkiyi Sil", font=("Arial", 16), command=lambda: agirlikli_iliski_sil(ders))
    btn_sil.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=lambda: ders_detay(ders))
    btn_geri.pack(pady=10)

def notlar_goster(ders):
    
    for widget in root.winfo_children():
        widget.destroy()

    notlar_baslik = tk.Label(root, text=f"{ders} Notlar", font=("Arial", 24))
    notlar_baslik.pack(pady=20)

    btn_goruntule = tk.Button(root, text="Notlar Görüntüle ve Düzenle", font=("Arial", 16), command=lambda: notlari_goruntule_ve_duzenle(ders))
    btn_goruntule.pack(pady=10)

    btn_olustur = tk.Button(root, text="Notları Ekle", font=("Arial", 16), command=lambda: notlari_ekle(ders))
    btn_goruntule.pack(pady=10)
    btn_olustur.pack(pady=10)

    btn_sil = tk.Button(root, text="Notları Sil", font=("Arial", 16), command=lambda: notlari_sil(ders))
    btn_sil.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=lambda: ders_detay(ders))
    btn_geri.pack(pady=10)
def notlari_goruntule_ve_duzenle(ders):
     
    
    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_notlar = filedialog.askopenfilename(filetypes=[("DersANotlar", "*.xlsx")])

        expected_file_name = "DersANotlar.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_notlar = filedialog.askopenfilename(filetypes=[("DersBNotlar", "*.xlsx")])

        expected_file_name = "DersBNotlar.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_notlar = filedialog.askopenfilename(filetypes=[("DersCNotlar", "*.xlsx")])

        expected_file_name = "DersCNotlar.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")

    try:
        if file_path_notlar:
            if os.path.basename(file_path_notlar) == expected_file_name:
               
                if os.name == 'nt':
                    os.startfile(file_path_notlar)
                else:
                    os.system(f"open {file_path_notlar}")

                
                messagebox.showinfo("Bilgi", "Dosya açıldı. Lütfen kapattıktan sonra işlem başlayacaktır.")

               
                while True:
                    try:
                        
                        with open(file_path_notlar, 'r'):
                            break
                    except IOError:
                        
                        time.sleep(1)

                
                file_path_notlar_1 = file_path_notlar
                df = pd.read_excel(file_path_notlar_1)

                
                df_sliced = df.iloc[:, 1:]
                data_list = df_sliced.values.tolist()  
                print(data_list)
                for i in data_list:
                    for j in i:
                        if j < 0 or j > 100:
                            messagebox.showerror("Hata", f"Lütfen değerleri 0 ile 100 arasında seçiniz. Hatalı değer: {j}")

                
                messagebox.showinfo("Bilgi", "Dosya başarıyla işlendi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")
        else:
            messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")



def notlari_ekle(ders):
    

    if ders =="BLM 313 - Yazılım Mühendisliği":

        expected_file_name = "DersANotlar.xlsx"

    elif ders =="BLM 315 - Yapay Zeka":
        

        expected_file_name = "DersBNotlar.xlsx"

    elif ders =="BLM 317 - Bilgisayar Ağları":
        

        expected_file_name = "DersCNotlar.xlsx"

    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")

    

    try:
        
        if os.path.exists(expected_file_name):
            os.remove(expected_file_name)
            messagebox.showinfo("Bilgi", f"'{expected_file_name}' dosyası başarıyla silindi.")

       
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

        if file_path:
           
            df = pd.read_excel(file_path)

            df_sliced = df.iloc[:, 1:]
            data_list = df_sliced.values.tolist()
            print(data_list)
            if not ((df_sliced >= 0) & (df_sliced <= 100)).all().all():
                messagebox.showerror("Hata", "Tüm değerler 0 ile 100 arasında olmalıdır.")
                return

            
            with pd.ExcelWriter(expected_file_name) as writer:
                df.to_excel(writer, sheet_name="Sayfa1", index=False)

            messagebox.showinfo("Başarılı", f"'{expected_file_name}' dosyası başarıyla oluşturuldu.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def notlari_sil(ders):

    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_notlar_2 = "DersANotlar.xlsx"

        file_path = file_path_notlar_2
    
        expected_file_name = "DersANotlar.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_notlar_2 = "DersBNotlar.xlsx"

        file_path = file_path_notlar_2
    
        expected_file_name = "DersBNotlar.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_notlar_2 = "DersCNotlar.xlsx"

        file_path = file_path_notlar_2
    
        expected_file_name = "DersCNotlar.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")
    

    try:
        if file_path:
            if os.path.basename(file_path) == expected_file_name:
                os.remove(file_path)
                messagebox.showinfo("Başarılı", f"'{expected_file_name}' başarıyla silindi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' değil. Seçilen dosya silinmedi.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


def degerlendirme_goruntule_ve_duzenle(ders):


    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_degerlendirme = filedialog.askopenfilename(filetypes=[("ders_ciktisi_tablosu", "*.xlsx")])

        expected_file_name = "ders_ciktisi_tablosu.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_degerlendirme = filedialog.askopenfilename(filetypes=[("ders_ciktisi_tablosu1", "*.xlsx")])

        expected_file_name = "ders_ciktisi_tablosu1.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_degerlendirme = filedialog.askopenfilename(filetypes=[("ders_ciktisi_tablosu2", "*.xlsx")])

        expected_file_name = "ders_ciktisi_tablosu2.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")
    

    try:
        if file_path_degerlendirme:
            if os.path.basename(file_path_degerlendirme) == expected_file_name:
                
                if os.name == 'nt':
                    os.startfile(file_path_degerlendirme)
                else:
                    os.system(f"open {file_path_degerlendirme}")

                
                messagebox.showinfo("Bilgi", "Dosya açıldı. Lütfen kapattıktan sonra işlem başlayacaktır.")

               
                while True:
                    try:
                        
                        with open(file_path_degerlendirme, 'r'):
                            break
                    except IOError:
                        
                        time.sleep(1)

                
                file_path_deg_1 = file_path_degerlendirme
                df = pd.read_excel(file_path_deg_1)
                df_sliced = df.iloc[:-1, 1:-1]  
                data_list = df_sliced.values.tolist()  
                print(data_list)
                for i in data_list:
                    for j in i:
                        if j < 0 or j > 1:
                            messagebox.showerror("Hata", f"Lütfen değerleri 0 ile 1 arasında seçiniz. Hatalı değer: {j}")
                last_row = df.iloc[-1, 1:-1].values

                last_row_sum = last_row.sum()
                print(last_row_sum)
               
                if last_row_sum != 100:
                    messagebox.showerror("Hata", f"Son satırdaki değerlerin toplamı 100 olmalıdır! Bulunan toplam: {last_row_sum}")
                    return

                
                messagebox.showinfo("Bilgi", "Dosya başarıyla işlendi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")
        else:
            messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")



def degerlendirme_ekle(ders):

    if ders =="BLM 313 - Yazılım Mühendisliği":

        expected_file_name = "ders_ciktisi_tablosu.xlsx"

    elif ders =="BLM 315 - Yapay Zeka":
        

        expected_file_name = "ders_ciktisi_tablosu1.xlsx"

    elif ders =="BLM 317 - Bilgisayar Ağları":
        

        expected_file_name = "ders_ciktisi_tablosu2.xlsx"

    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")

    

    try:
        
        if os.path.exists(expected_file_name):
            os.remove(expected_file_name)
            messagebox.showinfo("Bilgi", f"'{expected_file_name}' dosyası başarıyla silindi.")

        
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

        if file_path:
            
            df = pd.read_excel(file_path)

            df_sliced = df.iloc[0:-1, 1:-1]
            print(df_sliced)
            data_list = df_sliced.values.tolist()  
            print(data_list)
            if not ((df_sliced >= 0) & (df_sliced <= 1)).all().all():
                messagebox.showerror("Hata", "Tüm değerler 0 ile 1 arasında olmalıdır.")
                return
            last_row = df.iloc[-1, 1:-1].values

                
            last_row_sum = last_row.sum()

               
            if last_row_sum != 100:
                    messagebox.showerror("Hata", f"Son satırdaki değerlerin toplamı 100 olmalıdır! Bulunan toplam: {last_row_sum}")
                    return

            
            with pd.ExcelWriter(expected_file_name) as writer:
                df.to_excel(writer, sheet_name="ders_ciktisi_tablosu", index=False)
            messagebox.showinfo("Başarılı", f"'{expected_file_name}' dosyası başarıyla oluşturuldu.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def degerlendirme_sil(ders):

    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_deg_2 = "ders_ciktisi_tablosu.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "ders_ciktisi_tablosu.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_deg_2 = "ders_ciktisi_tablosu1.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "ders_ciktisi_tablosu1.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_deg_2 = "ders_ciktisi_tablosu2.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "ders_ciktisi_tablosu2.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")
    
    

    try:
        if file_path:
            if os.path.basename(file_path) == expected_file_name:
                os.remove(file_path)
                messagebox.showinfo("Başarılı", f"'{expected_file_name}' başarıyla silindi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' değil. Seçilen dosya silinmedi.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def agirlikli_notlar_goruntule(ders):


    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_name_ders_ciktisi = "ders_ciktisi_tablosu.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_name_ders_ciktisi = "ders_ciktisi_tablosu1.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_name_ders_ciktisi = "ders_ciktisi_tablosu2.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")

    


    if os.path.exists(file_name_ders_ciktisi):
        df_degerlendirme = pd.read_excel(file_name_ders_ciktisi, sheet_name="ders_ciktisi_tablosu", index_col="Ders Çıktısı")
        print(f"{file_name_ders_ciktisi} dosyasından veri okundu.")
    else:
        print(f"{file_name_ders_ciktisi} bulunamadı. Lütfen dosyayı oluşturun.")
        exit()


    agirliklar = df_degerlendirme.loc["Ağırlıklar"].values
    degerlendirme_sutunlari = df_degerlendirme.columns[:-1] 


    df_agirlikli_degerlendirme = pd.DataFrame(index=df_degerlendirme.index[:-1], columns=degerlendirme_sutunlari)  


    for col in degerlendirme_sutunlari:
        for row in df_degerlendirme.index[:-1]: 
            
            new_value = (df_degerlendirme.loc[row, col] * agirliklar[degerlendirme_sutunlari.tolist().index(col)]) / 100
            df_agirlikli_degerlendirme.loc[row, col] = round(new_value, 2)  


    df_agirlikli_degerlendirme["Toplam"] = df_agirlikli_degerlendirme.sum(axis=1)


    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_name_agirlikli = "agirlikli_degerlendirme.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_name_agirlikli = "agirlikli_degerlendirme1.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_name_agirlikli = "agirlikli_degerlendirme2.xlsx"
    
    if os.path.exists(file_name_agirlikli):
        os.remove(file_name_agirlikli)
    
    with pd.ExcelWriter(file_name_agirlikli) as writer:
        df_agirlikli_degerlendirme.to_excel(writer, sheet_name="Ağırlıklı Değerlendirme", index_label="Ders Çıktısı")
        print(f"{file_name_agirlikli} başarıyla oluşturuldu.")
    
    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_name_dersnotlar = "DersANotlar.xlsx"
        file_name_agirlikli = "agirlikli_degerlendirme.xlsx"
        new_file_name = "agirlikli_ogrenci_notlari.xlsx" 

    elif ders =="BLM 315 - Yapay Zeka":
        file_name_dersnotlar = "DersBNotlar.xlsx"
        file_name_agirlikli = "agirlikli_degerlendirme1.xlsx"
        new_file_name = "agirlikli_ogrenci_notlari1.xlsx" 

    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_name_dersnotlar = "DersCNotlar.xlsx"
        file_name_agirlikli = "agirlikli_degerlendirme2.xlsx"
        new_file_name = "agirlikli_ogrenci_notlari2.xlsx" 

    if os.path.exists(file_name_dersnotlar):
        df_dersanotlar = pd.read_excel(file_name_dersnotlar, sheet_name="Sayfa1", index_col="Ogrenci_No")
        print(f"{file_name_dersnotlar} dosyasından veri okundu.")
    else:
        print(f"{file_name_dersnotlar} bulunamadı. Lütfen dosyayı oluşturun.") 

    if os.path.exists(file_name_agirlikli):
        df_agirlikli = pd.read_excel(file_name_agirlikli, sheet_name="Ağırlıklı Değerlendirme", index_col="Ders Çıktısı")
        print(f"{file_name_agirlikli} dosyasından veri okundu.")
    else:
        print(f"{file_name_agirlikli} bulunamadı. Lütfen dosyayı oluşturun.")
        exit()


    with pd.ExcelWriter(new_file_name, engine='openpyxl') as writer: 
        
        start_row = 1

        for student in df_dersanotlar.index:
            student_data = df_dersanotlar.loc[student]

            student_table = pd.DataFrame(columns=df_agirlikli.columns, index=df_agirlikli.index)

            for column in df_agirlikli.columns:
                if column != "Toplam":  
                    for row in df_agirlikli.index:
                        student_table.loc[row, column] = round(student_data[column] * df_agirlikli.loc[row, column], 2)


        
            student_table["Toplam"] = student_table.sum(axis=1)

            student_table["Max"] = student_table.apply(lambda row: sum([100 * df_agirlikli.loc[row.name, col] for col in df_agirlikli.columns[:-1]]), axis=1)

            student_table["Başarı Oranı"] = (student_table["Toplam"] / student_table["Max"]) * 100

            
            student_table.to_excel(writer, sheet_name="Tüm Öğrenciler", startcol=0, startrow=start_row, index_label=f"Öğrenci {student}")
            
            
            start_row += len(student_table) + 3  

            
        if os.name == 'nt':
                    os.startfile(new_file_name)
        print(f"Tüm öğrencilerin tabloları tek bir sayfada başarıyla oluşturuldu.")


def agirlikli_notlar_sil(ders):
    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_deg_2 = "agirlikli_ogrenci_notlari.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ogrenci_notlari.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_deg_2 = "agirlikli_ogrenci_notlari1.xlsx" 
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ogrenci_notlari1.xlsx" 
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_deg_2 = "agirlikli_ogrenci_notlari2.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ogrenci_notlari2.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")
    
    

    try:
        if file_path:
            if os.path.basename(file_path) == expected_file_name:
                os.remove(file_path)
                messagebox.showinfo("Başarılı", f"'{expected_file_name}' başarıyla silindi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' değil. Seçilen dosya silinmedi.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def agirlikli_iliski_goruntule(ders):

    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_name_agirlikli_notlar = "agirlikli_ogrenci_notlari.xlsx"
        file_name_ders_program_ciktisi = "ders_program_cikti_iliskisi.xlsx"
        new_file_name_2 = "agirlikli_ders_program_ciktisi_notlari.xlsx"

    elif ders =="BLM 315 - Yapay Zeka":
        file_name_agirlikli_notlar = "agirlikli_ogrenci_notlari1.xlsx"
        file_name_ders_program_ciktisi = "ders_program_cikti_iliskisi.xlsx"
        new_file_name_2 = "agirlikli_ders_program_ciktisi_notlari1.xlsx"
        

    elif ders =="BLM 317 - Bilgisayar Ağları":

        file_name_agirlikli_notlar = "agirlikli_ogrenci_notlari2.xlsx"
        file_name_ders_program_ciktisi = "ders_program_cikti_iliskisi.xlsx"
        new_file_name_2 = "agirlikli_ders_program_ciktisi_notlari2.xlsx"


    if os.path.exists(file_name_ders_program_ciktisi):
        df_dersanotlar = pd.read_excel(file_name_ders_program_ciktisi, sheet_name="Tablo 1", index_col="Prg Çıktı")
        print(f"{file_name_ders_program_ciktisi} dosyasından veri okundu.")

        df_dersanotlar_sliced = df_dersanotlar.iloc[:, 0:-1]

        column_lists = [df_dersanotlar_sliced[col].tolist() for col in df_dersanotlar_sliced.columns]

        df_dersanotlar_sliced = df_dersanotlar.iloc[:, 0:]

        column_lists1 = [df_dersanotlar_sliced[col].tolist() for col in df_dersanotlar_sliced.columns]

        
    else:
        print(f"{file_name_ders_program_ciktisi} bulunamadı. Lütfen dosyayı oluşturun.")

    if os.path.exists(file_name_agirlikli_notlar):

        df = pd.read_excel(file_name_agirlikli_notlar, sheet_name="Tüm Öğrenciler")

        student_tables = []
        student_numbers = []

        basarim_orani_listesi = []

        start_row = 0  #
        while start_row < len(df):

            if isinstance(df.iloc[start_row, 0], str) and df.iloc[start_row, 0].startswith("Öğrenci"):

                student_number = df.iloc[start_row, 0]
                student_numbers.append(student_number)

                student_table = df.iloc[start_row + 1:start_row + 6]
                student_tables.append(student_table)

                basarim_orani = student_table.iloc[:, 9].tolist()
                basarim_orani_listesi.append(basarim_orani)

                start_row += len(student_table) + 3
            else:
                start_row += 1

        
        result_lists = []
        for first_item in basarim_orani_listesi:

            result = []
            for second_item in column_lists:
                multiplied_values = [first_value * second_value for first_value, second_value in
                                    zip(first_item, second_item)]
                result.append(multiplied_values)
            result_lists.append(result)
    result_lists1=[]
    for first_item in basarim_orani_listesi:
            result = []
            for i in range(len(first_item)):  
                second_item = column_lists[i]  
                
                multiplied_values = [first_item[i] * value for value in second_item]
                result.append(multiplied_values)
            result_lists1.append(result)
            
            
            

    
    for res in result_lists:
        

        with pd.ExcelWriter(new_file_name_2, engine='openpyxl') as writer:

            df = pd.read_excel("ders_program_cikti_iliskisi.xlsx", sheet_name="Tablo 1")

            start_row = 0
            program_cikti_sayilari = df['Prg Çıktı'].tolist()

            

            for student in student_numbers:
                sheet_name = "Ders Çıktısı"

                student_table = pd.DataFrame({
                    'Prg Çıktı': program_cikti_sayilari,

                })

                student_table.to_excel(writer, sheet_name=sheet_name, startrow=start_row + 2, index=False)

                start_row += len(student_table) + 3


    else:
        print()

    workbook = load_workbook(new_file_name_2)
    worksheet = workbook[sheet_name]

    row = 2



    prg_cikti_col = 1  

    bold_font = Font(bold=True) 
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )  


    row_indices = []

    for row in range(1, worksheet.max_row + 1):  
        if worksheet.cell(row=row, column=prg_cikti_col).value == "Prg Çıktı":
            row_indices.append(row)
            last_column = len(basarim_orani_listesi[0])+2
            for col in range(1, last_column): 
                cell = worksheet.cell(row=row, column=col)
                cell.font = bold_font  
                cell.border = thin_border  

    row_indices2=row_indices

    row_indices1=[row - 1 for row in row_indices]

    iliski_deg_as=column_lists1[-1]

    for idx, row in enumerate(row_indices1):
        
        cell_student = worksheet.cell(row=row, column=1, value=student_numbers[idx])
        cell_student.font = bold_font  
        cell_student.border = thin_border  

        
        cell_output = worksheet.cell(row=row, column=2, value="Ders Çıktısı")
        cell_output.font = bold_font  
        cell_output.border = thin_border  


    for idx, row in enumerate(row_indices):
        if idx < len(basarim_orani_listesi):  
            value_list = basarim_orani_listesi[idx]
            
            
            for col_offset, value in enumerate(value_list):
                worksheet.cell(row=row, column=prg_cikti_col + 1 + col_offset, value=value)
            
        
            last_col = prg_cikti_col  + len(value_list)  
            cell = worksheet.cell(row=row, column=last_col + 1) 
            cell.value = "Başarı Oranı"  
            cell.font = bold_font  
            cell.border = thin_border  

    row_indices = [row + 1 for row in row_indices]
    prg_cikti_col = 2  


    for idx, row in enumerate(row_indices):
        column_length = len(column_lists[0])  
        
    
        for col_offset in range(column_length):
            col = 1 + col_offset  
            
            
            for row_num in range(row, row + column_length):  
                
                if col == 1:  
                    cell = worksheet.cell(row=row_num, column=col)
                    cell.font = bold_font  
                    cell.border = thin_border  


    for idx, row in enumerate(row_indices):
        if idx < len(result_lists1):  
            value_list = result_lists1[idx]  
            col = prg_cikti_col 
            
            
            
            
            start_row = row  
            
            for sublist in value_list: 
                current_row = start_row 
                for value in sublist:  
                    worksheet.cell(row=current_row, column=col, value=value)  
                    current_row += 1  
                col += 1  

    iliski_deger_icin = []

    row_indices2 = [row + 1 for row in row_indices2]
    for idx, row in enumerate(row_indices2):
        row_total = []  
        
        
        for i in range(len(column_lists[0])):
            
            total = 0
            
            for offset in range(0,(len(basarim_orani_listesi[0])+1)): 
                right_cell = worksheet.cell(row=row + i, column=prg_cikti_col + offset)
                
                try:
                    
                    if right_cell.value:
                        total += float(right_cell.value)
                except ValueError:
                    continue  
            
            
            row_total.append(total)
        
        
        iliski_deger_icin.append(row_total)
        
    agirlikli_basarim_orani = []


    for idx, inner_list in enumerate(iliski_deger_icin):
        row_agirlikli = []  
        
        
        for i, value in enumerate(inner_list):
            
            division1 = value / len(basarim_orani_listesi[0]) if len(basarim_orani_listesi[0]) != 0 else 0 
            print(f"division1 (value={value}, len(basarim_orani_listesi[0])={len(basarim_orani_listesi[0])}): {division1}")

            
            division2 = division1 / iliski_deg_as[i] if iliski_deg_as[i] != 0 else 0  
            print(f"division2 (division1={division1}, iliski_deg_as[{i}]={iliski_deg_as[i]}): {division2}")
            
            
            row_agirlikli.append(division2)
        
        
        agirlikli_basarim_orani.append(row_agirlikli)
    

    
    red_bold_font = Font(bold=True, color="FF0000")
    row_indices2 = [row + -1 for row in row_indices2]

    for idx, row in enumerate(row_indices2):
        
        for col in range(1, worksheet.max_column + 1):
            cell = worksheet.cell(row=row, column=col)
            if cell.value == "Başarı Oranı":  
                basarim_orani_col = col  
                break
        else:
            continue  
        
    
        if idx < len(agirlikli_basarim_orani):  
            for i, value in enumerate(agirlikli_basarim_orani[idx]):
                target_cell = worksheet.cell(row=row + 1 + i, column=basarim_orani_col) 
                target_cell.value = value  
                target_cell.font = red_bold_font  
                target_cell.border = thin_border  

    workbook.save(new_file_name_2)
    if os.name == 'nt':
                    os.startfile(new_file_name_2)
    print(f"Tüm öğrencilerin tabloları tek bir sayfada başarıyla oluşturuldu.")

def agirlikli_iliski_sil(ders):
    if ders =="BLM 313 - Yazılım Mühendisliği":
        file_path_deg_2 = "agirlikli_ders_program_ciktisi_notlari.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ders_program_ciktisi_notlari.xlsx"
    elif ders =="BLM 315 - Yapay Zeka":
        file_path_deg_2 = "agirlikli_ders_program_ciktisi_notlari1.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ders_program_ciktisi_notlari1.xlsx"
    elif ders =="BLM 317 - Bilgisayar Ağları":
        file_path_deg_2 = "agirlikli_ders_program_ciktisi_notlari2.xlsx"
        file_path = file_path_deg_2
    
        expected_file_name = "agirlikli_ders_program_ciktisi_notlari2.xlsx"
    else: 
        messagebox.showinfo("Bilgi", "Böyle bir ders bulunamadı. Lütfen yöneticiniz ile iletişime geçiniz.")
    
    

    try:
        if file_path:
            if os.path.basename(file_path) == expected_file_name:
                os.remove(file_path)
                messagebox.showinfo("Başarılı", f"'{expected_file_name}' başarıyla silindi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' değil. Seçilen dosya silinmedi.")
        else:
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def program_ciktisi():
    for widget in root.winfo_children():
        widget.destroy()

    ciktisi_baslik = tk.Label(root, text="Program Çıktıları", font=("Arial", 24))
    ciktisi_baslik.pack(pady=20)

    
    btn_goruntule = tk.Button(root, text="Program Çıktısını Görüntüle ve Düzenle", font=("Arial", 16), command=program_ciktisi_goruntule_ve_duzenle)
    btn_goruntule.pack(pady=10)

    
    btn_olustur = tk.Button(root, text="Program Çıktısı Ekle", font=("Arial", 16), command=program_ciktisi_ekle)
    btn_olustur.pack(pady=10)

    btn_sil = tk.Button(root, text="Program Çıktısını Sil", font=("Arial", 16), command=program_ciktisi_sil)
    btn_sil.pack(pady=10)

    btn_geri = tk.Button(root, text="Geri", font=("Arial", 16), command=program_secimi)
    btn_geri.pack(pady=10)




def program_ciktisi_goruntule_ve_duzenle():



   file_path_ders_program_cikti_iliskisi = filedialog.askopenfilename(filetypes=[("ders_program_cikti_iliskisi", "*.xlsx")])

    
   expected_file_name = "ders_program_cikti_iliskisi.xlsx"

   try:
        if file_path_ders_program_cikti_iliskisi:
            if os.path.basename(file_path_ders_program_cikti_iliskisi) == expected_file_name:
                
                if os.name == 'nt':
                    os.startfile(file_path_ders_program_cikti_iliskisi)
                else:
                    os.system(f"open {file_path_ders_program_cikti_iliskisi}")

                
                messagebox.showinfo("Bilgi", "Dosya açıldı. Lütfen kapattıktan sonra işlem başlayacaktır.")

                
                while True:
                    try:
                        
                        with open(file_path_ders_program_cikti_iliskisi, 'r'):
                            break
                    except IOError:
                        
                        time.sleep(1)

                
                file_path_dpc_1 = file_path_ders_program_cikti_iliskisi
                df = pd.read_excel(file_path_dpc_1)
                df_sliced = df.iloc[:, 1:-1]  
                data_list = df_sliced.values.tolist()  
                print(data_list)
                for i in data_list:
                    for j in i:
                        if j < 0 or j > 1:
                            messagebox.showerror("Hata",f" Lütfen değerleri 0 ile 1 arasında seçiniz. Hatalı değer: {j}")
                            

                
                messagebox.showinfo("Bilgi", "Dosya başarıyla işlendi.")
            else:
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")
        else:
            messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' bulunamadı.")

   except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


def program_ciktisi_ekle():
    
    expected_file_name = "ders_program_cikti_iliskisi.xlsx"

    
    if os.path.exists(expected_file_name):
        try:
            os.remove(expected_file_name)
            messagebox.showinfo("Bilgi", f"{expected_file_name} dosyası başarıyla silindi.")
        except Exception as e:
            messagebox.showerror("Hata", f"{expected_file_name} dosyası silinirken bir hata oluştu: {e}")
            return

    
    file_path = filedialog.askopenfilename(filetypes=[("Excel Dosyası", "*.xlsx")])
    if not file_path:
        messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
        return

    try:
        
        df = pd.read_excel(file_path)
        df_sliced = df.iloc[:, 1:-1]  
        data_list = df_sliced.values.tolist()  

        
        
        for i, row in enumerate(data_list):
            for j, value in enumerate(row):
                if value < 0 or value > 1:
                    messagebox.showerror("Hata", f"Tabloda 0 ile 1 arasında olmayan bir değer bulundu: Satır {i+1}, Sütun {j+1} ({value})")
                    return

        
        with pd.ExcelWriter(expected_file_name) as writer:
            df.to_excel(writer, sheet_name="Tablo 1", index=False)
        messagebox.showinfo("Başarılı", f"Dosya başarıyla kaydedildi: {expected_file_name}")

    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

def program_ciktisi_sil():


    file_path_dpc_2="ders_program_cikti_iliskisi.xlsx"
    file_path = file_path_dpc_2
   
    expected_file_name = "ders_program_cikti_iliskisi.xlsx"
    
    try:
        if file_path:  
            
            if os.path.basename(file_path) == expected_file_name:
                
                os.remove(file_path)
                messagebox.showinfo("Başarılı", f"'{expected_file_name}' başarıyla silindi.")
            else:
                
                messagebox.showerror("Hata", f"Beklenen dosya '{expected_file_name}' değil. Seçilen dosya silinmedi.")
        else:
            
            messagebox.showerror("Hata", "Herhangi bir dosya seçilmedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

root = tk.Tk()
root.title("Ana Menü")
root.geometry("1280x720")

ana_menu()

root.mainloop()