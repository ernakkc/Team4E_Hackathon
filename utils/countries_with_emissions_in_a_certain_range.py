import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from utils.logger import Logger

def millions_formatter(x, pos):
    return f'{x / 1e6:.2f}M'

def countries_within_emission_range_emission(csv_path):
    logger = Logger()
    
    try:
        logger.info("Starting the analysis of CO₂ emissions within a specified range.")
        logger.info("Enter the year and the range of CO₂ emissions to analyze:", end=' ')
        year = int(input())
        
        while True:
            logger.info("Enter the minimum CO₂ emission value in million tons:", end=' ')
            min_emission = float(input())*1000000
            if min_emission < 0:
                logger.error("Minimum value cannot be negative, try again.")
                continue
            logger.info("Enter the maximum CO₂ emission value in million tons:", end=' ')
            max_emission = float(input())*1000000
            if max_emission < min_emission:
                logger.error("Maximum value cannot be smaller than the minimum, try again.")
            else:
                break
        
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            results = []
            excluded_entities = ["World", "High-income countries", "EU-27", "Non-OECD countries", "Asia", "Europe", "Africa"]
            
            for row in reader:
                if not row["Annual CO₂ emissions"]:
                    continue
                try:
                    row_year = int(row["Year"])
                    emission = float(row["Annual CO₂ emissions"])
                except ValueError:
                    continue
                
                if row_year == year and min_emission <= emission <= max_emission:
                    entity = row["Entity"]
                    if entity not in excluded_entities:
                        results.append((entity, emission))
        
        if not results:
            logger.warning(f"No countries found with CO₂ emissions between {min_emission:,.0f} and {max_emission:,.0f} tons in {year}.")
            return
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        logger.info(f"Countries with CO₂ emissions between {min_emission:,.0f} and {max_emission:,.0f} tons in {year}:")
        for entity, emission in results:
            print(f" - {entity}: {emission:,.0f} tons")
        
        countries = [item[0] for item in results]
        emissions = [item[1] for item in results]
        
        plt.figure(figsize=(12, 6))
        plt.bar(countries, emissions, color='skyblue')
        plt.title(f"CO₂ Emissions between {min_emission:,.0f} and {max_emission:,.0f} tons in {year}")
        plt.xlabel("Country")
        plt.ylabel("CO₂ Emissions (million tons)")
        plt.xticks(rotation=45, ha='right', fontsize=9)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}. Please check the file path.")
    except ValueError:
        logger.error("Invalid input! Please enter a valid year and emission values.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

