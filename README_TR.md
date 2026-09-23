# 🚀 Teams Toplu Üye Ekleme Aracı (Teams Bulk Member Adder)

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Arayüz: CustomTkinter](https://img.shields.io/badge/Arayüz-CustomTkinter-indigo.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6.svg)](https://www.microsoft.com/)

> **Excel (`.xlsx`, `.xls`) ve CSV dosyalarındaki öğrencileri ve üyeleri Microsoft Teams sınıflarına/ekiplerine otomatik olarak ekleyen masaüstü aracı.**

[🇬🇧 Click for English Documentation (README.md)](README.md)

---

## 📌 Problem ve Çözüm

Microsoft Teams'te sınıf veya ekip sahipleri 50-100 kişilik bir e-posta listesini toplu kopyala-yapıştır yaparak ekleyemez. Teams arayüzü, her bir öğrencinin e-postasını tek tek yazmanızı, üniversite dizininden bulunmasını beklemenizi ve Enter'a basarak tek tek seçmenizi zorunlu kılar.

**Teams Toplu Üye Ekleme Aracı** bu angaryayı tamamen ortadan kaldırır:
1. Excel veya CSV dosyanızı yükleyin.
2. Program E-Posta, Öğrenci No ve Ad-Soyad sütunlarını otomatik olarak tanır.
3. 5 saniyelik sesli geri sayım sırasında Teams'teki arama kutusuna tıklayın.
4. Program tüm öğrencileri sırayla tek tek kutuya otomatik ekler.
5. Teams'teki **"Ekle"** butonuna basarak işlemi tamamlayın!

---

## ✨ Özellikler

- **🎯 Akıllı Sütun Tespiti:** Üniversite OBS/ÖBS sistemleri, genel bilgi sistemleri, Canvas, Moodle ve Blackboard formatlarını otomatik tanır.
- **🌍 Çoklu Dil Desteği (i18n):** Arayüz üzerinden tek tıkla dil değiştirme:
  - 🇬🇧 İngilizce (`en`)
  - 🇹🇷 Türkçe (`tr`)
  - 🇪🇸 İspanyolca (`es`)
  - 🇫🇷 Fransızca (`fr`)
  - 🇩🇪 Almanca (`de`)
- **🎨 Modern Arayüz:** CustomTkinter ile tasarlanmış modern karanlık ve aydınlık mod, esnek pencere yapısı ve pencere küçüldüğünde kaybolmayan sabit buton paneli.
- **🛡️ Güvenlik ve Acil Durdurma:** Fare imlecini ekranın herhangi bir dış köşesine çekmek işlemi anında durdurur (PyAutoGUI FailSafe).
- **📋 Pano (Clipboard) Desteği:** E-postaları panodan `Ctrl+V` ile yapıştırdığı için Türkçe veya özel karakterlerde hiçbir tuşlama hatası yaşanmaz.
- **💾 Dışa Aktarma:** Yüklenen listedeki mailleri tek tıkla `.txt` veya standart `.csv` dosyası olarak kaydedebilme.
- **📦 Kurulumsuz `.exe` Desteği:** PyInstaller ile tek dosya `.exe` haline getirilebilir; kullanıcıların bilgisayarında Python kurulu olmasına gerek kalmaz.

---

## 🚀 Hızlı Başlangıç (Kaynak Koddan Çalıştırma)

### Gereksinimler

- Python 3.10 veya üzeri
- Windows işletim sistemi (Teams masaüstü uygulaması veya web tarayıcı)

### 1. Depoyu klonlayın
```bash
git clone https://github.com/ynsdgr53/teams-bulk-member-adder.git
cd teams-bulk-member-adder
```

### 2. Gerekli kütüphaneleri yükleyin
```bash
pip install -r requirements.txt
```

### 3. Uygulamayı çalıştırın
```bash
python src/main.py
```
*(Veya Windows'ta doğrudan `run.bat` dosyasına çift tıklayın)*

---

## 📦 Kurulumsuz `.exe` Oluşturma

Projeyi Python gerektirmeyen tek bir `.exe` haline getirmek için:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "Teams_Bulk_Member_Adder" --collect-all customtkinter src/main.py
```
*(Veya Windows'ta doğrudan `build_exe.bat` dosyasına çift tıklayın)*

---

## 📖 Kullanım Kılavuzu

1. **Dosya Seç:** **"Dosya Seç..."** butonuna basarak Excel (`.xlsx`, `.xls`) veya `.csv` dosyanızı seçin.
2. **Sütunları Kontrol Et:** E-Posta, Öğrenci No ve İsim sütunları otomatik eşleştirilir. Gerekirse açılır kutulardan değiştirebilirsiniz.
3. **Teams'i Hazırla:**
   - Teams'te dersinize gidin.
   - Sınıf adının yanındaki `...` menüsünden **"Üye ekle"** penceresini açın.
4. **Otomasyonu Başlat:**
   - **"Hepsini Teams'e Ekle"** butonuna basın (denemek için **"Test Et"** butonunu da kullanabilirsiniz).
   - 5 saniyelik sesli geri sayım başlar.
   - Bu sürede hemen Teams penceresindeki **öğrenci arama kutusuna tıklayın**.
5. **Tamamla:**
   - Program tüm öğrencileri sırayla yapıştırır ve Enter'a basar.
   - İşlem bittiğinde Teams'teki mavi **"Ekle"** butonuna basarak kaydedin.

---

## 📄 Lisans

Bu proje MIT Lisansı altında sunulmaktadır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
