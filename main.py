import csv
from rich import print
import matplotlib.pyplot as plt

file_name = 'data.csv'

population_per_continent = {}

with open(file_name, 'r') as csvfile:
  reader = csv.DictReader(csvfile)

  for line in reader:
    continent = line['continent']
    year = int(line['year'])
    population = int(line['population'])

    if continent not in population_per_continent:
      population_per_continent[continent] = {'population': [], 'years': []}

    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)

for continent in population_per_continent:
  years = population_per_continent[continent]['years']
  population = population_per_continent[continent]['population']
  plt.plot(years, population, label=continent, marker="o", alpha=0.6)

plt.title("Internet Population Per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users (in billions)")
plt.grid(True)
plt.legend()

plt.show()

