# Adım 1: Temel Fonksiyonlar
def topla(x, y):
    """İki sayıyı toplar ve sonucu döndürür."""
    return x + y

def main():
    """Uygulamanın ana giriş noktası."""
    a = 5
    b = 4
    sonuc = topla(a, b)
    print(f"Sonuç: {sonuc}")

# Betik doğrudan çalıştırıldığında main fonksiyonunu çağır
if __name__ == "__main__":
    main()d