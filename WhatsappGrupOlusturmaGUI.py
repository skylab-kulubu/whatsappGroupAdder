import tkinter as tk
from tkinter import messagebox
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Renk teması
BACKGROUND_COLOR = "#1E1E2E"
TEXT_BOX_COLOR = "#292841"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#3A7CA5"
EXIT_BUTTON_COLOR = "#F2A65A"

# GUI tasarımı
root = tk.Tk()
root.title("Gecekodu İçin Whatsapp Grup Oluşturucu")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg=BACKGROUND_COLOR)

# Frame
frame = tk.Frame(root, bg=BACKGROUND_COLOR, bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Başlık etiketi
title_label = tk.Label(frame, text="GRUP İÇİN NUMARALAR :", font=("Impact", 24, "bold"),
                       fg="#D6D6D6", bg=BACKGROUND_COLOR)
title_label.pack(pady=10)

# Numaralar için text box
text_box = tk.Text(frame, height=8, width=30, font=("Tahoma", 14),
                   bg=TEXT_BOX_COLOR, fg=TEXT_COLOR,
                   insertbackground=TEXT_COLOR, bd=2, relief="groove")
text_box.pack(pady=10)

def show_success_message(mesaj):
    success_window = tk.Toplevel(root)
    success_window.title("Başarı!")
    success_window.geometry("400x500")
    success_window.resizable(False, False)
    success_window.configure(bg=BACKGROUND_COLOR)

    success_message = tk.Label(success_window, text=mesaj, font=("Comic Sans MS", 16, "bold"),
                               fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
    success_message.place(relx=0.5, rely=0.5, anchor="center")

def start_group_creation():
    raw_numbers = text_box.get("1.0", tk.END).strip()
    if not raw_numbers:
        messagebox.showwarning("Uyarı", "Lütfen en az bir numara girin.")
        return

    numbers = [num.strip() for num in raw_numbers.split("\n") if num.strip()]
    messagebox.showinfo("QR Kodu", "Lütfen tarayıcıda açılan WhatsApp Web'de QR kodunu taratın. Devam etmek için 40 saniyeniz var.")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://web.whatsapp.com")
    time.sleep(40)  # QR kod okutma süresi

    try:
        new_chat_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='menu']"))
        )
        new_chat_button.click()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    except:
        messagebox.showerror("Hata", "Menü butonu bulunamadı!")
        driver.quit()
        return

    for number in numbers:
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            search_box.clear()
            search_box.send_keys(number)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
        except:
            print(f"Kişi eklenemedi: {number}")

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']"))
        )
        next_button.click()
    except:
        messagebox.showerror("Hata", "İleri butonu bulunamadı!")
        driver.quit()
        return

    try:
        create_group_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']"))
        )
        create_group_button.click()
        show_success_message("Grup başarıyla oluşturuldu!\n(Bu sekme ve uygulamayı kapatırsanız açılmış chrome sekmesi de kapanır.)")
        time.sleep(10)
    except:
        messagebox.showerror("Hata", "Grup oluşturma butonu bulunamadı!")
        driver.quit()
        return

# Başlat butonu
start_button = tk.Button(frame, text="💥 GRUP OLUŞTUR 💥", font=("Impact", 18),
                         bg=BUTTON_COLOR, fg="white", command=start_group_creation,
                         bd=0, relief="ridge", padx=20, pady=10,
                         activebackground=BUTTON_COLOR)
start_button.pack(pady=20)

# Çıkış butonu
exit_button = tk.Button(frame, text="🚨 ÇIKIŞ 🚨", font=("Impact", 16),
                        bg=EXIT_BUTTON_COLOR, fg="black", command=root.quit,
                        bd=0, relief="ridge", padx=15, pady=10,
                        activebackground=EXIT_BUTTON_COLOR)
exit_button.pack(pady=10)

root.mainloop()
