import customtkinter as ctk
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    # url = entry_url.get()
    product = entry_url.get()
    url = f"https://www.flipkart.com/search?q={product.replace(' ', '%20')}"
    data = {'title': [], 'price': []}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all("div", class_="RG5Slk")
        prices = soup.find_all("div", attrs={"class": "hZ3P6w DeU9vF"})

        for title in titles:
            data["title"].append(title.get_text(strip=True))
        for price in prices:
            data["price"].append(price.get_text(strip=True))

        df = pd.DataFrame.from_dict(data)
        filename = product + ".csv"
        df.to_csv(filename, index=False)
        output_label.configure(text=f"✅ {filename} Created Successfully", text_color="green")
    except Exception as e:
        output_label.configure(text=f"❌ Error: {str(e)}", text_color="red")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Flipkart Product Scraper")
app.geometry("500x300")

label_title = ctk.CTkLabel(app, text="Enter Product Name:", font=ctk.CTkFont(size=14))
label_title.pack(pady=10)

entry_url = ctk.CTkEntry(app, width=450)
# entry_url.insert(0, "iphone 16")
entry_url.pack(pady=5)

scrape_button = ctk.CTkButton(app, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=15)

output_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=13))
output_label.pack(pady=10)

app.mainloop()
