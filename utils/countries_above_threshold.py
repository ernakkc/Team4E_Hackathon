import csv
from utils.logger import Logger
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def countries_above_threshold(csv_path):
    """
    This function reads a CSV file containing CO₂ emissions data and filters countries
    that emitted more than a specified threshold in a given year. It then displays
    the results in a bar chart.
    :param csv_path: Path to the CSV file containing CO₂ emissions data.
    """
    logger = Logger()
    logger.info("Countries Emitting More Than a Specified Threshold in a Given Year")
    
    def billions_formatter(x, pos):
        if x >= 1e9:
            return f"{x/1e9:.2f}B"
        elif x >= 1e6:
            return f"{x/1e6:.0f}M"
        elif x >= 1e3:
            return f"{x/1e3:.0f}K"
        else:
            return f"{int(x)}"

    try:
        logger.info("Enter the year to analyze:", end="")
        year = int(input())
        logger.info("Enter the CO₂ emission threshold (in billion tons):", end="")
        threshold_billion = float(input())
        if threshold_billion <= 0:
            logger.error("Threshold must be a positive number.")
            return
        threshold_ton = threshold_billion * 1e9

        data = []
        unwanted_groups = {"world", "high-income countries", "eu-27", "non-oecd countries", "asia", "europe", "africa"}

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entity = row["Entity"].strip()
                entity_lower = entity.lower()
                y = int(row["Year"])
                emission_str = row.get("Annual CO₂ emissions", "").strip()

                if y == year and emission_str and entity_lower not in unwanted_groups:
                    emission = float(emission_str)
                    if emission > threshold_ton:
                        data.append((entity, emission))

        if not data:
            logger.info(f"No countries emitted more than {threshold_billion:.3f} billion tons CO₂ in {year}.")
            return

        # Sort descending by emission
        data.sort(key=lambda x: x[1], reverse=True)

        logger.info(f"Countries emitting more than {threshold_billion:.3f} billion tons CO₂ in {year}:")
        for country, emission in data:
            logger.info(f"{country}: {emission:,.0f} tons")

        countries, emissions = zip(*data)

        plt.figure(figsize=(12, 6))
        plt.bar(countries, emissions, color="orange")
        plt.title(f"Countries Emitting Over {threshold_billion:.3f} Billion Tons CO₂ in {year}")
        plt.xlabel("Countries")
        plt.ylabel("CO₂ Emissions (tons)")
        plt.xticks(rotation=45, ha='right', fontsize=9)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(billions_formatter))
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    except ValueError:
        logger.error("Invalid input! Please enter a valid year and threshold.")
    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}. Please check the file path.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
