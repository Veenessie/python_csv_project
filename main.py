import csv
from rich import print
import matplotlib.pyplot as plt


def generate_population_dictionary(filename):
  """
  Generate population dictionary from CSV file. 
  Return a dictionary following this structure: 
  "Africa": {population:[100, 200, 300], years[1990, 2000, 2010, 2020]},
   "Asia": {population:[100, 200, 300], years[1990, 2000, 2010, 2020]}
  """
  population_per_continent = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])

      if continent not in population_per_continent:
        population_per_continent[continent] = {'population': [], 'years': []}

      population_per_continent[continent]['population'].append(population)
      population_per_continent[continent]['years'].append(year)

  return population_per_continent


def create_population_plot(population_dictionary):
  """Generates the population plot chats from dictionary"""

  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.6)

  plt.title("Internet Population Per Continent")
  plt.xlabel("Year")
  plt.ylabel("Internet Users (in billions)")
  plt.grid(True)
  plt.legend()

  plt.show()


file_name = 'data.csv'

population_per_continent = generate_population_dictionary(file_name)
create_population_plot(population_per_continent)
