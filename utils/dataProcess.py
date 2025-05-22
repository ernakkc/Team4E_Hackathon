import csv
from utils.logger import Logger
from utils.general import convert_if_whole
import os

def addData(file_path):
    """
    Add data to the CO2 emissions file.
    :param file_path: Path to the CO2 emissions CSV file.
    """
    logger = Logger()
    # Check if the file exists
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return
    
    # Prompt user for data
    logger.info("Enter the data to be added:")
    logger.info("Note: Ensure that the data is in the correct format.")
    logger.info("If the data already exists, it will not be added again.")
    logger.info("Country name (Entity): ", end="")
    entity = input()
    logger.info("Country code (Code): ", end="")
    code = input()
    logger.info("Year: ", end="")
    year = int(input())
    logger.info("CO₂ emissions (Annual CO₂ emissions): ", end="")
    co2_emissions = float(input())
    co2_emissions = convert_if_whole(co2_emissions)
    

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            d_entity = row[0]
            d_year = int(row[2])
            if d_entity == entity and d_year == year:
                logger.error(f"Error: {entity} already exists for {year}.")
                return

    with open(file_path, mode='a+', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([entity, code, year, co2_emissions])
        logger.success(f"Data added: {entity} - {year}")

def listData(data):
    """
        data = {
            'country': {
                'code': 'country_code',
                'year': {
                    year: co2_emission_value
                }
            }
        }
    """
    logger = Logger()

    logger.info("Select the action you want to perform:")
    logger.info("1 - All data for a particular year")
    logger.info("2 - Data for a specific country within a specific year range")
    logger.info("3 - Data on specific CO₂ emissions range")
    
    try:
        choice = int(input("\n\tChoice (1/2/3): "))
    except ValueError:
        logger.error("Invalid input! Please enter 1, 2, or 3.")
        return

    if choice == 1:
        try:
            year = int(input("Enter the year (e.g., 1950): "))
            found = False
            for country, values in data.items():
                if year in values['year']:
                    co2_emission = values['year'][year]
                    print(f"{country}: {co2_emission} tons")
                    found = True
            if not found:
                logger.warning(f"No data found for the year {year}.")
        except ValueError:
            logger.error("Please enter a valid year!")
            return

    elif choice == 2:
        try:
            country = input("Enter the country name: ")
            start_year = int(input("Enter the start year (e.g., 1950): "))
            end_year = int(input("Enter the end year (e.g., 1960): "))
            if country not in data:
                logger.warning(f"No data found for country '{country}'.")
                return

            values = data[country]['year']
            found = False
            for year in range(start_year, end_year + 1):
                if year in values:
                    print(f"{year}: {values[year]} tons")
                    found = True
            if not found:
                logger.warning(f"No data for {country} between {start_year} and {end_year}.")
        except ValueError:
            logger.error("Invalid year input!")
            return

    elif choice == 3:
        try:
            min_emission = float(input("Enter minimum CO₂ emission value: "))
            max_emission = float(input("Enter maximum CO₂ emission value: "))
            found = False
            for country, values in data.items():
                for year, emission in values['year'].items():
                    if min_emission <= emission <= max_emission:
                        print(f"{country} - {year}: {emission} tons")
                        found = True
            if not found:
                logger.warning(f"No data found for emissions between {min_emission} and {max_emission}.")
        except ValueError:
            logger.error("Please enter valid emission values!")
            return

    else:
        logger.error("Invalid choice! Please select 1, 2, or 3.")
 
def updateData(file_path):
    logger = Logger()

    logger.info("Enter the data to be updated:")
    logger.info("Note: Ensure that the data is in the correct format.")
    logger.info("If the data already exists, it will not be updated.")
    logger.info("Country name (Entity): ", end="")
    entity = input()
    logger.info("Country code (Code): ", end="")
    code = input()
    logger.info("Year: ", end="")
    year = int(input())
    logger.info("New CO₂ emissions (Annual CO₂ emissions): ", end="")
    new_emissions = float(input())
    new_emissions = convert_if_whole(new_emissions)

    updated = False
    updated_rows = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            updated_rows.append(header)

            for row in reader:
                d_entity = row[0]
                d_year = int(row[2])
                if d_entity == entity and d_year == year:
                    row[3] = new_emissions
                    updated = True
                updated_rows.append(row)
        if not updated:
            logger.warning(f"No record found for {entity} in {year}.")
            return
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_rows)
            logger.success(f"CO₂ emissions updated for {entity} in {year}.")
    except FileNotFoundError:
        logger.error("CSV file not found.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
 
def deleteData(co2_filepath):
    """
    Delete the data for a specific country and year from the CO2 data file.
    If data for the specified country and year does not exist, it will raise a warning.
    """
    logger = Logger()
    
    # Check if the file exists
    if not os.path.exists(co2_filepath):
        logger.error(f"File {co2_filepath} does not exist.")
        return

    # get country and year from user
    logger.info("Enter the country name (Entity): ", end="")
    country = input()
    logger.info("Enter the year (e.g., 1950): ", end="")
    year = int(input())
    logger.info(f"Deleting data for {country} in {year}...")

    # Read all data from the file
    updated_rows = []
    is_found = False

    with open(co2_filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        updated_rows.append(header)

        for row in reader:
            d_country_name = row[0]
            d_year = int(row[2])

            if d_country_name == country and d_year == year:
                is_found = True
                continue  # skip this row (i.e., delete it)
            updated_rows.append(row)

    if not is_found:
        logger.warning(f"No data found for {country} in {year}.")
        return

    # Write the updated data back to the file
    with open(co2_filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(updated_rows)

    logger.info(f"Data for {country} in {year} has been deleted.")

