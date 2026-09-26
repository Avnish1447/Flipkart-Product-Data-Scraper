# 📦 Flipkart Product Scraper GUI

A modern desktop application built with `customtkinter` featuring an **Apple macOS Tahoe-inspired Frosted Glass interface**. It allows users to search for any product on **Flipkart**, extract real-time **titles** and **prices**, and export clean datasets into `.csv` files with just one click.

---

## ✨ Features

- 🔍 **Search by Product Name**: Simply type any product keyword (no complex URLs needed).
-  **macOS Tahoe Frosted Glass Aesthetic**: Floating frosted glass cards, specular highlight rims, and native San Francisco typography (`.AppleSystemUIFont`).
- 🌓 **Dynamic Theme Switcher**: Easily toggle between **System**, **Light**, and **Dark** modes on the fly.
- ⚡ **Multi-Threaded Scraping**: Background asynchronous execution keeps the UI smooth and responsive without beachballing or freezing.
- 📊 **Slim Activity Indicator**: Real-time animated progress bar during data extraction.
- ⌨️ **Keyboard Shortcut**: Press <kbd>Return / Enter</kbd> to scrape instantly.
- 📂 **Native macOS Quick Actions**: One-click **"Show in Finder"** and **"Open CSV"** buttons once the scrape is complete.
- 🛡️ **Resilient Selectors**: Multi-layout fallback support for diverse Flipkart product search categories.
- 💾 **Automatic CSV Export**: Saves results into a formatted `.csv` file named after your search query.

---

## 🖼️ Interface Preview

<img width="702" height="614" alt="Screenshot 2026-09-26 at 10 21 45 AM" src="https://github.com/user-attachments/assets/ebee6b04-92c7-4f21-8de5-2318d73557b6" />
<img width="702" height="614" alt="Screenshot 2026-09-26 at 10 23 51 AM" src="https://github.com/user-attachments/assets/6645886c-81bd-4b47-ac0c-ad5d6d217598" />


---

## 🔧 Requirements

Ensure you have Python 3.10+ installed (Python 3.12+ recommended for modern Tk 8.6/9.0 on macOS):

```bash
pip install customtkinter requests beautifulsoup4 pandas
```

---

## 🚀 How to Run

1. **Clone or download** the repository:
   ```bash
   git clone https://github.com/Avnish1447/Flipkart-Product-Data-Scraper.git
   cd Flipkart-Product-Data-Scraper
   ```

2. **Run the application**:
   ```bash
   python3 "Data Scraper.py"
   ```

3. Enter any product name (e.g., `MacBook Air M3`, `iPhone 16`, `Sony WH-1000XM5`).
4. Click **"Scrape"** or press <kbd>Return</kbd>.
5. Use the quick action buttons to reveal the generated `.csv` file in Finder or open it immediately in your spreadsheet viewer.

---

## 📁 Output Format

The generated `.csv` file will contain:

| title | price |
| :--- | :--- |
| Apple MacBook Air M3 - (16 GB/256 GB SSD/macOS Sequoia) | ₹1,14,900 |
| Apple iPhone 16 (Black, 128 GB) | ₹69,900 |
| ... | ... |

---

## 🛑 Disclaimer

- This project is for **educational purposes only**.
- Flipkart’s website layout and CSS class names may change over time, which could require periodic selector updates.
- Please use responsibly and respect rate limits.

---

## 🧑‍💻 Author

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Avnish1447)   [![Email](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:avnishagrawal1447@gmail.com)   [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/avnish-agrawal-84b39728a/)
