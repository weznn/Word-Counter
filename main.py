def kelime_sayacı(metin):
    kelimeler = metin.split()
    return len(kelimeler)

def main():
    metin = input("Lütfen bir metin girin: ")
    sayı = kelime_sayacı(metin)
    print(f"Girilen metinde {sayı} kelime bulunuyor.")

if __name__ == "__main__":
    main()
