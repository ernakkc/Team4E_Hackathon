import csv
from logger import Logger
import os

def deleteData(country, year, co2_filepath):
    """
    Delete the data for a specific country and year from the CO2 data file.
    If data for the specified country and year does not exist, it will raise a warning.
    """
    logger = Logger()
    
    # Check if the file exists
    if not os.path.exists(co2_filepath):
        logger.error(f"File {co2_filepath} does not exist.")
        return

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

