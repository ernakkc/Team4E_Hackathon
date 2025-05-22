<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CO₂ Emissions Data Analysis Tool - Team4E</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      padding: 20px;
      background-color: #f4f4f4;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    pre {
      background: #eee;
      padding: 10px;
      overflow-x: auto;
    }
    code {
      background: #ddd;
      padding: 2px 4px;
      border-radius: 4px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 8px;
    }
    th {
      background-color: #e1e1e1;
    }
  </style>
</head>
<body>

<h1>🌍 CO₂ Emissions Data Analysis Tool</h1>
<h2>Team4E Hackathon Projesi</h2>

<p>Bu proje, ülkelerin yıllara göre karbondioksit (CO₂) salım verilerini analiz etmeyi amaçlayan konsol tabanlı bir analiz aracıdır. 
CSV dosyalarından alınan verilerle çeşitli karşılaştırmalar, trend analizleri ve raporlar oluşturabilir, sonuçları grafiksel olarak görüntüleyebilirsiniz.</p>


  <h2>📁 Klasör Yapısı</h2>
  <pre><code>project/
├── hackathon_data/
│   ├── annual-co2-emissions-per-country.csv
│   └── population.csv
├── utils/
│   ├── average_emission.py
│   ├── countries_above_threshold.py
│   ├── countries_with_emissions_in_a_certain_range.py
│   ├── country_comparison.py
│   ├── dataProcess.py
│   ├── emission_intensity.py
│   ├── general.py
│   ├── logger.py
│   ├── max_increasing_decreasing.py
│   ├── menu.py
│   ├── report_generation.py
│   ├── sorting_emmision.py
│   ├── trendanalysis.py
│   └── year_to_comparison.py
├── main.py
└── README.md
</code></pre>

  <h2>🚀 Kurulum ve Çalıştırma</h2>
  <ol>
    <li>Python 3 kurulu olmalıdır.</li>
    <li>Gerekli kütüphaneleri yükleyin:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Uygulamayı başlatın:
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>🔧 Özellikler</h2>

  <h3>🔢 Veri İşlemleri</h3>
  <p>Verileri kolayca <strong>ekleyebilir</strong>, <strong>listeleyebilir</strong>, <strong>güncelleyebilir</strong> ve <strong>silebilir</strong>siniz.</p>
  <p>Bunların tamamı <code>dataProcess.py</code> dosyasında yönetilir.</p>

  <h3>📊 Veri Analizi Modülleri</h3>
  <table>
    <thead>
      <tr>
        <th>Özellik</th>
        <th>Açıklama</th>
        <th>Dosya</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Eşik Üstü Ülkeler</strong></td>
        <td>Belirli bir CO₂ değeri üzerindeki ülkeleri listeler</td>
        <td><code>countries_above_threshold.py</code></td>
      </tr>
      <tr>
        <td><strong>İki Ülke Karşılaştırma</strong></td>
        <td>Seçilen yılda iki ülkenin CO₂ salımını karşılaştırır</td>
        <td><code>country_comparison.py</code></td>
      </tr>
      <tr>
        <td><strong>Belirli Aralıkta Ülkeler</strong></td>
        <td>Belirli bir yıl ve salım aralığına göre ülkeleri listeler</td>
        <td><code>countries_with_emissions_in_a_certain_range.py</code></td>
      </tr>
      <tr>
        <td><strong>Ortalama CO₂ Salımı</strong></td>
        <td>Bir ülkenin yıllara göre ortalama CO₂ salımı</td>
        <td><code>average_emission.py</code></td>
      </tr>
      <tr>
        <td><strong>Kişi Başı CO₂</strong></td>
        <td>Nüfusa göre kişi başı CO₂ salımı</td>
        <td><code>emission_intensity.py</code></td>
      </tr>
      <tr>
        <td><strong>Trend Analizi</strong></td>
        <td>Artış/azalış eğilimlerini analiz eder</td>
        <td><code>trendanalysis.py</code></td>
      </tr>
      <tr>
        <td><strong>Sıralama & Grafik</strong></td>
        <td>Verileri sıralayıp grafikler üretir</td>
        <td><code>sorting_emmision.py</code></td>
      </tr>
      <tr>
        <td><strong>Değişim Tespiti</strong></td>
        <td>Son 10 yıldaki maksimum artış/azalışları bulur</td>
        <td><code>max_increasing_decreasing.py</code></td>
      </tr>
      <tr>
        <td><strong>Yıllar Arası Karşılaştırma</strong></td>
        <td>Farklı iki yıl arasındaki salım farklarını gösterir</td>
        <td><code>year_to_comparison.py</code></td>
      </tr>
      <tr>
        <td><strong>Rapor Oluşturma</strong></td>
        <td>Tam kapsamlı analiz raporu üretir</td>
        <td><code>report_generation.py</code></td>
      </tr>
    </tbody>
  </table>

  <h2>📋 Menü Sistemi</h2>
  <p>
    Program, kullanıcı dostu bir <strong>menü sistemi</strong> ile çalışır. Kullanıcılar menüden istediği işlemi seçerek analizleri başlatabilir.
  </p>

  <h2>📘 Örnek Kullanım</h2>
  <ol>
    <li>Program başlatılır.</li>
    <li>Menüden <strong>"6. İki ülkenin salım karşılaştırması"</strong> seçilir.</li>
    <li>Kullanıcıdan iki ülke ve yıl bilgisi alınır.</li>
    <li>Seçilen ülkelerin CO₂ salım miktarları grafikle gösterilir.</li>
  </ol>

  <h2>🧱 Kullanılan Kütüphaneler</h2>
  <ul>
    <li><code>matplotlib</code> – Grafik oluşturma</li>
    <li><code>csv</code> – CSV verilerini işleme</li>
    <li><code>os</code>, <code>sys</code> – Konsol işlemleri</li>
    <li><code>input()</code> – Kullanıcı etkileşimi</li>
    <li><code>utils/logger.py</code> – Renkli konsol çıktıları için özel logger</li>
  </ul>

  <h2>📞 İletişim</h2>
  <p><strong>Proje Sahibi:</strong> Team4E_Hackathon</p>

</body>
</html>
