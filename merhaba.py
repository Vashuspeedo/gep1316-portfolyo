from datetime import date

ad = input("Adınız nedir? ")
dogum_yili = int(input("Doğum yılınız nedir? (Örn: 2003): "))

guncel_yil = date.today().year

if dogum_yili > guncel_yil:
    print(f"Uyarı, {ad}! Henüz {dogum_yili} yılına gelmedik. Lütfen geçerli bir doğum yılı girin.")
elif dogum_yili < 1900:
    print(f"Uyarı, {ad}! Girdiğiniz doğum yılı ({dogum_yili}) geçerli görünmüyor.")
else:
    yas = guncel_yil - dogum_yili
    print(f"Merhaba {ad}! {guncel_yil} yılı itibarıyla {yas} yaşındasın. Kodlama dünyasına hoş geldin!")
