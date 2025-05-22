import csv
import statistics
from utils.logger import Logger

def analyze_emissions_full(file_path):

    logger = Logger()
    logger.info("Analyzing CO₂ emissions...")
    
    # User input
    logger.info("Enter the country name (Entity):", end=' ')
    entity = input().strip()
    emissions_data = []

    try:
        # Read and collect data
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Entity'] == entity and row['Annual CO₂ emissions']:
                    try:
                        year = int(row['Year'])
                        emissions = float(row['Annual CO₂ emissions'])
                        emissions_data.append((year, emissions))
                    except ValueError:
                        continue

        if not emissions_data:
            logger.warning(f"No valid CO₂ emission records found for {entity}.")
            return

        # Sort by year
        emissions_data.sort(key=lambda x: x[0])
        all_years = [y for y, _ in emissions_data]
        all_values = [v for _, v in emissions_data]

        # Year range
        first_year = min(all_years)
        last_year = max(all_years)

        # Full range min/max
        full_min_year, full_min_val = min(emissions_data, key=lambda x: x[1])
        full_max_year, full_max_val = max(emissions_data, key=lambda x: x[1])

        # Last 10 years stats
        last_10_data = sorted(emissions_data, key=lambda x: x[0], reverse=True)[:10]
        last10_years = [y for y, _ in last_10_data]
        last10_values = [v for _, v in last_10_data]

        if len(last10_values) >= 2:
            last10_avg = statistics.mean(last10_values)
            last10_std = statistics.stdev(last10_values)
            last10_min_year, last10_min_val = min(last_10_data, key=lambda x: x[1])
            last10_max_year, last10_max_val = max(last_10_data, key=lambda x: x[1])
        else:
            last10_avg = last10_std = last10_min_val = last10_max_val = None

        # Output
        print(f"\n📊 CO₂ Emissions Analysis for {entity}")
        print(f"🕒 Data available from {first_year} to {last_year}")

        print("\n📈 Last 10 Years:")
        if last10_avg is not None:
            print(f"   ▪️ Lowest: {last10_min_val:,.0f} tons in {last10_min_year}")
            print(f"   ▪️ Highest: {last10_max_val:,.0f} tons in {last10_max_year}")
            print(f"   ▪️ Average: {last10_avg:,.0f} tons")
            print(f"   ▪️ Std Dev: {last10_std:,.0f} tons")
        else:
            print("   ⚠️ Not enough data for last 10 years.")

        print("\n📜 All Years:")
        print(f"   ▪️ Lowest: {full_min_val:,.0f} tons in {full_min_year}")
        print(f"   ▪️ Highest: {full_max_val:,.0f} tons in {full_max_year}\n")

    except FileNotFoundError:
        logger.error("❌ CSV file not found. Please check the file path.")
    except Exception as e:
        logger.error(f"❌ An unexpected error occurred: {e}")

