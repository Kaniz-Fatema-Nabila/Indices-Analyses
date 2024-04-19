from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def main():
    website= ("https://www.investing.com/indices/world-indices")
    driver= webdriver.Chrome()
    driver.get(website)

    # Hover over the "Markets" dropdown and "commodities"dropdowns 
    markets_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navMenu"]/ul/li[1]/a')))
    action = ActionChains(driver)
    action.move_to_element(markets_dropdown).perform()

    commodities_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="navMenu"]/ul/li[1]/ul/li[3]/a')))
    action.move_to_element(commodities_dropdown).perform()

    # Find and click on the "Real Time Commodities" option
    real_time_commodities_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navMenu"]/ul/li[1]/ul/li[3]/div/ul[1]/li[1]/a')))
    real_time_commodities_option.click()

    # Initialize empty lists to store data
    cfi_data=[]
    cfi_perf_data=[]
    cfi_tech_data=[]
    cfi_country_names=[]

    # Extract Commodity Future Indices Price Data
    cfi_rows= driver.find_elements(By.CLASS_NAME,"datatable-v2_row__hkEus")[1: ]
    cfi_column=["Name", "Month","Last", "High","Low", "Chg.", "Chg%", "Date/Time"]
    for cfi_row in cfi_rows:
        cfi_cells = cfi_row.find_elements(By.CLASS_NAME,"datatable-v2_cell__IwP1U")[1:]

        cfi_row_data = {}
        for index, cfi_cell in enumerate(cfi_cells):
            cfi_row_data[cfi_column[index]] = cfi_cell.text
        
        cfi_data.append(cfi_row_data)

    # Click on the "Perfomance" option
    cfi_performance= driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/button[2]')
    cfi_performance.click()

    # Extract Commodity Future Indices Performances Data
    cfi_perf_rows= driver.find_elements(By.CLASS_NAME,"datatable-v2_row__hkEus")[1:]

    cfi_perf_column=["Name", "Daily%", "1 Week%","1 Month%", "YTD%", "1 Year%", "3 Years%"]

    for cfi_perf_row in cfi_perf_rows:
        cfi_perf_cells = cfi_perf_row.find_elements(By.CLASS_NAME,"datatable-v2_cell__IwP1U")[1:]

        cfi_perf_row_data = {}
        for index, cfi_perf_cell in enumerate(cfi_perf_cells):
            cfi_perf_row_data[cfi_perf_column[index]] = cfi_perf_cell.text
        
        cfi_perf_data.append(cfi_perf_row_data)

    # Extract Commodity Future Indices Technical Data
    cfi_technical= driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/button[3]')
    cfi_technical.click()
    cfi_tech_rows= driver.find_elements(By.CLASS_NAME,"datatable-v2_row__hkEus")[1:]

    cfi_tech_column=["Name", "Hourly", "Daily","Weekly", "Monthly"]

    for cfi_tech_row in cfi_tech_rows:
        cfi_tech_cells = cfi_tech_row.find_elements(By.CLASS_NAME,"datatable-v2_cell__IwP1U")[1:]

        cfi_tech_row_data = {}
        for index, cfi_tech_cell in enumerate(cfi_tech_cells):
            cfi_tech_row_data[cfi_tech_column[index]] = cfi_tech_cell.text
        
        cfi_tech_data.append(cfi_tech_row_data)

    # Extract country names
    cfi_country_elements = driver.find_elements(By.CLASS_NAME,"flag_flag__gUPtc")[1:]
    cfi_country_names = [element.get_attribute("title") for element in cfi_country_elements]

    driver.close()

    #Convert into DataFrames
    cfi_df=pd.DataFrame(cfi_data, columns=cfi_column)
    cfi_df.insert(0, 'Country', cfi_country_names)
    
    cfi_perf_df=pd.DataFrame(cfi_perf_data, columns=cfi_perf_column)
    cfi_perf_df.insert(0, 'Country', cfi_country_names)
    
    cfi_tech_df=pd.DataFrame(cfi_tech_data,columns=cfi_tech_column)
    cfi_tech_df.insert(0, 'Country', cfi_country_names)
    
    #Convert into CSV files
    cfi_df.to_csv("Commodity_Future_Indices_Price.csv",index=False)
    cfi_perf_df.to_csv("Commodity_Future_Indices_Performance.csv",index=False)
    cfi_tech_df.to_csv("Commodity_Future_Indices_Technique.csv",index=False)

    return

if __name__ == "__main__":
    main()

