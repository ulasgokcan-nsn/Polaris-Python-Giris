sayi = int(input("İSTEDİĞİNİZ POZİTİF SAYIYI GİRİNİZ:"))

if sayi <= 0:
    print("LÜTFEN POZİTİF BİR SAYI GİRİNİZ!")

else:
    bolum = 1
    sayim = 1
    indikator = sayi / bolum
    while indikator >= 10:
        bolum = bolum * 10
        indikator = sayi / bolum
        sayim = sayim + 1
    
    print(sayim)

    