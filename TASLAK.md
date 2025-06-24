## ProcSpy GUI

___

## 1\. PROJE GENEL TANIMI

**Amaç:**  
Windows 10/11 ortamında çalışan, sistemdeki mikrofon ve kamera erişimlerini gerçek zamanlı tespit eden, kullanıcıya anlık ve geçmiş verilerle güçlü görünürlük sağlayan, yüksek kullanılabilirlik ve güvenlik standartlarına sahip bir GUI uygulaması geliştirmek.

## 2\. MİMARİ TASARIM & KATMANLAR

### 2.1. Yüksek Seviye Mimarî

```
<div><p>pgsql</p><p><code><span><span>+</span><span><span>---------------------------+</span></span><span>
|        GUI Katmanı        |  &lt;- PySide6 (QMainWindow + Tabs)
| - </span><span><span>View</span></span><span> &amp; </span><span><span>User</span></span><span> Interaction |
+</span><span><span>---------------------------+</span></span><span>
           |
+</span><span><span>---------------------------+</span></span><span>
|      İş Mantığı Katmanı    |  &lt;- Controller, Arka Plan Threadler
| - Süreç Tespiti           |
| - Veri Modeli Yönetimi    |
+</span><span><span>---------------------------+</span></span><span>
           |
+</span><span><span>---------------------------+</span></span><span>
|    Sistem / API Katmanı    |  &lt;- Windows API, WMI, COM, Kernel Calls
| - Mikrofon/Kamera Tespiti |
| - Process Bilgileri       |
+</span><span><span>---------------------------+</span></span><span>
           |
+</span><span><span>---------------------------+</span></span><span>
|       Veri Katmanı         |  &lt;- Loglama, Config, History DB
| - </span><span><span>JSON</span></span><span>/CSV, SQLite, </span><span><span>Log</span></span><span>    |
+</span><span><span>---------------------------+</span></span><span>
</span></span></code></p></div>
```

___

## 3\. TEKNOLOJİ YIĞINI & SEÇİMLER

| Katman | Teknoloji/Kütüphane | Açıklama | Alternatifler |
| --- | --- | --- | --- |
| Programlama Dili | Python 3.10+ | Geniş kütüphane desteği, hızlı geliştirme | C#, Rust, Go (zamanla) |
| GUI | PySide6 (Qt for Python) | Platformlar arası, zengin widget seti | PyQt5, wxPython, Kivy |
| Sistem API | pywin32, comtypes, ctypes, WMI | Windows API entegrasyonu, COM arayüzü | pywinauto, win32gui |
| Çoklu İşlem | threading.Thread, concurrent.futures | GUI donmasını engellemek için asenkron çalışma | asyncio (karmaşık), multiprocessing |
| Veritabanı | SQLite (via `sqlite3` veya `SQLAlchemy`) | Erişim logları ve geçmiş veriler için yerel veritabanı | JSON, CSV |
| Loglama | Python logging modülü | Detaylı debug ve hata kayıtları | Loguru |
| Paketleme | PyInstaller, cx\_Freeze | EXE üretmek için | Nuitka |
| Test | pytest, unittest | Birim ve entegrasyon testleri | tox, coverage |

___

## 4\. KOD MİMARİSİ & MODÜLER YAPI

### 4.1. Modüler Yapı

| Modül/Klasör | Sorumluluk | Notlar |
| --- | --- | --- |
| `src/gui` | Arayüz sınıfları, widget’lar, ana pencere | Signal/Slot bağlantıları burada kurulur |
| `src/core/detectors` | Mikrofon ve Kamera tespit modülleri | Ayrı detectorlar (factory pattern uygulanabilir) |
| `src/core/monitor` | Arka plan threadleri, izleme servisleri | Thread-safe veri aktarımı için Event ve Queue |
| `src/core/models` | Veri modelleri, process bilgisi, erişim durumu | Pydantic veya dataclasses ile yapılandırılabilir |
| `src/utils` | Yardımcı fonksiyonlar, Windows API wrapper’ları | Hata yönetimi, API çağrıları burada toplanır |
| `src/config` | Uygulama ayarları, konfigürasyon yönetimi | JSON veya YAML formatında yapılandırma |
| `src/resources` | İkonlar, stil dosyaları (QSS), statik içerikler | Temalar için genişletilebilir |
| `logs` | Log dosyaları | Günlük döndürme (rotation) ve seviye bazlı loglama |
| `tests` | Test senaryoları | Unit, integration, GUI testleri |
| `docs` | Proje dökümantasyonu, API açıklamaları | Sphinx veya MkDocs önerilir |

