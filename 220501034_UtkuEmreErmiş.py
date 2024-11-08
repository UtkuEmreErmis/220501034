import time


def menu():
    while True:
        print("\n--- METİN İŞLEME MENÜSÜ ---")
        print("1 - Metinde verilen kelimelerin harflerini alt alta yazdırma")
        print("2 - Metnin tamamen ve kelime kelime tersini bulma")
        print("3 - Tüm 'a' harflerini 'A' ile değiştirme")
        print("4 - Metindeki kelimeleri ayrı ayrı yazdırma")
        print("5 - Metindeki kelimeleri yeniden birleştirme")
        print("6 - Metindeki ünlü harflerin sayısını bulma")
        print("7 - Yazı yazma hızını hesaplama")
        print("0 - Çıkış")

        choice = input("Seçiminizi yapın: ")
        if choice == '0':
            print("Çıkış yapılıyor...")
            break
        elif choice in map(str, range(1, 8)):
            text = input("Metni girin: ")
            if choice == '1':
                list_characters(text)
            elif choice == '2':
                reverse_text(text)
            elif choice == '3':
                replace_a_with_A(text)
            elif choice == '4':
                list_words(text)
            elif choice == '5':
                join_words(text)
            elif choice == '6':
                count_vowels(text)
            elif choice == '7':
                calculate_typing_speed(text)
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


def list_characters(text):
    print("\n--- Harfleri Alt Alta Yazdırma ---")
    for word in text.split():
        for char in word:
            print(char)
        print()  # Her kelime arasında bir satır boşluk bırakmak için


def reverse_text(text):
    print("\n--- Metnin Tersini Alma ---")
    print("Orjinal Metin:", text)
    print("Tamamen Ters:", text[::-1])
    reversed_words = ' '.join(word[::-1] for word in text.split())
    print("Kelime Kelime Ters:", reversed_words)


def replace_a_with_A(text):
    print("\n--- 'a' Harflerini 'A' ile Değiştirme ---")
    replaced_text = text.replace('a', 'A').replace('A', 'A')  # Küçük ve büyük harf için
    print("Yeni Metin:", replaced_text)


def list_words(text):
    print("\n--- Kelimeleri Liste Şeklinde Gösterme ---")
    words = text.split()
    print("Kelimeler Listesi:", words)


def join_words(text):
    print("\n--- Kelimeleri Birleştirme ---")
    words = text.split()
    joined_text = ''.join(words)
    print("Birleştirilmiş Metin:", joined_text)


def count_vowels(text):
    vowels = "aeıioöuüAEIİOÖUÜ"
    count = sum(1 for char in text if char in vowels)
    print("\n--- Ünlü Harf Sayısı ---")
    print("Ünlü harf sayısı:", count)


def calculate_typing_speed(text):
    print("\n--- Yazma Hızı Hesaplama ---")
    input("Başlamak için Enter tuşuna basın...")
    start_time = time.time()
    user_input = input("Metni tekrar yazın: ")
    end_time = time.time()

    time_taken = end_time - start_time
    char_count = len(user_input)
    speed = char_count / time_taken if time_taken > 0 else 0

    print(f"\nYazma süresi: {time_taken:.2f} saniye")
    print(f"Saniye başına yazılan harf sayısı: {speed:.2f}")


# Menü başlatma
menu()
