import csv
from tabulate import tabulate 
from utils.logger import Logger

def analyze_co2_trends(csv_file_path):
    logger = Logger()

    logger.info("Analyzing CO2 emission trends...")

    country_data = {}
    
    logger.info("Enter target country name (e.g., 'United States'):")
    target_country = input().strip()

    logger.info(f"Starting CO2 emission trend analysis for '{target_country}'...")


    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        try:
            entity_idx = header.index('Entity')
            year_idx = header.index('Year')
            emissions_idx = header.index('Annual CO₂ emissions')
        except ValueError as e:
            logger.error(f"Error: Expected columns not found in CSV headers. Please ensure 'Entity', 'Year', and 'Annual CO₂ emissions' columns exist. Error: {e}")
            return

        for row in reader:
            try:
                entity = row[entity_idx]
                if entity != target_country:
                    continue

                year = int(row[year_idx])
                emissions_str = row[emissions_idx]
                emissions = float(emissions_str) if emissions_str else 0.0

                if entity not in country_data:
                    country_data[entity] = {}
                country_data[entity][year] = emissions
            except (ValueError, IndexError) as e:
                logger.error(f"Error: Problem processing row '{row}'. Error: {e}")
                continue

    target_years = [2021, 2022, 2023]
    years_data = country_data.get(target_country)

    if not years_data:
        logger.warning(f"No data found for '{target_country}'.")
        return

    emissions = [years_data.get(year) for year in target_years]

    if all(e is not None for e in emissions):
        if emissions[0] <= emissions[1] <= emissions[2]:
            trend = "Continuous Increase"
        elif emissions[0] >= emissions[1] >= emissions[2]:
            trend = "Continuous Decrease"
        else:
            trend = "Variable Trend"
    else:
        trend = "Insufficient data (for the last 3 years)"

    # Tabloyu yazdır
    print(tabulate([[target_country, trend]], headers=["Country", "CO2 Emission Trend (Last 3 Years)"], tablefmt="grid"))
