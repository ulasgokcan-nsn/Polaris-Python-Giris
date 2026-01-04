import re

def sifre_kontrol():
    sifre = input(" Bir şifre belirleyin: ")

    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]).{8,}$'

    if re.match(pattern, sifre):
        print(" Güçlü şifre! Harika bir seçim!")
    else:
        print(" UYARI!! Şifre zayıf! En az 1 büyük harf, 1 sayı ve 1 özel karakter içermeli, ayrıca 8 karakterden uzun olmalı.")

# Çalıştır
sifre_kontrol()