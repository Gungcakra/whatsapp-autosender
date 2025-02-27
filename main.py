from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


numbers = [
    "6282247800248", "6282146015089", "6281943664991", "6281351567341", "6281574766067",
    "6285737146987", "6281337959680", "6282146560125", "6282341416119", "6281805589154",
    "6281298841377", "62895395934251", "6289604443719", "6281215976397", "6285179986763",
    "6287855223111", "6287897803672", "6289649854005", "6287750226402", "6281999969274",
    "6282145021559", "6287781680370", "6281237113644", "62895347910846", "6281238687335",
    "6281558129904", "6285175202751", "6281237828894", "62895324035230", "6283114298174"
]
message = """Halo kakak 🙌, sehubung kakak sudah mendaftar seminar FANTASI 2025 maka dari itu kami akan mengundang kakak untuk masuk ke grup WhatsApp seminar FANTASI 2025 (online).
Terimakasi 🙏
https://chat.whatsapp.com/Gewi5TVBm3xHtk44afEkct

"""



driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Scan QR Code di WhatsApp Web, lalu tekan Enter untuk melanjutkan...")

for number in numbers:
    try:
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)
        time.sleep(10) 
        
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )
        send_button.click()
        
        print(f"Pesan berhasil dikirim ke {number}")
        time.sleep(5)  
    except Exception as e:
        print(f"Gagal mengirim ke {number}: {e}")

print("Selesai mengirim pesan!")
driver.quit()
