from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def main():
    website= ("https://www.investing.com/indices/world-indices")
    driver= webdriver.Chrome()
    driver.get(website)

    # Click on the "Major World Market Indices" tab
    major_indices_tab = driver.find_element(By.XPATH, '//*[@id="subNav"]/ul/li[2]/a')
    major_indices_tab.click()

    # Initialize empty lists to store data
    mi_data = []
    mi_perf_data=[]
    mi_country_names = []

    # Extract Major Indices Price Data
    mi_rows= driver.find_elements(By.CLASS_NAME,"datatable-v2_row__hkEus")[1: ]

    mi_column=["Name", "Last", "High","Low", "Chg.", "Chg%", "Date/Time"]

    for mi_row in mi_rows:
        mi_cells = mi_row.find_elements(By.CLASS_NAME,"datatable-v2_cell__IwP1U")[1:]

        mi_row_data = {}
        for index, mi_cell in enumerate(mi_cells):
            mi_row_data[mi_column[index]] = mi_cell.text
        
        mi_data.append(mi_row_data)

    # Extract Major Indices Performance data
    mi_performance= driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/button[2]')
    mi_performance.click()
    mi_perf_rows= driver.find_elements(By.CLASS_NAME,"datatable-v2_row__hkEus")[1: ]

    mi_perf_column=["Name", "Daily%", "1 Week%","1 Month%", "YTD%", "1 Year%", "3 Years%"]

    for mi_perf_row in mi_perf_rows:
        mi_perf_cells = mi_perf_row.find_elements(By.CLASS_NAME,"datatable-v2_cell__IwP1U")[1:]

        mi_perf_row_data = {}
        for index, mi_perf_cell in enumerate(mi_perf_cells):
            mi_perf_row_data[mi_perf_column[index]] = mi_perf_cell.text
        
        mi_perf_data.append(mi_perf_row_data)

    
    # Extract country names
    mi_country_elements = driver.find_elements(By.CLASS_NAME,"flag_flag__gUPtc")[1:]
    mi_country_names = [element.get_attribute("title") for element in mi_country_elements]

    driver.close()

    # Convert into DataFrames
    mi_df = pd.DataFrame(mi_data, columns=mi_column)
    mi_df.insert(0, 'Country', mi_country_names)

    mi_perf_df = pd.DataFrame(mi_perf_data, columns=mi_perf_column)
    mi_perf_df.insert(0, 'Country', mi_country_names)
    
    # Convert into CSV files
    mi_df.to_csv("Major_Future_Indices_Price.csv", index=False)
    mi_perf_df.to_csv("Major_Future_Indices_Performance.csv", index=False)

    return

if __name__ == "__main__":
    main()