___

## 5\. FONKSİYONEL ÖZELLİKLER & İLERİ SEVİYE YAKLAŞIMLAR

| Özellik | Detaylar & İyileştirmeler | Teknoloji/Metod |
| --- | --- | --- |
| Mikrofon & Kamera erişim tespiti | API ve heuristic yöntemler kombinasyonu | WASAPI, WMI, DeviceIoControl + Process handle tarama |
| Gerçek zamanlı izleme | 3 saniyelik periyotlarla kontrol, thread ile paralel çalışma | threading + Signal-Slot ile GUI güncelleme |
| Detaylı process bilgisi | PID, isim, path, erişim zamanı, CPU/Memory kullanımı | psutil + WMI |
| Kullanıcı dostu GUI | Renklendirme, tooltip, ikonlar, filtre, yenile butonu | PySide6 QTableWidget, CSS stili |
| Geçmiş kayıtlar & loglama | JSON/CSV dışa aktarma, SQLite destekli geçmiş veritabanı | sqlite3, pandas, logging modülü |
| Uyarı ve bildirim sistemi | Şüpheli davranışlarda popup ve status bar uyarısı | Qt Dialog, System Tray Notification (win10toast) |
| Güvenlik ve gizlilik | Veriler şifreli kayıt (AES), sadece yetkili kullanıcılar için | cryptography kütüphanesi |
| Modüler ve genişletilebilir mimari | Yeni detector eklenebilirlik, eklenti sistemi | Plugin pattern, dynamic import |
| Performans & kaynak yönetimi | Hafif CPU kullanımı, thread-safe, bellek sızıntısı önleme | Profiling, resource cleanup |
| Çoklu dil desteği (i18n) | İngilizce & Türkçe başlangıç, kolay eklenebilir dil dosyaları | Qt Linguist, `.ts` dosyaları |
| Otomatik güncelleme & sürüm kontrolü | Uygulama içi güncelleme kontrolü, sürüm takibi | PyUpdater, GitHub API |
| Erişim Kontrolü | Admin yetkisi ile çalışma zorunluluğu, izin sorgulama | UAC istemci kontrolü |
| CLI Arayüzü & Otomasyon | Komut satırı parametreleriyle çalışma | argparse |

___

## 6\. MİKROFON VE KAMERA ERİŞİMİ TESBİT DETAYLARI

### 6.1. Kamera Erişim Tespiti

-   `WMI` üzerinden aktif processler ve donanım ilişkileri sorgulanır.
    
-   `SetupAPI` kullanılarak cihazlar ve sürücüler taranır.
    
-   `DeviceIoControl` ile device handle’ları açan processler bulunur.
    
-   `DirectShow` ve `Media Foundation` filtreleriyle aktif video stream sorgulanır.
    
-   Heuristic: USB port ve driver sorgulamalarıyla cihaz kullanımda mı kontrol edilir.
    
-   Güvenlik: Admin yetkisi ile çalıştırılmalı, API çağrılarında hata yönetimi kritik.
    

### 6.2. Mikrofon Erişim Tespiti

-   `Core Audio API (WASAPI)` kullanılarak aktif `AudioSession`lar incelenir.
    
-   `IMMDeviceEnumerator` ve `IAudioSessionManager` ile capture stream’ler listelenir.
    
-   `audiodg.exe` process’in altındaki sessionlar parse edilir.
    
-   Heuristic: Process bazlı stream açma/kapama döngüleri takip edilir.
    
-   Alternatif: `etw` (Event Tracing for Windows) ile kernel seviyesinde audio event yakalanabilir (ileri seviye).
    

___

## 7\. GUI TASARIM & USER EXPERIENCE (UX) DETAYLARI

