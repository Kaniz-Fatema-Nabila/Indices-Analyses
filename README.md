# Indices-Analyses

## Problem statement:
The project aims to collect data of the indices of different categories of market from [this website](https://www.investing.com/indices/world-indices).
Then the collected data is utilized to analyze the market indices and visualize the following correlations using Tableau Dashboards:

1. Analyze the geographical distribution of indices. Compare indices from different region and visualize them.
2. Major world market indices and their performance over time. Visualize how indices changed over days, months and years.
3. Analyze future indices and visualize their performance over days, months and years.
4. Analyze the real time commodity futures prices, their performances and technique and visualize with charts.

You can visit the following dashboards here:
1. [World Indices](https://public.tableau.com/app/profile/kaniz.fatema.nabila/viz/WorldIndices_17132836521760/Dashboard1)
2. [Major Indices](https://public.tableau.com/app/profile/kaniz.fatema.nabila/viz/MajorIndices/Dashboard1)
3. [Indices Future](https://public.tableau.com/app/profile/kaniz.fatema.nabila/viz/IndicesFuture/Dashboard1)
4. [Commodity Future Indices](https://public.tableau.com/app/profile/kaniz.fatema.nabila/viz/CommodityFutureIndices/Dashboard1)

## Build from sources
1. Clone the repository
   ```bash
   https://github.com/Kaniz-Fatema-Nabila/Indices-Analyses.git
   ```
2. Initialize and activate virtual environment
   ```bash
   vitual --no-site-packages venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install selenium
   pip install pandas
   ```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads
5. Run the scrapers
   -world_indices
   ```bash
   python web_scraping/world_indices.py
   ```
   -major_indices
    ```bash
   python web_scraping/major_indices.py
   ```
     -indices_future
    ```bash
   python web_scraping/indices_future.py
   ```
     -commodity_future
    ```bash
   python web_scraping/commodity_future.py
   ```
6. You will get the scrapped data in the CSV files

      
