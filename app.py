# Adım 2: Argüman Ayrıştırma
import argparse

def topla(x, y):
    """İki sayıyı toplar ve sonucu döndürür."""
    return x + y

def main():
    """Uygulamanın ana giriş noktası."""
    parser = argparse.ArgumentParser(description="İki sayıyı toplayan basit bir CLI uygulaması.")
    parser.add_argument("sayi1", type=int, help="Toplanacak ilk sayı")
    parser.add_argument("sayi2", type=int, help="Toplanacak ikinci sayı")

    args = parser.parse_args()

    sonuc = topla(args.sayi1, args.sayi2)
    print(f"Sonuç: {sonuc}")

if __name__ == "__main__":
    main()