| Bileşen | Özellikler | İleri Seviye UX Düşünceleri |
| --- | --- | --- |
| Ana Pencere | QMainWindow, Titlebar’da app adı ve versiyon | Modern flat design, DPI scaling destekli |
| Sekmeler | "Mikrofon" ve "Kamera", ikonlu ve renkli | Sekme geçiş animasyonu, arama çubuğu |
| Process Tablosu | Kolonlar: PID, İsim, Path, Başlangıç Zamanı, Durum (Aktif/Pasif) | Canlı filtreleme, sütun sıralama, context menu |
| Renk Kodları | Explorer – gri, tanınan popüler uygulamalar – sarı, bilinmeyen/kara liste – kırmızı | Erişim riski seviyesi gösterimi |
| Tooltip | Process path, komut satırı argümanları, son erişim zamanı | Kopyalama butonu, detaylı bilgi popup’ları |
| Durum Çubuğu | Anlık erişim sayısı, sistem durumu | Canlı uyarılar, bağlantı durumu göstergesi |
| Butonlar | Yenile, Filtrele (Aktif erişimler), Ayarlar | Kısayol tuşları, sağ tıklama menüsü |
| Tema | Light & Dark mode, özelleştirilebilir renk paletleri | Kullanıcı tercihlerine göre otomatik tema seçimi |

___

## 8\. GÜVENLİK & İZLENEBİLİRLİK

| Konu | Açıklama & Öneriler |
| --- | --- |
| Yetkilendirme | Yalnızca admin yetkisiyle çalıştırılmalı, UAC ile kontrol |
| Veri Şifreleme | Log dosyaları AES ile şifrelenmeli |
| Güvenlik Denetimi | Kodda injection, buffer overflow riskleri minimize edilmeli |
| Erişim Loglama | Hangi process ne zaman ve ne sıklıkla erişti kaydedilmeli |
| Log Koruma | Yetkisiz erişime karşı loglar korunmalı |
| Otomatik Uyarılar | Anormal erişimler için bildirim mekanizması |
| Güncelleme Güvenliği | İmzalı güncellemeler, TLS üzerinden indirme |
| Açık Kaynak Güvenliği | Bağımlılık güncellemeleri ve güvenlik yamaları takip edilmeli |

___

## 9\. PERFORMANS OPTİMİZASYONU

-   Arka plan thread’leri minimum CPU ve RAM kullanacak şekilde optimize edilmeli.
    
-   API çağrıları önbellekleme ve debounce uygulanmalı.
    
-   Gereksiz GUI güncellemeleri engellenmeli (veri farkı kontrolü).
    
-   Profiling ile bellek sızıntıları önlenmeli.
    
-   Async işlemler için thread havuzu kullanılabilir.
    
-   Çok büyük process listelerinde sayfalama ve lazy loading yapılabilir.
    

___

## 10\. TEST STRATEJİSİ

| Test Türü | İçerik | Araçlar & Metodolojiler |
| --- | --- | --- |
| Unit Test | Fonksiyonel doğruluk, modüller arası sınırlar | pytest, mock, fixtures |
| Integration Test | Modüllerin birlikte çalışması, API çağrılarının test edilmesi | pytest, CI pipeline (GitHub Actions, Jenkins) |
| GUI Test | Arayüz elemanlarının fonksiyonel testi | PySide6 QTest, Selenium (mümkünse) |
| Load Test | Uzun süreli çalışma, kaynak kullanımı testi | Profiling araçları (py-spy, memory\_profiler) |
| Security Test | Yetki kontrolleri, log güvenliği | Penetrasyon testi, statik kod analizi |
| User Acceptance Test | Son kullanıcı senaryoları, UX testleri | Beta tester feedback, manuel testler |

___

## 11\. GELİŞTİRME VE SÜRÜM YÖNETİMİ

-   Git branch modeli: GitFlow veya trunk-based development önerilir.
    
-   Kod inceleme zorunlu (pull request ile).
    
-   Kod standartları: PEP8 uyumu, otomatik formatlama (black, isort).
    
-   CI/CD pipeline: Otomatik test, paketleme, statik analiz (SonarQube, pylint).
    
-   Sürüm numaralandırma: SemVer (ör. v1.0.0)
    
-   Geliştirme dökümantasyonu düzenli tutulmalı (`docs/DEVELOPMENT.md`).
    
-   Kullanıcı dokümanı ve API dökümantasyonu (`docs/USER_GUIDE.md`, `docs/API.md`).
    

