from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# WhatsApp Webi açar
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com")
print("Lütfen QR kodunu tarat...")
time.sleep(40)  # QR kod taratmak için bekleme süresi internet ve bilgisayar hızına göre arttırıp azalt

#menuye girip grup oluşturuyor
try:
    new_chat_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='menu']"))
    )
    new_chat_button.click()
    print("Menu butonuna tıklandı.")

    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    print("Aşağı yön tuşuna basıldı ve Enter'a basılarak devam edildi.")

except:
    print("Menu butonu bulunamadı!")
    driver.quit()

# Grup oluşturulacak numaralar
numbers = ["+905xxxxxxxxx", "905xxxxxxxxx"]

for number in numbers:
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        search_box.send_keys(number)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
        print(f"Kişi eklendi: {number}")
    except:
        print(f"Kişi eklenemedi: {number}")

# İleri butonuna basıyor
try:
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']"))
    )
    next_button.click()
except:
    print("İleri butonu bulunamadı!")

# Grup adını buradan düzenle
try:
    group_name_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='Grup Konusu (İsteğe Bağlı)']"))
    )
    group_name_box.send_keys("SKY LAB: Duyuru 2 vs...")#buraya giriyorsun grup ismini üst tarafa değil
except:
    print("Grup adı girilemedi!")

# Grup oluşturma butonuna basıp tamamlıyor
try:
    create_group_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']"))
    )
    create_group_button.click()
    print("Grup başarıyla oluşturuldu!")
    time.sleep(100)
except:
    print("Grup oluşturma butonu bulunamadı!")

#kullanırken çok fazla gir çık yapıp grup oluşturursanız grup oluşturma banı/hesabı açma banı gibi bişiler yiyebilirsiniz 