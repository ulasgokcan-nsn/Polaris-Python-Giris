import random

sayi = random.randint(1, 100)

print("🎯 Sayı Tahmin Oyununa Hoş Geldin!")
print("1 ile 100 arasında bir sayı tuttum, hadi tahmin et:")

tahmin_sayisi = 0

while True:
    tahmin = int(input("Tahminin: "))
    tahmin_sayisi += 1

    if tahmin < sayi:
        print("Daha büyük bir sayı dene!")
    elif tahmin > sayi:
        print("Daha küçük bir sayı dene!")
    else:
        a = str(tahmin_sayisi)
        print("Tebrikler! " + a + " " + "denemede doğru cevaba ulaştın!")
        break