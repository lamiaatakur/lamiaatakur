#Kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek sonucunda True ya da False gönderen fonksiyonun python kodu
#kullanıcıadı: admin, sifre:123456 olmalı
def kontrol (kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return True
    else:
        return False
kullanici=input("Kullanıcı adınız:")
sifre=input("Şifreniz:")
sonuc=kontrol(kullanici,sifre)
if sonuc == True:
    print("Giriş başarılı")
else:
    print("Giriş yapılamadı")
    