___

## 12\. DAĞITIM & YAYIN

-   PyInstaller ile tek executable haline getirme.
    
    
-   Dijital imzalama ve sertifika entegrasyonu.
    
-   Sürüm notları (changelog) hazırlanması.
    
-   Otomatik güncelleme mekanizması (PyUpdater).
    
___

## 13\. GELİŞTİRME ÖRNEK AKIŞI (FLOW)

1.  `main.py` → uygulama başlatılır, `MainWindow` oluşturulur
    
2.  `MainWindow` → `QTabWidget` ile Mikrofon ve Kamera sekmelerini yükler
    
3.  Arka planda `background_monitor.py` iki thread başlatır:
    
    -   `monitor_microphone()`
        
    -   `monitor_camera()`
        
4.  Thread’ler belirli aralıklarla `detectors/` modüllerini çağırır, erişen process listesini alır
    
5.  Yeni veri GUI thread’ine `PySide6.Signal` ile iletilir
    
6.  `QTableWidget` güncellenir (eski liste ile fark kontrolü yapılarak)
    
7.  Kullanıcı yenileme veya filtreleme yaparsa ilgili slot çalışır
    
8.  Loglama modülü aktif erişimleri kaydeder, gerektiğinde dışa aktarım sağlar
    
9.  Hata durumunda kullanıcıya uyarı gösterilir ve log dosyasına yazılır
    

___

## 14\. KOD ÖRNEĞİ: Thread ve Signal-Slot Kullanımı

```
<div><p>python</p><p><code id="code-lang-python"><span><span><span>from</span></span><span> PySide6.QtCore </span><span><span>import</span></span><span> QObject, Signal, QThread
</span><span><span>import</span></span><span> time

</span><span><span>class</span></span><span> </span><span><span>MonitorWorker</span></span><span>(</span><span><span>QObject</span></span><span>):
    data_updated = Signal(</span><span><span>list</span></span><span>)  </span><span><span># Yeni process listesi</span></span><span>

    </span><span><span>def</span></span><span> </span><span><span>__init__</span></span><span>(</span><span><span>self, detector_func, interval=<span>3</span></span></span><span>):
        </span><span><span>super</span></span><span>().__init__()
        self._running = </span><span><span>True</span></span><span>
        self.detector_func = detector_func
        self.interval = interval

    </span><span><span>def</span></span><span> </span><span><span>stop</span></span><span>(</span><span><span>self</span></span><span>):
        self._running = </span><span><span>False</span></span><span>

    </span><span><span>def</span></span><span> </span><span><span>run</span></span><span>(</span><span><span>self</span></span><span>):
        </span><span><span>while</span></span><span> self._running:
            process_list = self.detector_func()
            self.data_updated.emit(process_list)
            time.sleep(self.interval)

</span><span><span># Kullanımı main_window.py içinde:</span></span><span>
</span><span><span># thread = QThread()</span></span><span>
</span><span><span># worker = MonitorWorker(detect_microphone_processes)</span></span><span>
</span><span><span># worker.moveToThread(thread)</span></span><span>
</span><span><span># thread.started.connect(worker.run)</span></span><span>
</span><span><span># worker.data_updated.connect(update_gui_table)</span></span><span>
</span><span><span># thread.start()</span></span><span>
</span></span></code></p></div>
```

___

## 15\. GELİŞMİŞ ÖNERİLER VE İLERİ SEVİYE KATMA DEĞERLER

| İyileştirme / Özellik | Açıklama |
| --- | --- |
| Erişim Anomali Algoritması | Makine öğrenmesi ile olağan dışı erişimlerin tespiti |
| Saldırı Simülasyonu | Test ortamında simüle edilmiş kötü amaçlı erişim |
| Entegrasyon API | REST veya gRPC ile uzaktan izleme ve entegrasyon |
| Bulut Senkronizasyonu | Kullanıcı ayarları ve logların buluta yedeklenmesi |
| Çoklu Kullanıcı Desteği | Kullanıcı bazlı erişim kontrolü |
| Gelişmiş Filtreleme | Tarih aralığı, process özelliklerine göre filtreleme |
| Erişim İzinleri Yönetimi | Uygulamaya özel izin yönetimi |

