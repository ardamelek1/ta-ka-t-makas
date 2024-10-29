Taş-Kağıt-Makas - Yapay Zeka Destekli Python Oyunu
Bu proje, klasik taş-kağıt-makas oyununa şans faktörünü dengeleyen ve oyuncu davranışını öğrenerek stratejik hamleler yapan bir yapay zeka eklenmiş Python oyunudur.

Özellikler
Geleneksel Oyun Mekaniği: Kullanıcıya karşı taş, kağıt ve makas seçenekleriyle oynanır.
Stratejik Bilgisayar Seçimi: Kullanıcı tercihleri analiz edilerek yapay zeka bir sonraki hamlede en uygun yanıtı verir.
İki Farklı Yapay Zeka Stratejisi:
Markov Zinciri: Kullanıcının son iki seçimine göre bilgisayarın en uygun hamleyi yapması sağlanır.
Makine Öğrenmesi: Lojistik regresyon algoritmasıyla kullanıcının seçimi tahmin edilerek karşı hamle yapılır.
Kurulum
Bu projeyi çalıştırmak için Python 3 ve gerekli kütüphanelere ihtiyaç vardır.

Python 3'ü yükleyin: Python web sitesinden Python 3'ü indirip kurabilirsiniz.
Gerekli Kütüphaneleri Yükleyin:
bash
Kodu kopyala
pip install -r requirements.txt
veya
bash
Kodu kopyala
pip install scikit-learn
Kullanım
Projeyi başlatmak için, ana dizinde aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
python main.py
Oynanış
Oyun başlarken "taş", "kağıt" veya "makas" seçimini yaparak oyuna katılabilirsiniz.
Yapay zeka, her hamlede seçimlerinize göre analiz yapar ve stratejik bir yanıt verir.
Oyunu bitirmek için "q" veya herhangi bir geçersiz tuşa basabilirsiniz.
Örnek Ekran Çıktısı
yaml
Kodu kopyala
Taş, kağıt, makas? (Bitirmek için herhangi bir harf): taş Kazandınız! Bilgisayar: makas , Siz: taş Final puanınız: 5
Katkıda Bulunma
Katkıda bulunmak için:

Bu projeyi forklayın
Yeni bir branch oluşturun (
git checkout -b yeni-ozellik
)
Yaptığınız değişiklikleri commit edin (
git commit -m 'Yeni özellik ekle'
)
Branch'i gönderin (
git push origin yeni-ozellik
)
Bir Pull Request açın
