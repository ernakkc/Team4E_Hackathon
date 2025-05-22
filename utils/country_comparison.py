import csv
import matplotlib.pyplot as plt
from utils.logger import Logger
from matplotlib.ticker import FuncFormatter

def millions_formatter(x, pos):
    return f'{x / 1e6:.2f}M'

def compare_two_countries(csv_path):
    logger = Logger()
    logger.info("Starting CO₂ emission comparison between two countries...")

    try:
        year = int(input("Enter the year for comparison: "))
        country1 = input("Enter the name of the first country: ").strip()
        country2 = input("Enter the name of the second country: ").strip()

        emissions = {country1: None, country2: None}

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Entity"] in emissions and row["Year"] == str(year):
                    emission_str = row["Annual CO₂ emissions"]
                    if emission_str:
                        try:
                            emissions[row["Entity"]] = float(emission_str)
                        except ValueError:
                            continue

        if emissions[country1] is None or emissions[country2] is None:
            logger.warning("Emission data for one or both countries is missing for the specified year.")
            return

        logger.info(f"{country1} ({year}): {emissions[country1]:,.0f} tons")
        logger.info(f"{country2} ({year}): {emissions[country2]:,.0f} tons")
        logger.info("Generating comparison chart...")

        # Bar chart
        plt.figure(figsize=(8, 5))
        plt.bar([country1, country2], [emissions[country1], emissions[country2]], color=['#1f77b4', '#ff7f0e'])
        plt.title(f"CO₂ Emissions Comparison in {year}")
        plt.ylabel("CO₂ Emissions (million tons)")
        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
    except ValueError:
        logger.error("Invalid input. Please enter numeric values for the year.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
