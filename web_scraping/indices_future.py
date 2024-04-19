from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def main():
    website = "https://www.investing.com/indices/world-indices"
    driver = webdriver.Chrome()
    driver.get(website)

    # Click on the "Indices Futures" tab
    indices_futures_tab = driver.find_element(By.XPATH, '//*[@id="subNav"]/ul/li[4]')
    indices_futures_tab.click()

    # Initialize empty lists to store data
    fi_data = []
    fi_perf_data = []

    # Extract Indices Futures Price Data
    fi_tables = driver.find_elements(By.CLASS_NAME, "datatable-v2_table__93S4Y")[0:1]
    for fi_table in fi_tables:
        fi_rows = fi_table.find_elements(By.CLASS_NAME, "datatable-v2_row__hkEus")[1:]

        fi_column_names = ["Name","Month","Last", "High", "Low", "Chg.", "Chg%", "Date/Time"]
    
        for fi_row in fi_rows:
            fi_cells = fi_row.find_elements(By.TAG_NAME, "td")[1:]
        
            fi_row_data = [fi_cell.text for fi_cell in fi_cells]
            fi_data.append(fi_row_data)

    #Extract Indices Futures Performance Data
    fi_performance = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[1]/button[2]')
    fi_performance.click()

    #fi_perf_tables = driver.find_elements(By.CLASS_NAME, "datatable-v2_table__93S4Y")[0:1]
    for fi_table in fi_tables:
        fi_perf_rows = fi_table.find_elements(By.CLASS_NAME, "datatable-v2_row__hkEus")[1:]

        fi_perf_column = ["Name", "Daily%", "1 week%", "1 Month%", "YTD%", "1 Year%", "3 Years%"]

        for fi_perf_row in fi_perf_rows:
            fi_perf_cells = fi_perf_row.find_elements(By.CLASS_NAME, "datatable-v2_cell__IwP1U")[1:]

            fi_perf_row_data = [fi_perf_cell.text for fi_perf_cell in fi_perf_cells]
            fi_perf_data.append(fi_perf_row_data)

    # Extract country names
    for fi_table in fi_tables:
        fi_country_elements = fi_table.find_elements(By.CLASS_NAME, "flag_flag__gUPtc")

        fi_country_names = [element.get_attribute("title") for element in fi_country_elements]

    driver.close()

    # Convert into DataFrames
    fi_df = pd.DataFrame(data=fi_data, columns=fi_column_names)
    fi_df.insert(0, 'Country', fi_country_names)
    
    fi_perf = pd.DataFrame(data=fi_perf_data, columns=fi_perf_column)
    fi_perf.insert(0, 'Country', fi_country_names)

    #Convert into CSV file
    fi_df.to_csv("Indices_Future_Price.csv", index=False)
    fi_perf.to_csv("Indices_Future_Performance.csv", index=False)

    return

if __name__ == "__main__":
    main()
