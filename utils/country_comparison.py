import csv
import matplotlib.pyplot as plt
from utils.logger import Logger
from matplotlib.ticker import FuncFormatter

def millions_formatter(x, pos):
    return f'{x / 1e6:.2f}M'

def countries_within_emission_range(csv_path):
    logger = Logger()
    logger.info("Starting the analysis of CO₂ emissions within a specified range.")
    try:
        logger.info("Enter the year and the range of CO₂ emissions to analyze:", end=' ')
        year = int(input())

        while True:
            logger.info("Enter the minimum CO₂ emission value in Million tons:", end=' ')
            min_val = float(input())*1000000
            if min_val < 0:
                logger.error("Minimum value cannot be negative. Try again.")
                continue
            logger.info("Enter the maximum CO₂ emission value in Million tons:", end=' ')
            max_val = float(input())* 1000000
            if max_val < min_val:
                logger.error("Maximum value cannot be smaller than the minimum. Try again.")
            else:
                break

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            selected_data = []

            for row in reader:
                if not row["Annual CO₂ emissions"]:
                    continue
                try:
                    row_year = int(row["Year"])
                    emission = float(row["Annual CO₂ emissions"])
                except ValueError:
                    continue

                if row_year == year and min_val <= emission <= max_val:
                    entity = row["Entity"]
                    if entity not in ["World", "High-income countries", "EU-27", "Non-OECD countries", "Asia", "Europe", "Africa"]:
                        selected_data.append((entity, emission))

        if not selected_data:
            logger.warning(f"No countries found with CO₂ emissions between {min_val:,.0f} and {max_val:,.0f} tons in {year}.")
            return

        selected_data.sort(key=lambda x: x[1], reverse=True)

        logger.info(f"Countries with CO₂ emissions between {min_val:,.0f} and {max_val:,.0f} tons in {year}:")
        for entity, emission in selected_data:
            logger.info(f"{entity}: {emission:,.0f} tons")
        logger.info("Plotting the data...")

        countries = [item[0] for item in selected_data]
        emissions = [item[1] for item in selected_data]

        plt.figure(figsize=(12, 6))
        plt.bar(countries, emissions, color='skyblue')
        plt.title(f"CO₂ Emissions Between {min_val:,.0f} and {max_val:,.0f} Tons in {year}")
        plt.xlabel("Countries")
        plt.ylabel("CO₂ Emissions (million tons)")
        plt.xticks(rotation=45, ha='right', fontsize=9)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.tight_layout()
        plt.grid(True, axis='y', linestyle='--', alpha=0.5)
        plt.show()

    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
    except ValueError:
        logger.error("Invalid input. Please enter numeric values for year and emissions.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
