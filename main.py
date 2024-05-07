import csv
from rich import print
import matplotlib.pyplot as plt

file_name = 'data.csv'

with open(file_name, 'r') as csvfile:
  reader = csv.DictReader(csvfile)

  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']
    print(continent)
    print(year)
    print(population)


plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker ="x")

plt.title("Internet Population Per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.legend()

plt.show()