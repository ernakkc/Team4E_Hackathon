import csv
import matplotlib.pyplot as plt
from utils.logger import Logger

def filter_and_sort_emissions_with_plot(file_path):
    logger = Logger()
    
    # Step 1: User input
    logger.info("Enter the country name (Entity):", end=' ')
    entity = input()
    if not entity:
        logger.error("❌ Invalid country name. Please enter a valid name.")
        return
    logger.info("Enter the start year (e.g., 2000):", end=' ')
    start_year = int(input())
    logger.info("Enter the end year (e.g., 2020):", end=' ')
    end_year = int(input())
    if start_year > end_year:
        logger.error("❌ Start year cannot be greater than end year.")
        return
    logger.info("Enter the sort order (asc/desc):", end=' ')
    order = input().strip().lower()

    reverse_sort = False
    if order == "desc":
        reverse_sort = True
    elif order != "asc":
        logger.error("❌ Invalid sort option. Use 'asc' or 'desc'.")
        return

    # Step 2: Read & filter
    emissions_filtered = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Entity'] == entity and row['Annual CO₂ emissions']:
                    try:
                        year = int(row['Year'])
                        if int(start_year) <= year <= int(end_year):
                            emissions = float(row['Annual CO₂ emissions'])
                            emissions_filtered.append((year, emissions))
                    except ValueError:
                        continue

        if not emissions_filtered:
            logger.warning(f"⚠️ No emission data found for {entity} between {start_year} and {end_year}.")
            return

        # Step 3: Sort
        sorted_data = sorted(emissions_filtered, key=lambda x: x[1], reverse=reverse_sort)

        # Step 4: Print output
        logger.info(f"📄 CO₂ Emissions for {entity} ({start_year} - {end_year}), sorted by emissions ({'descending' if reverse_sort else 'ascending'}):")
        for year, emission in sorted_data:
            print(f"   {year}: {emission:,.0f} tons")

        # Step 5: Plot
        years = [str(year) for year, _ in sorted_data]
        emissions = [em for _, em in sorted_data]

        plt.figure(figsize=(12, 6))
        plt.bar(years, [e / 1e6 for e in emissions], color="skyblue")
        plt.title(f"{entity} CO₂ Emissions ({start_year}–{end_year}) - Sorted {'Descending' if reverse_sort else 'Ascending'}")
        plt.xlabel("Year")
        plt.ylabel("CO₂ Emissions (Million Tons)")
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        logger.error("❌ CSV file not found.")

    except Exception as e:
        logger.error(f"❌ An unexpected error occurred: {e}")

