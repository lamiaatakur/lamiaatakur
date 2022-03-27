# Dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı fonksiyon yazınız.Kullanıcıdan aldığınız değere göre alanı ve çevreyi ekrana yazdırınız.
def cevre(kisa,uzun):
    return (kisa+uzun)*2
def alan(kisa,uzun):
    return kisa*uzun
kisa_kenar=int(input("Kısa kenarı giriniz:"))
uzun_kenar=int(input("Uzun kenarı giriniz:"))
print("Dikdörtgenin çevresi:",cevre(kisa_kenar,uzun_kenar))
print("Dikdörtgenin alanı:",alan(kisa_kenar,uzun_kenar))

8