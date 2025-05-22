import csv
import matplotlib.pyplot as plt
from utils.logger import Logger

def analyze_10_year_emission_change_and_get_details(csv_file_path):
    logger = Logger()
    logger.info("Analyzing 10-year CO2 emission change...")
    country_data = {}
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        try:
            entity_idx = header.index('Entity')
            year_idx = header.index('Year')
            emissions_idx = header.index('Annual CO₂ emissions')
        except ValueError as e:
            logger.error(f"Error: Expected columns not found in CSV headers. Please ensure 'Entity', 'Year', and 'Annual CO₂ emissions' columns exist. Error: {e}")
            return None, None, None

        for row in reader:
            try:
                entity = row[entity_idx]
                year = int(row[year_idx])
                emissions_str = row[emissions_idx]
                if emissions_str:
                    emissions = float(emissions_str) 
                else:
                    emissions = 0.0

                if entity not in country_data:
                    country_data[entity] = {}
                country_data[entity][year] = emissions
            except (ValueError, IndexError) as e:
                logger.error(f"Error: Problem processing row '{row}'. This might be a data type error or missing column. Error: {e}")
                continue

    max_increase = -float('inf')
    min_decrease = float('inf')
    country_max_increase_info = {}
    country_min_decrease_info = {}

    start_year = 2013
    end_year = 2023

    for country, years_data in country_data.items():
        emission_2013 = years_data.get(start_year)
        emission_2023 = years_data.get(end_year)

        if emission_2013 is not None and emission_2023 is not None:
            change = emission_2023 - emission_2013

            if change > max_increase:
                max_increase = change
                country_max_increase_info = {
                    'country': country,
                    '2013_emissions': emission_2013,
                    '2023_emissions': emission_2023,
                    'change': change
                }

            if change < min_decrease:
                min_decrease = change
                country_min_decrease_info = {
                    'country': country,
                    '2013_emissions': emission_2013,
                    '2023_emissions': emission_2023,
                    'change': change
                }
            
     


    most_increased_info, most_decreased_info, all_country_data = country_max_increase_info, country_min_decrease_info, country_data

    if most_increased_info and most_decreased_info:
        print(f"Greatest CO2 emission increase (2013-2023): {most_increased_info['country']} ({most_increased_info['change']:,.2f} increase)")
        print(f"Greatest CO2 emission decrease (2013-2023): {most_decreased_info['country']} ({most_decreased_info['change']:,.2f} decrease)")

        # Prepare data for plotting
        countries_to_plot = [most_increased_info['country'], most_decreased_info['country']]
        years = [2013, 2023]
        
        emissions_increase = [most_increased_info['2013_emissions'], most_increased_info['2023_emissions']]
        emissions_decrease = [most_decreased_info['2013_emissions'], most_decreased_info['2023_emissions']]

        # Plot
        fig, ax = plt.subplots(figsize=(12, 7)) # Increased figure size for better text visibility

        # Plot for the country with greatest increase
        ax.plot(years, emissions_increase, marker='o', linestyle='-', color='green', label=f"{most_increased_info['country']} (Increase)")
        
        # Annotate start and end values
        ax.text(years[0], emissions_increase[0], f'{emissions_increase[0]:,.0f}', ha='right', va='bottom', color='green', fontsize=9)
        ax.text(years[1], emissions_increase[1], f'{emissions_increase[1]:,.0f}', ha='left', va='top', color='green', fontsize=9)
        
        # Annotate the total increase amount near the end point
        mid_point_increase = (emissions_increase[0] + emissions_increase[1]) / 2
        ax.text(2018, mid_point_increase, 
                f'+{most_increased_info["change"]:,.0f}', 
                ha='center', va='center', color='darkgreen', 
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'), 
                fontsize=10, fontweight='bold')


        # Plot for the country with greatest decrease
        ax.plot(years, emissions_decrease, marker='o', linestyle='-', color='red', label=f"{most_decreased_info['country']} (Decrease)")
        
        # Annotate start and end values
        ax.text(years[0], emissions_decrease[0], f'{emissions_decrease[0]:,.0f}', ha='right', va='top', color='red', fontsize=9)
        ax.text(years[1], emissions_decrease[1], f'{emissions_decrease[1]:,.0f}', ha='left', va='bottom', color='red', fontsize=9)

        # Annotate the total decrease amount near the end point
        mid_point_decrease = (emissions_decrease[0] + emissions_decrease[1]) / 2
        ax.text(2018, mid_point_decrease, 
                f'{most_decreased_info["change"]:,.0f}', # Decrease values are already negative
                ha='center', va='center', color='darkred', 
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'), 
                fontsize=10, fontweight='bold')


        # Titles and labels
        ax.set_title('CO₂ Emission Change Between 2013 and 2023 (Greatest Increase/Decrease)')
        ax.set_xlabel('Year')
        ax.set_ylabel('Annual CO₂ Emissions (tonnes)')
        ax.set_xticks(years)
        ax.ticklabel_format(style='plain', axis='y')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    else:
        print("10-year emission change analysis could not be performed. Check data availability.")