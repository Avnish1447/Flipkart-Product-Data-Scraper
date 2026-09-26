import os
import subprocess
import threading
import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
import pandas as pd

last_exported_file = None

def run_scraper_thread():
    threading.Thread(target=scrape_data, daemon=True).start()

def scrape_data():
    global last_exported_file
    product = entry_product.get().strip()
    if not product:
        update_status("⚠️ Please enter a product name", "#FF9F0A")
        return

    url = f"https://www.flipkart.com/search?q={product.replace(' ', '%20')}"
    data = {'title': [], 'price': []}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }

    # UI State: Scraping
    scrape_button.configure(state="disabled", text="Scraping...")
    progress_bar.set(0)
    progress_bar.start()
    update_status("Fetching data from Flipkart...", ("#007AFF", "#0A84FF"))
    hide_action_buttons()

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Selectors across different Flipkart layouts
        titles = soup.find_all("div", class_="RG5Slk")
        if not titles:
            titles = soup.find_all("div", class_="KzDlHZ") or soup.find_all("a", class_="wjcEIp")

        prices = soup.find_all("div", class_="DeU9vF")
        if not prices:
            prices = soup.find_all("div", class_="Nx9bqj")

        for title, price in zip(titles, prices):
            data["title"].append(title.get_text(strip=True))
            data["price"].append(price.get_text(strip=True))

        if not data["title"]:
            update_status("⚠️ No products found or request was blocked", "#FF9F0A")
            return

        df = pd.DataFrame(data)
        filename = f"{product}.csv"
        df.to_csv(filename, index=False)
        last_exported_file = os.path.abspath(filename)

        update_status(f"✨ Saved {len(data['title'])} products to {filename}", ("#34C759", "#30D158"))
        show_action_buttons()
    except Exception as e:
        update_status(f"❌ Error: {str(e)}", ("#FF3B30", "#FF453A"))
    finally:
        progress_bar.stop()
        progress_bar.set(0)
        scrape_button.configure(state="normal", text="Scrape")

def update_status(text, color):
    output_label.configure(text=text, text_color=color)

def show_action_buttons():
    actions_frame.pack(fill="x", padx=16, pady=(12, 4))

def hide_action_buttons():
    actions_frame.pack_forget()

def reveal_in_finder():
    if last_exported_file and os.path.exists(last_exported_file):
        subprocess.run(["open", "-R", last_exported_file])

def open_file():
    if last_exported_file and os.path.exists(last_exported_file):
        subprocess.run(["open", last_exported_file])

def set_appearance(mode):
    ctk.set_appearance_mode(mode)

# --- macOS Tahoe Frosted Theme (Solid UI Elements) ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Flipkart Product Scraper")
app.geometry("590x470")
app.resizable(False, False)

# Keep the window 100% solid and opaque (no faded elements)
app.attributes("-alpha", 1.0)
app.configure(fg_color=("#E5E7EB", "#111216"))

SF_FONT = ".AppleSystemUIFont"

# Outer Container
root_container = ctk.CTkFrame(app, fg_color="transparent")
root_container.pack(fill="both", expand=True, padx=28, pady=24)

# Header Section: Title & Subtitle + Theme Segmented Button
header_frame = ctk.CTkFrame(root_container, fg_color="transparent")
header_frame.pack(fill="x", pady=(0, 16))

header_left = ctk.CTkFrame(header_frame, fg_color="transparent")
header_left.pack(side="left")

title_label = ctk.CTkLabel(
    header_left,
    text="Flipkart Scraper",
    font=ctk.CTkFont(family=SF_FONT, size=23, weight="bold"),
    text_color=("#111827", "#F9FAFB"),
    anchor="w"
)
title_label.pack(anchor="w")

subtitle_label = ctk.CTkLabel(
    header_left,
    text="macOS Tahoe Frosted Glass • Live Product Data Extractor",
    font=ctk.CTkFont(family=SF_FONT, size=12),
    text_color=("#6B7280", "#9CA3AF"),
    anchor="w"
)
subtitle_label.pack(anchor="w", pady=(2, 0))

# Segmented Theme Switcher
theme_switcher = ctk.CTkSegmentedButton(
    header_frame,
    values=["System", "Light", "Dark"],
    font=ctk.CTkFont(family=SF_FONT, size=11, weight="bold"),
    height=28,
    corner_radius=8,
    dynamic_resizing=False,
    command=set_appearance
)
theme_switcher.set("System")
theme_switcher.pack(side="right")

