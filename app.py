# Adım 3: Hata Yönetimi
import argparse
import sys

def topla(x, y):
    """İki sayıyı toplar ve sonucu döndürür."""
    return x + y

def main():
    """Uygulamanın ana giriş noktası."""
    parser = argparse.ArgumentParser(description="İki sayıyı toplayan basit bir CLI uygulaması.")
    parser.add_argument("sayi1", help="Toplanacak ilk sayı")
    parser.add_argument("sayi2", help="Toplanacak ikinci sayı")

    args = parser.parse_args()

    try:
        sayi1 = int(args.sayi1)
        sayi2 = int(args.sayi2)
        sonuc = topla(sayi1, sayi2)
        print(f"Sonuç: {sonuc}")
    except ValueError:
        print("Hata: Lütfen sadece sayısal değerler girin.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()