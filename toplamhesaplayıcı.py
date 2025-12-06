print("1'DEN İSTEDİĞİNİZ SAYIYA KADAR OLAN SAYILARI TOPLAMA")
sayi = int(input('LÜTFEN SAYIYI GİRİNİZ:'))

toplam = 0

while sayi > 0:
    toplam = toplam + sayi
    sayi = sayi - 1

print("CEVAP: " , toplam)