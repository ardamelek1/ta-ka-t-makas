from sklearn.linear_model import LogisticRegression
import numpy as np
import random

# Veri seti oluştur
veri = []
sonuclar = []

# Model tanımla
model = LogisticRegression()

# Eğitim fonksiyonu
def model_egit():
    if len(veri) >= 10:  # En az 10 veriyle eğitime başla
        model.fit(veri, sonuclar)

# Tahmin fonksiyonu
def tahmin_et():
    if len(veri) < 10:
        return random.choice(["taş", "kağıt", "makas"])
    son_secim = [veri[-1]]
    tahmin = model.predict(son_secim)[0]
    return tahmin

# Başlangıç ayarları
puan = 0

while True:
    # Bilgisayar tahmini
    tahmin = tahmin_et()

    # Bilgisayarın stratejik seçimi
    if tahmin == "taş":
        bilgisayar = "kağıt"
    elif tahmin == "kağıt":
        bilgisayar = "makas"
    else:
        bilgisayar = "taş"
   
    # Kullanıcı seçimini al
    kullanıcı = input("taş, kağıt, makas? (Bitirmek için herhangi bir harf): ")

    if kullanıcı not in ["taş", "kağıt", "makas"]:
        print("Final puanınız:", puan)
        break
   
    # Veriyi ekle ve modeli eğit
    veri.append([kullanıcı == "taş", kullanıcı == "kağıt", kullanıcı == "makas"])
    sonuclar.append(1 if bilgisayar == kullanıcı else 0)
    model_egit()

    # Skor ve oyun işlemleri
    if kullanıcı == bilgisayar:
        print("Berabere!")
    elif (kullanıcı == "taş" and bilgisayar == "kağıt") or \
         (kullanıcı == "kağıt" and bilgisayar == "makas") or \
         (kullanıcı == "makas" and bilgisayar == "taş"):
        puan -= 1
        print("Kaybettiniz! Bilgisayar:", bilgisayar, ", Siz:", kullanıcı)
        print('Puan: ' + str(puan))
    else:
        puan += 1
        print("Kazandınız! Bilgisayar:", bilgisayar, ", Siz:", kullanıcı)
        print('Puan: ' + str(puan))
