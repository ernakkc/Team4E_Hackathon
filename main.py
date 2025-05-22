import csv
from utils.logger import Logger

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
                'year': {
                    'co2': 0,
                    'population': 0
                }
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
                    data[country]['year'][year] = {'co2': co2, 'population': 0}
                else:
                    data[country]['year'][year]['co2'] += co2
        with open(POPULATION_PATH, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                country = row[0]
                code = row[1]
                year = int(row[2])
                population = int(row[3])
                if country not in data:
                    data[country] = {'code': code, 'year': {}}
                if year not in data[country]['year']:
                    data[country]['year'][year] = {'co2': 0, 'population': population}
                else:
                    data[country]['year'][year]['population'] += population
        
        self.logger.success("Data loaded successfully")
        return data
    
    def run(self):
        self.data = self.load_data()
    

if __name__ == "__main__":
    app = Main()
    app.run()