# Text Selector OCR (Windows)

Text Selector OCR is a lightweight Windows background utility that allows you to
select any area of the screen and extract text using OCR — similar to the
Snipping Tool, but for copying text.

---

## 🚀 Features

- Screenshot-style text selection
- Global hotkey (**Ctrl + Caps Lock**)
- Runs in the background
- Copies extracted text directly to the clipboard
- Works repeatedly without restarting
- Offline OCR using Tesseract
- Supports multiple languages (based on installed Tesseract models)

---

## 🖥️ System Requirements

- Windows 10 or Windows 11
- Python 3.10 or newer
- Tesseract OCR

---

## 🔧 Installation (From Source)

### 1️⃣ Install Python

Download Python from:  
https://www.python.org/downloads/

✅ During installation, enable **Add Python to PATH**

Verify installation:
```bash
python --version
2️⃣ Install Tesseract OCR
Download the Windows installer from:
https://github.com/UB-Mannheim/tesseract/wiki

Default installation path:

text
Copy code
C:\Program Files\Tesseract-OCR\tesseract.exe
3️⃣ Clone the Repository
Open PowerShell and run:

bash
Copy code
git clone https://github.com/PRANAVKAKDE613/text-selector-ocr.git
cd text-selector-ocr
4️⃣ Install Python Dependencies
bash
Copy code
pip install opencv-python pytesseract pyperclip keyboard pillow plyer numpy
▶️ Running the Tool
Start the program using:

bash
Copy code
python text_selector.py
You should see a message indicating the tool is running in the background.

🎯 How to Use
Press Ctrl + Caps Lock

A transparent overlay appears

Click and drag to select the desired text area

Release the mouse button

✅ Extracted text is copied to the clipboard

Paste the text anywhere using Ctrl + V

You can repeat this process as many times as required.

⚙️ Hotkey Configuration
Default hotkey:

text
Copy code
Ctrl + Caps Lock
You may change the hotkey in text_selector.py if desired.

📦 Build Standalone EXE (Optional)
1️⃣ Install PyInstaller
bash
Copy code
pip install pyinstaller
2️⃣ Build the EXE
bash
Copy code
pyinstaller --onefile --noconsole text_selector.py
Output location:

text
Copy code
dist\text_selector.exe
🔁 Run Automatically on Startup (Recommended)
For reliable startup behavior, use Task Scheduler:

Open Task Scheduler

Click Create Task

Trigger: At log on

Action: Start a program

Program: text_selector.exe

✅ Run only when user is logged on

✅ Run with highest privileges

Save the task

This ensures the tool is available after every system restart.

⚠️ Important Notes
Do not run multiple instances simultaneously

Build folders (build/, dist/) are excluded from the repository

OCR accuracy depends on screen clarity, font, and resolution

Caps Lock triggers multiple key events; this is handled internally

🛠️ Troubleshooting
Ensure the program is running using Task Manager

Verify Tesseract OCR is installed at the correct path

Run the script from terminal to confirm all dependencies are installed

If the hotkey does not work, restart the program once

📄 License
This project is licensed under the MIT License.

⭐ Support
If you find this project helpful:

⭐ Star the repository

🐞 Open an issue for bugs or feature requests

yaml
Copy code

---

## ✅ What to do next

1. Paste this into `README.md`
2. Commit and push:
```bash
git add README.md
git commit -m "Add complete installation and usage README"
git push
