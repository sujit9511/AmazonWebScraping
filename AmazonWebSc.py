from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd


driver = webdriver.Edge("../msedgedriver.exe")

driver.get("https://amazon.in/")


driver.maximize_window()
time.sleep(2)


driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(
    "samsung galaxy s23 ultra", Keys.ENTER
)
time.sleep(2)

element = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span'
driver.find_element(By.XPATH, element).click()

time.sleep(1)

driver.switch_to.window(driver.window_handles[1])

time.sleep(2)


table = driver.find_element(By.XPATH, '//*[@id="productDetails_techSpec_section_1"]')

driver.execute_script("arguments[0].scrollIntoView();", table)


time.sleep(2)


df = pd.read_html(table.get_attribute("outerHTML"))[0]

time.sleep(2)

df.to_csv("product_details.csv", index=False)


# time.sleep(2)


time.sleep(3)
driver.quit()
