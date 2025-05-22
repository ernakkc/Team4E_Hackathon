import csv
import matplotlib.pyplot as plt
from utils.logger import Logger
from matplotlib.ticker import FuncFormatter

def billions_formatter(x, pos):
    return f'{x / 1e9:.2f}B'

def emission_difference(csv_path):
    logger = Logger()
    try:
        logger.info("Starting emission difference calculation...")
        logger.info("Enter the country name:", end=' ')
        country_input = input().strip().lower()
        logger.info("Enter the first year:", end=' ')
        year1 = int(input())
        logger.info("Enter the second year:", end=' ')
        year2 = int(input())

        emission_year1 = None
        emission_year2 = None

        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)

            normalized_headers = [h.strip().lower().replace(' ', '').replace('₂','2') for h in headers]
            idx_entity = normalized_headers.index('entity')
            idx_year = normalized_headers.index('year')
            idx_emission = normalized_headers.index('annualco2emissions')

            for row in reader:
                entity = row[idx_entity].strip().lower()
                try:
                    year = int(row[idx_year].strip())
                    emission = float(row[idx_emission].strip())
                except:
                    continue

                if entity == country_input:
                    if year == year1:
                        emission_year1 = emission
                    elif year == year2:
                        emission_year2 = emission

        if emission_year1 is None:
            logger.error(f"No data found for {country_input.title()} in {year1}.")
            return
        if emission_year2 is None:
            logger.error(f"No data found for {country_input.title()} in {year2}.")
            return

        diff = emission_year2 - emission_year1
        pct_change = (diff / emission_year1) * 100 if emission_year1 != 0 else 0

        logger.info(f"CO₂ emissions for {country_input.title()} in {year1}: {emission_year1:,.0f} tons")
        print(f"\nCO₂ emissions for {country_input.title()}:")
        print(f"{year1}: {emission_year1:,.0f} tons")
        print(f"{year2}: {emission_year2:,.0f} tons")
        print(f"Difference: {diff:,.0f} tons")
        print(f"Percentage change: {pct_change:.2f}%")

        # Grafik için
        years = [year1, year2]
        emissions = [emission_year1, emission_year2]

        plt.figure(figsize=(7,5))
        plt.bar([str(year) for year in years], emissions, color=['blue', 'orange'])
        plt.title(f"CO₂ Emissions for {country_input.title()}: {year1} vs {year2}")
        plt.ylabel("CO₂ Emissions (Tons)")
        plt.gca().yaxis.set_major_formatter(FuncFormatter(billions_formatter))
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    except ValueError:
        logger.error("Invalid input. Please enter numeric values for years.")
    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
