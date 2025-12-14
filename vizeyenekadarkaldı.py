import datetime

tarih = input(" Sınav tarihini ve saatini gir (örnek: 2025-12-25 09:30): ")

sinav_tarihi = datetime.datetime.strptime(tarih, "%Y-%m-%d %H:%M")

simdi = datetime.datetime.now()

kalan = sinav_tarihi - simdi

gun = kalan.days
saat = kalan.seconds // 3600
dakika = (kalan.seconds % 3600) // 60

a = str(gun)
b = str(saat)
c = str(dakika)

print(a + " gün, " + b + " saat, " + c + " dakika kaldı! Başarılar!")