from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


numbers = [
# Phone Number
]
message = """
# Message
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
