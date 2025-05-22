import csv
from utils.logger import Logger


def average_emission_for_country(csv_path):
    logger = Logger()
    logger.info("Calculating average CO₂ emission for a country...")
    
    logger.info("Enter the country name:", end=' ')
    country_input = input().strip().lower()

    while True:
        try:
            logger.info("Enter the start year:", end=' ')
            start_year = int(input())
            logger.info("Enter the end year:", end=' ')
            end_year = int(input())
            if start_year > end_year:
                logger.error("Start year must be less than or equal to end year. Please try again.")
            else:
                break
        except ValueError:
            logger.error("Invalid input. Please enter numeric values for years.")

    total_emission = 0
    count = 0

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)

            for row in reader:
                entity = row[0].strip().lower()
                try:
                    year = int(row[2].strip())
                    emission = float(row[3].strip())
                except:
                    continue

                if entity == country_input and start_year <= year <= end_year:
                    total_emission += emission
                    count += 1

        if count == 0:
            logger.error(f"No emission data found for {country_input.title()} between {start_year} and {end_year}.")
            return

        average_emission = total_emission / count
        logger.info(f"Average CO₂ emission for {country_input.title()} from {start_year} to {end_year} is {average_emission:,.2f} tons.")

    except FileNotFoundError:
        logger.error(f"File not found: {csv_path}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