# Solid Frosted Glass Card with Specular Highlight Rim
card_frame = ctk.CTkFrame(
    root_container,
    corner_radius=18,
    fg_color=("#FFFFFF", "#1E1F26"),
    border_width=1,
    border_color=("#D1D5DB", "#383A48")
)
card_frame.pack(fill="both", expand=True)

card_content = ctk.CTkFrame(card_frame, fg_color="transparent")
card_content.pack(fill="both", expand=True, padx=24, pady=20)

# Input Field Label
input_label = ctk.CTkLabel(
    card_content,
    text="Search Product",
    font=ctk.CTkFont(family=SF_FONT, size=13, weight="bold"),
    text_color=("#1C1C1E", "#E5E5EA")
)
input_label.pack(anchor="w", pady=(0, 8))

# Search Capsule Row
search_row = ctk.CTkFrame(card_content, fg_color="transparent")
search_row.pack(fill="x", pady=(0, 10))

entry_product = ctk.CTkEntry(
    search_row,
    placeholder_text="e.g. MacBook Air M3, iPhone 16, Sony WH-1000XM5...",
    height=42,
    corner_radius=12,
    font=ctk.CTkFont(family=SF_FONT, size=13),
    fg_color=("#F2F2F7", "#16161A"),
    border_color=("#D1D1D6", "#35353E"),
    border_width=1
)
entry_product.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry_product.insert(0, "MacBook Air M3")
entry_product.focus_set()
entry_product.bind("<Return>", lambda event: run_scraper_thread())

# Tahoe Cyan-Blue Glow Pill Button
scrape_button = ctk.CTkButton(
    search_row,
    text="Scrape",
    font=ctk.CTkFont(family=SF_FONT, size=13, weight="bold"),
    height=42,
    width=110,
    corner_radius=12,
    fg_color=("#007AFF", "#0A84FF"),
    hover_color=("#0062CC", "#0070E0"),
    command=run_scraper_thread
)
scrape_button.pack(side="right")

# Slim Progress Indicator
progress_bar = ctk.CTkProgressBar(
    card_content,
    height=3,
    corner_radius=2,
    mode="indeterminate",
    progress_color=("#007AFF", "#0A84FF"),
    fg_color=("#E5E5EA", "#2C2C32")
)
progress_bar.pack(fill="x", pady=(2, 14))
progress_bar.set(0)

# Frosted Glass Status Badge
status_card = ctk.CTkFrame(
    card_content,
    corner_radius=12,
    fg_color=("#F2F2F7", "#16161A"),
    border_width=1,
    border_color=("#E5E5EA", "#2D2D36")
)
status_card.pack(fill="x", pady=(0, 8), ipady=8)

output_label = ctk.CTkLabel(
    status_card,
    text="Ready to search and scrape products",
    font=ctk.CTkFont(family=SF_FONT, size=12, weight="bold"),
    text_color=("#636366", "#AEAEB2")
)
output_label.pack(pady=4)

# Quick Action Buttons (Reveal in Finder & Open CSV)
actions_frame = ctk.CTkFrame(card_content, fg_color="transparent")

btn_finder = ctk.CTkButton(
    actions_frame,
    text="📂 Show in Finder",
    font=ctk.CTkFont(family=SF_FONT, size=12, weight="bold"),
    height=36,
    corner_radius=10,
    fg_color=("#E5E5EA", "#2C2C34"),
    hover_color=("#D1D1D6", "#383842"),
    text_color=("#1C1C1E", "#F5F5F7"),
    border_width=1,
    border_color=("#D1D1D6", "#42424E"),
    command=reveal_in_finder
)
btn_finder.pack(side="left", expand=True, fill="x", padx=(0, 6))

btn_open = ctk.CTkButton(
    actions_frame,
    text="📄 Open CSV",
    font=ctk.CTkFont(family=SF_FONT, size=12, weight="bold"),
    height=36,
    corner_radius=10,
    fg_color=("#E5E5EA", "#2C2C34"),
    hover_color=("#D1D1D6", "#383842"),
    text_color=("#1C1C1E", "#F5F5F7"),
    border_width=1,
    border_color=("#D1D1D6", "#42424E"),
    command=open_file
)
btn_open.pack(side="right", expand=True, fill="x", padx=(6, 0))

actions_frame.pack_forget()

app.mainloop()





