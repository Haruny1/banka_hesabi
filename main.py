from banka_hesabi import BankaHesabi

def main():
    hesap = BankaHesabi(
        input("Hesap Sahibi: "),
        float(input("Başlangıç Bakiyesi: "))
    )

    with open("hesap_bilgileri.txt", "w", encoding="utf-8") as file:
        file.write(hesap.hesap_ozeti() + "\n")

    while True:
        secim = input("\n1- Para Yatır\n2- Para Çek\n3- Bakiye Göster\n4- Hesap Özeti\n5- İşlem Geçmişi\n6- Çıkış\nSeçim: ")

        if secim == "1":
            miktar = float(input("Yatırılacak miktar: "))
            hesap.para_yatir(miktar)
            with open("islemler.txt", "a", encoding="utf-8") as file:
                file.write(f"YATIR | {miktar} TL | {hesap.hesap_ozeti()}\n")
            print("Yeni Bakiye:", hesap.get_bakiye())

        elif secim == "2":
            miktar = float(input("Çekilecek miktar: "))
            hesap.para_cek(miktar)
            with open("islemler.txt", "a", encoding="utf-8") as file:
                file.write(f"CEK | {miktar} TL | {hesap.hesap_ozeti()}\n")
            print("Yeni Bakiye:", hesap.get_bakiye())

        elif secim == "3":
            print("Bakiye:", hesap.get_bakiye())

        elif secim == "4":
            print(hesap.hesap_ozeti())

        elif secim == "5":
            try:
                with open("islemler.txt", "r", encoding="utf-8") as file:
                    print("\n--- İŞLEM GEÇMİŞİ ---")
                    print(file.read())
            except FileNotFoundError:
                print("Henüz işlem geçmişi yok.")

        elif secim == "6":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Hatalı seçim!")

if __name__ == "__main__":
    main()
