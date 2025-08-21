import os
from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
def download_latest_pdf():
    os.makedirs(DOWNLOAD_DIR , exist_ok=True)

    options = Options()
    prefs = {"download.default_directory":DOWNLOAD_DIR}
    options.add_experimental_option("prefs",prefs)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://nrldc.in/daily/daily-psp-report"

        driver.get(url)
        time.sleep(5)

        pdf_link = driver.find_element(By.CSS_SELECTOR, "td a[href$='.pdf']")
        pdf_url = pdf_link.get_attribute("href")

        driver.get(pdf_url)
        time.sleep(10)
    finally:
        driver.quit()

    for f in os.listdir(DOWNLOAD_DIR):
        if f.endswith(".pdf"):
            return os.path.join(DOWNLOAD_DIR, f)
    return None



