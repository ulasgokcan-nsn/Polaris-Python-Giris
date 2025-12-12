sayi = input("LÜTFEN BİR SAYI GİRİNİZ:")
try:
    sayi1 = int(sayi)
    print("İşlem Tamamdır!")
except ValueError:
    print("HATA! LÜTFEN SAYI GİRİNİZ!")