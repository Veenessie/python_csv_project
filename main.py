import csv
from rich import print

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