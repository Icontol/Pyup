import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, Style, init

# Inisialisasi Colorama untuk mengaktifkan kode escape ANSI di Windows
init()

# URL website yang ingin Anda periksa dan tampilkan di terminal
website_url = 'https://criticalcourteousdevices.icontol.repl.co'

# Fungsi untuk memeriksa status website
def check_website_status(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return None

# Fungsi untuk mendapatkan dan menampilkan konten teks dari website
def display_website_text_content(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()  # Mengambil konten teks dari website
            print(Fore.GREEN + f"Konten teks dari {url}:" + Style.RESET_ALL)
            print(text_content)  # Menampilkan konten teks
        else:
            print(Fore.RED + f"Website {url} memberikan respons dengan kode status {response.status_code}." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat memeriksa status website {url}: {e}" + Style.RESET_ALL)

# Loop untuk memeriksa status website secara berkala
while True:
    status_code = check_website_status(website_url)
    if status_code is not None:
        if status_code == 200:
            print(Fore.CYAN + f"\nWebsite {website_url} aktif." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Memeriksa konten teks pada: {time.strftime('%Y-%m-%d %H:%M:%S')}" + Style.RESET_ALL)

            display_website_text_content(website_url)
        else:
            print(Fore.RED + f"\nWebsite {website_url} memberikan respons dengan kode status {status_code}." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\nTerjadi kesalahan saat memeriksa status website {website_url}." + Style.RESET_ALL)

    # Waktu jeda sebelum memeriksa status kembali (dalam detik)
    time.sleep(2)  # Waktu jeda 2 detik