___

## 16\. DİZİN YAPISI

```
ProcSpy-GUI/
├── main.py                     # Ana giriş noktası
├── requirements.txt            # Gerekli kütüphaneler
├── README.md                   # Proje dokümantasyonu
├── .gitignore                  # Git ignore dosyası
├── config/
│   ├── __init__.py
│   └── settings.py            # Uygulama ayarları
├── src/
│   ├── __init__.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py     # Ana pencere sınıfı
│   │   ├── tabs/
│   │   │   ├── __init__.py
│   │   │   ├── base_tab.py    # Temel tab sınıfı
│   │   │   ├── microphone_tab.py  # Mikrofon sekmesi
│   │   │   └── camera_tab.py      # Kamera sekmesi
│   │   ├── widgets/
│   │   │   ├── __init__.py
│   │   │   ├── process_table.py   # Process tablosu widget'ı
│   │   │   └── status_bar.py      # Durum çubuğu
│   │   └── dialogs/
│   │       ├── __init__.py
│   │       └── about_dialog.py    # Hakkında diyalogu
│   ├── core/
│   │   ├── __init__.py
│   │   ├── detectors/
│   │   │   ├── __init__.py
│   │   │   ├── base_detector.py   # Temel detector sınıfı
│   │   │   ├── camera_detector.py # Kamera erişim tespiti
│   │   │   └── microphone_detector.py # Mikrofon erişim tespiti
│   │   ├── monitor/
│   │   │   ├── __init__.py
│   │   │   └── background_monitor.py # Arka plan izleme thread'leri
│   │   └── models/
│   │       ├── __init__.py
│   │       └── process_info.py    # Process bilgi modeli
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── windows_api.py         # Windows API yardımcıları
│   │   ├── logger.py              # Loglama yardımcıları
│   │   └── helpers.py             # Genel yardımcı fonksiyonlar
│   └── resources/
│       ├── __init__.py
│       ├── icons/
│       │   ├── app_icon.ico       # Uygulama ikonu
│       │   ├── microphone.png     # Mikrofon ikonu
│       │   ├── camera.png         # Kamera ikonu
│       │   └── warning.png        # Uyarı ikonu
│       └── styles/
│           └── main.qss           # Qt Style Sheet
├── tests/
│   ├── __init__.py
│   ├── test_detectors.py          # Detector testleri
│   ├── test_gui.py                # GUI testleri
│   └── test_utils.py              # Yardımcı fonksiyon testleri
├── docs/
│   ├── API.md                     # API dokümantasyonu
│   ├── DEVELOPMENT.md             # Geliştirme kılavuzu
│   └── USER_GUIDE.md              # Kullanıcı kılavuzu
├── build/                         # Build dosyaları (PyInstaller vb.)
│   └── .gitkeep
├── dist/                          # Dağıtım dosyaları
│   └── .gitkeep
└── logs/                          # Log dosyaları
    └── .gitkeep
```

## Dizin Açıklamaları

### 📁 **Kök Dizin**
- `main.py`: Uygulamanın ana giriş noktası
- `requirements.txt`: Python bağımlılıkları
- `README.md`: Proje dokümantasyonu

### 📁 **config/**
- Uygulama ayarları ve konfigürasyon dosyaları

### 📁 **src/gui/**
- **main_window.py**: Ana pencere ve uygulama mantığı
- **tabs/**: Mikrofon ve kamera sekmeleri
- **widgets/**: Özel GUI bileşenleri
- **dialogs/**: Pop-up diyaloglar

### 📁 **src/core/**
- **detectors/**: Kamera ve mikrofon erişim tespit sınıfları
- **monitor/**: Arka plan izleme thread'leri
- **models/**: Veri modelleri

### 📁 **src/utils/**
- Windows API wrapper'ları ve yardımcı fonksiyonlar

### 📁 **src/resources/**
- **icons/**: Uygulama ikonları
- **styles/**: Qt stylesheet dosyaları

### 📁 **tests/**
- Unit testler ve entegrasyon testleri

### 📁 **docs/**
- Proje dokümantasyonu

### 📁 **build/ & dist/**
- PyInstaller ile executable oluştururken kullanılacak

### 📁 **logs/**
- Uygulama log dosyaları
