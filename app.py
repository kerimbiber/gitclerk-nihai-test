class Hesaplayici:
    """
    Bu sınıf, çeşitli hesaplama ve selamlama işlemleri yapar.
    """
    def __init__(self):
        pass

    def selamla(self, isim):
        # Selamlama mesajı artık büyük harfle döndürülüyor
        return f"MERHABA, {isim}!"

    def topla(self, a, c):
        return a + c

# Sınıftan bir nesne oluşturuyoruz
hesap_makinesi = Hesaplayici()

# Metotları nesne üzerinden çağırıyoruz
mesaj = hesap_makinesi.selamla("Yapay Zeka")
print(mesaj)

sonuc = hesap_makinesi.topla(5, 10)
print(f"5 + 10 = {sonuc}")