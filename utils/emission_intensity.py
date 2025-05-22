import csv
import matplotlib.pyplot as plt
from utils.logger import Logger
from matplotlib.ticker import FuncFormatter

def billions_formatter(x, pos):
    return f'{x / 1e9:.2f}B'

def is_valid_country(name):
    # Sadece harf ve boşluk kabul et
    return all(c.isalpha() or c.isspace() for c in name)

def per_capita_emission(emission_csv_path, population_csv_path):
    logger = Logger()
    logger.info("Starting per capita emission calculation...")
    
    while True:
        logger.info("Enter the country name:", end=' ')
        country_input = input().strip()
        if is_valid_country(country_input) and len(country_input) > 0:
            country_input_lower = country_input.lower()
            break
        else:
            logger.error("❌ Invalid country name. Please enter letters and spaces only.")

    while True:
        logger.info("Enter the year:", end=' ')
        year_input = input().strip()
        if year_input.isdigit():
            year_input = int(year_input)
            break
        else:
            logger.error("❌ Invalid year. Please enter numeric digits only.")

    emission_value = None
    population_value = None

    try:
        # Emission verisini oku
        with open(emission_csv_path, 'r', encoding='utf-8') as f_emis:
            reader = csv.reader(f_emis)
            next(reader)  # header atla

            for row in reader:
                entity = row[0].strip().lower()
                try:
                    year = int(row[2].strip())
                    emission = float(row[3].strip())
                except:
                    continue

                if entity == country_input_lower and year == year_input:
                    emission_value = emission
                    break

        # Nüfus verisini oku
        with open(population_csv_path, 'r', encoding='utf-8') as f_pop:
            reader = csv.reader(f_pop)
            next(reader)  # header atla

            for row in reader:
                entity = row[0].strip().lower()
                try:
                    year = int(row[2].strip())
                    population = int(row[3].strip())
                except:
                    continue

                if entity == country_input_lower and year == year_input:
                    population_value = population
                    break

        # Kontroller
        if emission_value is None:
            logger.error(f"❌ No emission data found for {country_input.title()} in {year_input}.")
            return
        if population_value is None or population_value == 0:
            logger.error(f"❌ No valid population data found for {country_input.title()} in {year_input}.")
            return

        # Kişi başına emisyon hesapla (ton / kişi)
        per_capita = emission_value / population_value

        logger.info(f"✅ {country_input.title()}’s CO₂ emission per capita in {year_input}: {per_capita:.6f} tons per person")

        # Grafik
        plt.figure(figsize=(6, 4))
        plt.bar(country_input.title(), per_capita, color='green')
        plt.title(f"Per Capita CO₂ Emission in {year_input}")
        plt.ylabel("Tons per person")
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError as e:
        logger.error(f"❌ File not found: {e.filename}")
    except Exception as e:
        logger.error(f"❌ An error occurred: {e}")
