#Kullanıcı adı ve şifre alınız. Kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme başarıyla giriş yaptınız" yazsın. Yanlış girildikçe "kullanıcı adı veya şifre hatalı" yazıp tekrar kullanıcı adı ve şifre sorsun!
while True:
    kullanici_adi = input("Kullanıcı adı giriniz:")
    sifre = input("Şire giriniz:")
    if kullanici_adi != "admin" and sifre!="123456":
        break
    else:
        print("Kullanıcı adı veya şifre hatalı")
print("Sisteme başarıyla giriş yaptınız")







