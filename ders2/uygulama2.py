#kullanıcıdan harf girilmesini isteyiniz. E girerse erkek, K girerse kadın ekrana yazdırınız.
cinsiyet=input("Bir harf giriniz E/K:")
if cinsiyet=="E" or cinsiyet=="e":
    print("Erkek")
elif cinsiyet=="K" or cinsiyet=="k": #2. veya daha fazla şart olursa elif kullanılır
    print("Kadın")
else:
    print("Lütfen E veya K giriniz!")
print("Hoşçakalın...")
