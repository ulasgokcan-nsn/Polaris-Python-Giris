ilksayi = int(input('Lütfen ilk sayıyı giriniz:'))
ikincisayi = int(input('Lütfen ikinci sayıyı giriniz:'))
istenenislem = input('Yapmak istediğiniz işlemin sembolünü giriniz:')
sonucmetni = 'YAPTIĞINIZ İŞLEMİN SONUCU: '
toplama = ilksayi + ikincisayi
cikarma = ilksayi - ikincisayi
carpma = ilksayi * ikincisayi
bolme = ilksayi / ikincisayi

top = str(toplama)
cik = str(cikarma)
carp = str(carpma)
bol = str(bolme)
a = str(sonucmetni)

if istenenislem == '+':
    print(a + top)

if istenenislem == '-':
    print(a + cik)

if istenenislem == '*':
    print(a + carp)

if istenenislem == '/':
    print(a + bol)