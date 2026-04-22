from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser setup
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# fetching website
driver.get("https://www.smartprix.com/mobiles")

# wait until products appear
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sm-product")))

# loading products
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    try:
        # click Load
        load_more = driver.find_element(By.XPATH, "//div[contains(text(),'Load More')]")
        load_more.click()
        time.sleep(2)
    except:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

print("All products loaded")

# saving html content
html = driver.page_source

# saving html file
with open("smartprix.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML saved successfully")