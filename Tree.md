# ProcSpy GUI - Dizin Yapısı

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