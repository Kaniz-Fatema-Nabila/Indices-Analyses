from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def main():
    website = "https://www.investing.com/indices/world-indices"
    driver = webdriver.Chrome()
    driver.get(website)
    
    # Find all tables containing world indices data
    wi_tables = driver.find_elements(By.CLASS_NAME, 'genTbl')[0:93]
    
    # Initialize lists to store data
    wi_data = []
    wi_country_names = []

    # Extract World Indices Data
    for wi_table in wi_tables:
        wi_rows = wi_table.find_elements(By.TAG_NAME, "tr")[1:]

        wi_column_names = ["Indices", "Last", "High", "Low", "Chg.", "Chg%", "Date/Time"]

        for wi_row in wi_rows:
            wi_cells = wi_row.find_elements(By.TAG_NAME, "td")[1:-1]
        
            wi_row_data = {}
            for index, wi_cell in enumerate(wi_cells):
                wi_row_data[wi_column_names[index]] = wi_cell.text
            
            wi_data.append(wi_row_data)

    # Extract country names
    wi_country_elements = driver.find_elements(By.CLASS_NAME,"ceFlags")[39:]
    wi_country_names = [element.get_attribute("title") for element in wi_country_elements]

    driver.close()

    # Convert into DataFrame
    wi_data_df = pd.DataFrame(wi_data, columns=wi_column_names)

    # Add country names to the DataFrame
    wi_data_df.insert(0, 'Country', wi_country_names)

    # Convert into CSV file
    wi_data_df.to_csv("World_Indices.csv", index=False)

    return

if __name__ == "__main__":
    main()
