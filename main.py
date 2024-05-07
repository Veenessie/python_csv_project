import csv
from rich import print
import matplotlib.pyplot as plt

file_name = 'data.csv'

population_per_continent = {}

with open(file_name, 'r') as csvfile:
  reader = csv.DictReader(csvfile)

  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']

    if continent not in population_per_continent:
      population_per_continent[continent] = {'population': [], 'years': []}

    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)

print(population_per_continent)

plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400],
         label="Europe",
         marker="x")

plt.title("Internet Population Per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.legend()

plt.show()
