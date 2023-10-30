from functools import reduce





def k_kucuk(k, liste):
    if k > 0 and k <= len(liste):
        # Listeyi küçükten büyüğe sırala
        sirali_liste = sorted(liste)
        # İstenen k. elemanı bul ve döndür
        k_kucuk_eleman = sirali_liste[k - 1]
        return k_kucuk_eleman
    else:
        return "Hatalı k değeri"




def en_yakin_cift(hedef_sayi, liste):
    liste.sort()  # Listeyi küçükten büyüğe sırala

    en_yakin_fark = float('inf')  # Sonsuz büyük bir başlangıç farkı
    en_yakin_cift = None

    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(toplam - hedef_sayi)
            if fark < en_yakin_fark:
                en_yakin_fark = fark
                en_yakin_cift = (liste[i], liste[j])

    return en_yakin_cift




def tekrar_eden_elemanlar(liste):
    # List comprehension ile tekrar eden elemanları bul
    tekrar_edenler = [x for x in liste if liste.count(x) > 1]

    # Tekrar eden elemanları bir set'e dönüştürerek her elemanın yalnızca bir kez görünmesini sağla
    tekrar_edenler = list(set(tekrar_edenler))

    return tekrar_edenler





def matris_carpimi(matris1, matris2):
    # İlk matrisin satır sayısı ve sütun sayısı
    m = len(matris1)
    n = len(matris1[0])

    # İkinci matrisin sütun sayısı
    p = len(matris2[0])

    # Sonuç matrisini oluştur
    sonuc = [[0 for _ in range(p)] for _ in range(m)]

    # Matris çarpımını hesapla
    for i in range(m):
        for j in range(p):
            sonuc[i][j] = sum(matris1[i][k] * matris2[k][j] for k in range(n))

    return sonuc




def kelime_frekanslari(dosya_konumu):
    with open(dosya_konumu, 'r') as dosya:
        metin = dosya.read()

    kelimeler = metin.split()

    # Her kelimenin frekansını hesapla
    frekanslar = reduce(lambda acc, kelime: {**acc, kelime: acc.get(kelime, 0) + 1}, kelimeler, {})

    return frekanslar


dosya_konumu = 'giris_metni.txt'
sonuc = kelime_frekanslari(dosya_konumu)



def en_kucuk_deger(liste):
    # Liste boşsa veya tek elemanlıysa o eleman en küçük değerdir
    if len(liste) == 0:
        return None
    elif len(liste) == 1:
        return liste[0]

    # Listenin ilk elemanını en küçük olarak kabul ediyoruz
    en_kucuk = liste[0]

    # Geriye kalan elemanları dolaşıp en küçüğü bulma
    for eleman in liste:
        if eleman < en_kucuk:
            en_kucuk = eleman

    return en_kucuk




def karekok(N, x0, tol=1e-10, maxiter=10, iterasyon=0):
    x_next = 0.5 * (x0 + N / x0)
    hata = abs(x_next * x_next - N)

    if hata < tol or iterasyon >= maxiter:
        if iterasyon >= maxiter:
            print(f"{maxiter} iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin.")
        return x_next

    return karekok(N, x_next, tol, maxiter, iterasyon + 1)



def eb_ortak_bolen(a, b):
    if b == 0:
        return a
    else:
        return eb_ortak_bolen(b, a % b)



def asal_veya_degil(n, i=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return asal_veya_degil(n, i + 1)



print("KONSOL MENÜSÜ\n\n "
      ""
      "Aşağıdaki seçeneklerin sıra numarasını giriniz.\n\n"
      ""
      "1. k’nıncı en küçük elemanı bulma örneğini göster.\n "
      "2. En yakın çifti bulma örneğini göster.\n "
      "3. Bir listenin tekrar eden elemanlarını bulma örneğini göster.\n "
      "4. Matris çarpımı örneğini göster.\n "
      "5. Bir text dosyasındaki kelimelerin frekansını bulma örneğini göster.\n "
      "6. Liste içinde en küçük değeri bulma örneğini göster.\n "
      "7. Karekök fonksiyonu örneğini göster.\n "
      "8. En büyük ortak bölen örneğini göster.\n "
      "9. Asallık testi örneğini göster.\n ")

secenek = int(input(""))

if secenek == 1:
    liste = [7, 10, 4, 3, 20, 15]
    k_degeri = 3
    sonuc = k_kucuk(k_degeri, liste)
    print(f'k_kucuk({k_degeri}, {liste})')
    print(sonuc)

elif secenek == 2:
    liste = [10, 22, 28, 29, 30, 40]
    hedef_sayi = 54
    sonuc = en_yakin_cift(hedef_sayi, liste)
    print(f'en_yakin_cift({hedef_sayi}, {liste})')
    print(sonuc)

elif secenek == 3:
    liste = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
    sonuc = tekrar_eden_elemanlar(liste)
    print(f'tekrar_eden_elemanlar({liste})')
    print(sonuc)

elif secenek == 4:
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    sonuc = matris_carpimi(A, B)
    print(f'matris_carpimi({A}, {B})')
    print(sonuc)

elif secenek == 5:
    for kelime, frekans in sonuc.items():
        print(f"{kelime}={frekans}")

elif secenek == 6:
    liste1 = [1, 4, 6, 91, 2, 5]
    liste2 = [1, 2, 3, -1, 4, -2, 5]

    sonuc1 = en_kucuk_deger(liste1)
    sonuc2 = en_kucuk_deger(liste2)

    print(f'en_kucuk_deger({liste1})')
    print(sonuc1)
    print("")
    print(f'en_kucuk_deger({liste2})')
    print(sonuc2)

elif secenek == 7:
    karekok_1 = karekok(N=10, x0=1)
    print(f'karekok(N=10, x0=1)')
    print(karekok_1)
    print("")

    karekok_2 = karekok(N=10000, x0=0.1)
    print(f'karekok(N=10000, x0=0.1)')
    print(karekok_2)
    print("")

    karekok_3 = karekok(N=10000, x0=0.1, maxiter=15)
    print(f'karekok(N=10000, x0=0.1, maxiter=15)')
    print(karekok_3)

elif secenek == 8:
    sonuc1 = eb_ortak_bolen(18, 64)
    print(f'eb_ortak_bolen(18, 64)')
    print(sonuc1)
    print("")

    sonuc2 = eb_ortak_bolen(32, 64)
    print(f'eb_ortak_bolen(32, 64)')
    print(sonuc2)

elif secenek == 9:
    sonuc1 = asal_veya_degil(35)
    print(f'asal_veya_degil(35)')
    print(sonuc1)
    print("")

    sonuc2 = asal_veya_degil(97)
    print(f'asal_veya_degil(97)')
    print(sonuc2)

else:
    print("Lütfen yukardaki sıra numaralarını giriniz. ")
