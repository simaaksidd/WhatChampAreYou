from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

URL = 'https://tactics.tools/units'

traits_xp = "//div[contains(@class, 'absolute') and contains(@class, 'top-[-10px]') and \
            contains(@class, 'right-0') and contains(@class, 'flex') and \
            contains(@class, 'pr-[2px]') and contains(@class, 'css-184s4zu')]"

items_xp = "//div[contains(@class, 'absolute') and contains(@class, 'right-0') and \
            contains(@class, 'flex') and contains(@class, 'justify-center') and \
            contains(@class, 'left-[-1px]') and contains(@class, 'bottom-[-7px]')]"

avp_xp = "//div[contains(@class, 'text-right') and contains(@class, 'w-[34px]') and \
            contains(@class, 'css-1thou9h')]"

champs_xp = "//div[contains(@class, 'flex') and \
                    contains(@class, 'flex-col') and contains(@class, 'gap-6')]"

options = Options()
options.add_argument("--headless=new")  # Use 'new' for the latest headless mode
driver = webdriver.Chrome(options=options)

driver.get(URL)

wait = WebDriverWait(driver, 5)

champs = wait.until(EC.visibility_of_element_located((By.XPATH, champs_xp)))

costs = champs.find_elements(By.CLASS_NAME, 'css-aykz05')

data = []

i = 0
for cost in costs:
    units = cost.find_elements(By.CLASS_NAME, 'no-webkit-preview')
    row_data = []
    for unit in units:
        name = unit.get_attribute('href')[28:]
        
        avp = unit.find_elements(By.XPATH, avp_xp)[i].text

        traits_list = []
        trait_container = unit.find_elements(By.XPATH, traits_xp)
        traits = trait_container[i].find_elements(By.TAG_NAME, 'image')
        for trait in traits:
            traits_list.append(trait.get_attribute('href')[46:-6])
        if not traits_list:
            traits_list.append('NA')
        
        items_list = []
        items_container = unit.find_elements(By.XPATH, items_xp)
        items = items_container[i].find_elements(By.TAG_NAME, 'img')
        for item in items:
            items_list.append(item.get_attribute('alt'))
        if not items_list:
            items_list.append('NA')

        i += 1
        data.append([name, avp, ', '.join(traits_list), ', '.join(items_list)])

df = pd.DataFrame(data)
csv_file_path = '/Users/simaa/Documents/opggbot/tftdata.csv'
df.to_csv(csv_file_path, index=False)

driver.quit()
