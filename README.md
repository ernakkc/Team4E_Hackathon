# Team4E_Hackathon

# CO₂ Emissions Data Analysis Tool

Bu proje, ülkelerin yıllara göre CO₂ salım verilerini analiz etmek amacıyla geliştirilmiştir. Farklı analiz ve karşılaştırmalar yapabileceğiniz kapsamlı bir konsol uygulamasıdır. Veriler CSV dosyalarından alınır ve kullanıcıya grafiklerle birlikte anlamlı bilgiler sunulur.

## 📂 Klasör Yapısı

project/
├── hackathon_data/
│ ├── hackathon_data/annual-co2-emissions-per-countryannual-co2-emissions-per-country.csv
│ └── hackathon_data/population/population.csv
├── utils/
│ ├── average_emission.py
│ ├── countries_above_threshold.py
│ ├── countries_with_emissions_in_a_certain_range.py
│ ├── country_comparison.py
│ ├── dataProcess.py
│ ├── emission_intensity.py
│ ├── general.py
│ ├── logger.py
│ ├── max_increasing_decreasing.py
│ ├── menu.py
│ ├── report_generation.py
│ ├── sorting_emmision.py
│ ├── trendanalysis.py
│ └── year_to_comparison.py
├── main.py
└── README.md

## 🚀 Nasıl Çalıştırılır?

Python 3 yüklü olmalıdır.

```bash
pip install -r requirements.txt
python main.py
```

🔧 Özellikler
🔢 Veri İşlemleri
Veri Ekleme / Silme / Güncelleme / Listeleme
CSV dosyaları üzerinden CO₂ salım verisi ekleme ve düzenleme işlemleri.

📊 Veri Analizi
Belirli bir eşiğin üzerindeki ülkeleri listeleme
countries_above_threshold.py

İki ülkenin belirli bir yıldaki CO₂ karşılaştırması
country_comparison.py

Belirli bir yıl ve salım aralığına göre ülke filtreleme ve görselleştirme
countries_with_emissions_in_a_certain_range.py

Bir ülkenin yıllara göre ortalama CO₂ salımı
average_emission.py

Kişi başı CO₂ salımı analizi (emission intensity)
emission_intensity.py

Nüfus verisi gerektirir (population.csv)

CO₂ salım trend analizi (artış/azalış eğilimleri)
trendanalysis.py

Verileri sıralama ve grafik oluşturma
sorting_emmision.py

Bir ülkenin son 10 yıldaki değişim oranı ve maksimum artış/azalış tespiti
max_increasing_decreasing.py

Farklı iki yıl arasındaki salım farklarını karşılaştırma
year_to_comparison.py

Tam kapsamlı analiz raporu oluşturma
report_generation.py

📋 Menü Sistemi
Program bir menü sistemi ile çalışır. Kullanıcılar menüden ilgili işlemi seçerek analizleri başlatabilir.

📘 Örnek Kullanım
Program başlatılır.

Menüden "6. İki ülkenin salım karşılaştırması" seçilir.

Kullanıcıdan iki ülke ve yıl bilgisi alınır.

Seçilen ülkelerin CO₂ salım miktarları ekrana yazdırılır ve grafik gösterilir.

🧱 Kullanılan Kütüphaneler
matplotlib – Grafik oluşturma

csv – CSV verilerini işleme

os ve sys – Konsol işlemleri

input() – Kullanıcı etkileşimi

custom logger – Renkli konsol çıktıları (utils/logger.py)

📞 İletişim
Proje sahibi: Team4E_Hackathon
