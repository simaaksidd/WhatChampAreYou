from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

URL = 'https://lor.gg/en/cards'

traits_xp = "//div[contains(@class, 'absolute') and contains(@class, 'top-[-10px]') and \
            contains(@class, 'right-0') and contains(@class, 'flex') and \
            contains(@class, 'pr-[2px]') and contains(@class, 'css-184s4zu')]"

items_xp = "//div[contains(@class, 'absolute') and contains(@class, 'right-0') and \
            contains(@class, 'flex') and contains(@class, 'justify-center') and \
            contains(@class, 'left-[-1px]') and contains(@class, 'bottom-[-7px]')]"

avp_xp = "//div[contains(@class, 'text-right') and contains(@class, 'w-[34px]') and \
            contains(@class, 'css-1thou9h')]"

button_xp = '//button[@data-v-ab8b99a4=""]'

options = Options()
options.add_argument("--headless=new") 
driver = webdriver.Chrome(options=options)

driver.get(URL)

wait = WebDriverWait(driver, 5)

button = wait.until(EC.visibility_of_element_located((By.XPATH, button_xp)))

button.click()



data = []

df = pd.DataFrame(data)
csv_file_path = '/Users/simaa/Documents/opggbot/lordata.csv'
df.to_csv(csv_file_path, index=False)

driver.quit()
