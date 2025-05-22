import csv
from utils.logger import Logger
from utils.year_to_comparison import emission_difference
from utils.menu import printMenu, clearScreen, goodbye, wait_for_user
from utils.country_comparison import countries_within_emission_range
from utils.countries_with_emissions_in_a_certain_range import countries_within_emission_range_emission
from utils.countries_above_threshold import countries_above_threshold
from utils.dataProcess import addData, listData, deleteData, updateData
from utils.average_emission import average_emission_for_country
from utils.emission_intensity import per_capita_emission
from utils.trendanalysis import analyze_co2_trends
from utils.sorting_emmision import filter_and_sort_emissions_with_plot
from utils.max_increasing_decreasing import analyze_10_year_emission_change_and_get_details
from utils.report_generation import analyze_emissions_full

CO2_PATH = 'hackathon_data/annual-co2-emissions-per-country/annual-co2-emissions-per-country.csv'
POPULATION_PATH = 'hackathon_data/population/population.csv'

class Main:
    def __init__(self):
        self.logger = Logger()
        self.data = {}
    

    def load_data(self):
        data = {}
        """
        data = {
            'country': {
                'code': 'country_code',
                'year': co2_emission_value
            }
        }
        """
        with open(CO2_PATH, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                country = row[0]
                code = row[1]
                year = int(row[2])
                co2 = float(row[3])
                if country not in data:
                    data[country] = {'code': code, 'year': {}}
                if year not in data[country]['year']:
                    data[country]['year'][year] = co2
                else:
                    data[country]['year'][year] += co2
                    
        self.logger.success("Data loaded successfully")
        return data
    
    def reload_data(self):
        self.data = {}
        self.load_data()
        self.logger.success("Data reloaded successfully")
        return self.data
        
    def delete_data(self, country, year):
        deleteData(country, year, CO2_PATH)
        self.reload_data()
        self.logger.success(f"Data for {country} in {year} deleted successfully")
        return self.data
        
    def run(self):
        self.data = self.load_data()
        
        while True:
            choice = printMenu()
            clearScreen()
            if choice == "1":
                addData(CO2_PATH)
                self.reload_data()
                wait_for_user()
            elif choice == "2":
                listData(self.data)
                self.reload_data()
                wait_for_user()
            elif choice == "3":
                updateData(CO2_PATH)
                self.reload_data()
                wait_for_user()
            elif choice == "4":
                deleteData(CO2_PATH)
                self.reload_data()
                wait_for_user()
            elif choice == "5":
                countries_above_threshold(CO2_PATH)
                wait_for_user()
            elif choice == "6":
                countries_within_emission_range(CO2_PATH)
                wait_for_user()
            elif choice == "7":
                countries_within_emission_range_emission(CO2_PATH)
                wait_for_user()
            elif choice == "8":
                emission_difference(CO2_PATH)
                wait_for_user()
            elif choice == "9":
                average_emission_for_country(CO2_PATH)
                wait_for_user()
            elif choice == "10":
                per_capita_emission(CO2_PATH, POPULATION_PATH)
                wait_for_user() 
            elif choice == "11":
                analyze_co2_trends(CO2_PATH)
                wait_for_user()
            elif choice == "12":
                filter_and_sort_emissions_with_plot(CO2_PATH)
                wait_for_user()
            elif choice == "13":
                analyze_10_year_emission_change_and_get_details(CO2_PATH)
                wait_for_user()
            elif choice == "14":
                analyze_emissions_full(CO2_PATH)
                wait_for_user()
            
            if choice == "15":
                clearScreen()
                goodbye()

if __name__ == "__main__":
    app = Main()
    app.run()