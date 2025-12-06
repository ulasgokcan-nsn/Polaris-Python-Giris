sayi = int(input('LÜTFEN BİR SAYI GİRİNİZ:'))

if sayi == 0:
    print('ATEŞLE!')

elif sayi < 0:
    print('LÜTFEN 0 VEYA DAHA BÜYÜK BİR SAYI GİRİNİZ!')

elif sayi > 0:
    while sayi > 0:
        print(sayi)
        sayi = sayi - 1
    print('ATEŞLE!')