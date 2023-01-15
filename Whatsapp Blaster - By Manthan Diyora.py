import os
import time
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

root = tk.Tk()
root.withdraw()

print(''' __          __  _               _                                     ____    _                 _                     
 \ \        / / | |             | |                                   |  _ \  | |               | |                    
  \ \  /\  / /  | |__     __ _  | |_   ___    __ _   _ __    _ __     | |_) | | |   __ _   ___  | |_    ___   _ __     
   \ \/  \/ /   | '_ \   / _` | | __| / __|  / _` | | '_ \  | '_ \    |  _ <  | |  / _` | / __| | __|  / _ \ | '__|    
    \  /\  /    | | | | | (_| | | |_  \__ \ | (_| | | |_) | | |_) |   | |_) | | | | (_| | \__ \ | |_  |  __/ | |       
     \/  \/     |_| |_|  \__,_|  \__| |___/  \__,_| | .__/  | .__/    |____/  |_|  \__,_| |___/  \__|  \___| |_|       
                                                    | |     | |                                                        
                                                    |_|     |_|                                                        
  ____              __  __                   _     _                         _____    _                                
 |  _ \            |  \/  |                 | |   | |                       |  __ \  (_)                               
 | |_) |  _   _    | \  / |   __ _   _ __   | |_  | |__     __ _   _ __     | |  | |  _   _   _    ___    _ __    __ _ 
 |  _ <  | | | |   | |\/| |  / _` | | '_ \  | __| | '_ \   / _` | | '_ \    | |  | | | | | | | |  / _ \  | '__|  / _` |
 | |_) | | |_| |   | |  | | | (_| | | | | | | |_  | | | | | (_| | | | | |   | |__| | | | | |_| | | (_) | | |    | (_| |
 |____/   \__, |   |_|  |_|  \__,_| |_| |_|  \__| |_| |_|  \__,_| |_| |_|   |_____/  |_|  \__, |  \___/  |_|     \__,_|
           __/ |                                                                           __/ |                       
          |___/                                                                           |___/                        
          
          ''')

pdf_files = []
num_files = int(input("How many files do you want to send? 1,2,3,4....? "))
for i in range(num_files):
    pdf_file = filedialog.askopenfilename(initialdir = "Desktop", title = "Document", filetypes = (("Document", "*.*"), ("all files", "*.*")))
    pdf_file = os.path.abspath(pdf_file)
    pdf_files.append(pdf_file)

def sendpdf():
    document_sent = 0
    for pdf in pdf_files:
        if os.path.exists(pdf):
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span").click()
            time.sleep(1)
            file = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[4]/button/input")
            file.send_keys(pdf)
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div").click()
            time.sleep(5)
            document_sent = document_sent + 1
            print(f"{document_sent} document sent")

input("Press Enter to open Numbers List without country code ")
contact_list = filedialog.askopenfilename(initialdir = "Desktop", title = "Number List", filetypes = (("TXT File", "*.txt"), ("all files", "*.*")))
contact_list = os.path.abspath(contact_list)
number = open(contact_list, "r")
driver = webdriver.Firefox()
for x in number:
    url = "https://web.whatsapp.com/send?phone=%2B+91" + x + "&text&app_absent=0"
    driver.get(url)
    element_present = EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span"))
    WebDriverWait(driver, 90).until(element_present)
    time.sleep(2)
    sendpdf()
    print("Selected Document sent to " + x)
