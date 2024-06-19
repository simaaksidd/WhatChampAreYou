from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://op.gg/champions')

wait = WebDriverWait(driver, 10) 

xpath_expression = "//table[contains(@class, 'css-f65xnu') and contains(@class, 'e8rg48x1')]"

table = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_expression)))
rows = table.find_elements(By.TAG_NAME, 'tr')
data = []
for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')
    row_data = []
    for idx, col in enumerate(columns):
        if idx == 0:
            rank = col.text
            row_data.append(f'Rank: {rank}')
        elif idx == 1:
            champ = col.text
            row_data.append(f'{champ}')
        elif idx == 2:
            tier = col.text
            row_data.append(f'Tier: {tier}')
        elif idx == 3:  
            img = col.find_elements(By.TAG_NAME, 'img') 
            alt = img[0].get_attribute('alt')
            row_data.append(f'{alt}') 
        elif idx == 4:
            wr = col.text
            row_data.append(f'Win Rate: {wr}')
        elif idx == 5:
            pr = col.text
            row_data.append(f'Pick Rate: {pr}')
        elif idx == 6:
            br = col.text
            row_data.append(f'Ban Rate: {br}')
        elif idx == 7:
            c = []
            champs = col.find_elements(By.TAG_NAME, 'img')
            for i in range(3):
                c.append(champs[i].get_attribute('alt'))
            counters = ', '.join(c)
            row_data.append(f'Counters: {counters}')
        
    data.append(row_data)

df = pd.DataFrame(data)
csv_file_path = '/Users/simaa/Documents/opggbot/data.csv'
df.to_csv(csv_file_path, index=False)

driver.quit()