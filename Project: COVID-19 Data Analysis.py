import pandas as pd
import matplotlib.pyplot as plt

class CovidAnalysis:
    def __init__(self, data_url):
        self.df = pd.read_csv(data_url)

    def preprocess(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.sort_values('date', inplace=True)

    def plot_cases_over_time(self, country):
        country_df = self.df[self.df['location'] == country]
        plt.figure(figsize=(10, 6))
        plt.plot(country_df['date'], country_df['total_cases'])
        plt.title(f'COVID-19 Total Cases Over Time in {country}')
        plt.xlabel('Date')
        plt.ylabel('Total Cases')
        plt.grid(True)
        plt.show()

def main():
    DATA_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    analysis = CovidAnalysis(DATA_URL)
    analysis.preprocess()
    analysis.plot_cases_over_time('United States')

if __name__ == "__main__":
    main()
