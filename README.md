# 🚀 Teams Bulk Member Adder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![GUI: CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-indigo.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Platform: Windows | Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg)](#-quick-start-running-from-source)
[![i18n: EN | TR | ES | FR | DE](https://img.shields.io/badge/i18n-EN%20%7C%20TR%20%7C%20ES%20%7C%20FR%20%7C%20DE-green.svg)](#-internationalization)

> **Automate bulk student and member enrollment into Microsoft Teams classes and teams directly from Excel (`.xlsx`, `.xls`) and CSV files.**

[🇹🇷 Türkçe Dokümantasyon için tıklayın (README_TR.md)](README_TR.md)

---

## 📌 Problem

In Microsoft Teams, team owners and educators cannot simply copy and paste a list of 50–100+ email addresses into the "Add member" dialog. Teams requires typing or pasting each email individually, waiting for directory lookup, selecting the suggestion, and repeating this tedious process one by one.

**Teams Bulk Member Adder** eliminates this manual work:
1. Load your Excel or CSV file.
2. The smart detector automatically identifies Email, ID, and Name columns.
3. Switch to Teams during the 5-second countdown.
4. The tool automatically types, resolves, and enters all members one by one.
5. Click **"Add"** in Teams and you are done!

---

## ✨ Features

- **🎯 Smart Column Detection:** Automatically identifies email, member/student ID, and name columns across university management systems (University SIS / OBS, Canvas, Moodle, Blackboard) and multiple languages.
- **🌍 Multi-Language (i18n):** Native support with an on-the-fly language switcher for:
  - 🇬🇧 English (`en`)
  - 🇹🇷 Turkish (`tr`)
  - 🇪🇸 Spanish (`es`)
  - 🇫🇷 French (`fr`)
  - 🇩🇪 German (`de`)
- **🎨 Modern User Interface:** Built with CustomTkinter featuring clean dark and light modes, responsive design, and sticky control panels that never disappear on window resize.
- **🛡️ Safety & FailSafe:** Moving the mouse cursor to any corner of the screen triggers PyAutoGUI's FailSafe and immediately terminates the automation safely.
- **📋 Clipboard-Powered Emulation:** Pastes emails via clipboard (`Ctrl+V`) to ensure 100% character accuracy without keyboard layout or special character issues.
- **💾 Data Export:** Export verified email lists as clean newline-separated `.txt` or standardized `.csv` files.
- **📦 Zero-Dependency Executable:** Can be compiled into a standalone `.exe` using PyInstaller—no Python installation required for end users.

---

## 🚀 Quick Start (Running from Source)

### Prerequisites

- Python 3.10 or newer
- **Windows:** Microsoft Teams Desktop app or Web app
- **Linux:** X11 desktop environment, plus system packages:
  ```bash
  sudo apt update && sudo apt install -y python3-tk xclip
  ```

### 1. Clone the repository
```bash
git clone https://github.com/ynsdgr53/teams-bulk-member-adder.git
cd teams-bulk-member-adder
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
# Windows
python src/main.py

# Linux
python3 src/main.py
```
*(Or double-click `run.bat` on Windows)*

---

## 📦 Building a Standalone Executable (`.exe`)

You can compile the entire application into a single portable `.exe` file that can be shared with colleagues without requiring Python:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "Teams_Bulk_Member_Adder" --collect-all customtkinter src/main.py
```
*(Or simply double-click `build_exe.bat` on Windows)*

The compiled executable will be located in the root directory as `Teams_Bulk_Member_Adder.exe`.

---

## 📖 Step-by-Step Usage Guide

1. **Select File:** Click **"Browse..."** and choose your Excel (`.xlsx`, `.xls`) or `.csv` file.
2. **Review Columns:** The application automatically maps the Email, ID, and Name columns. You can manually adjust them if needed.
3. **Open Microsoft Teams:**
   - Go to your team or class.
   - Click the `...` menu next to the team name and select **"Add member"**.
   - Make sure the member search box is visible on your screen.
4. **Start Automation:**
   - Click **"Add All to Teams"** (or **"Test (First 2)"** to verify first).
   - A **5-second audible countdown** will begin.
   - During these 5 seconds, switch to Teams and **click inside the member search input box**.
5. **Finalize:**
   - The tool will automatically enter all members one by one.
   - Once completed, click the blue **"Add"** button in Teams to finalize enrollment.

---

## 🧪 Running Unit Tests

Unit tests are included to verify Excel and CSV parsing, as well as multi-language column detection:

```bash
python -m unittest discover -s tests
```

---

## 📁 Project Structure

```
TeamsBulkMemberAdder/
│
├── .github/
│   └── workflows/
│       └── release.yml        # Automated GitHub Actions workflow to build .exe
├── src/
│   ├── __init__.py
│   ├── main.py                # Application entry point
│   ├── app.py                 # Modern CustomTkinter UI
│   ├── importer.py            # Smart Excel & CSV data loader & column detector
│   ├── automator.py           # Safe keyboard/clipboard automation engine
│   └── i18n.py                # Multi-language translation manager
├── tests/
│   ├── __init__.py
│   └── test_importer.py       # Unit tests for multi-language importing
├── .gitignore
├── LICENSE                    # MIT License
├── README.md                  # English Documentation
├── README_TR.md               # Turkish Documentation
├── requirements.txt           # Python dependencies
├── pyproject.toml             # Modern packaging metadata
├── build_exe.bat              # One-click Windows build script
└── run.bat                    # Quick launcher
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
