
cities = []

while True:

    city_name = input("Enter the name of a city (or type 'stop' to end): ")

    if city_name.lower() == 'stop':
        break

    population = len(city_name) * 1000000

    cities.append((city_name, population))

cities.sort(reverse=True, key=lambda x: x[1])

for city, population in cities:
    print(f"{city}: {population} citizens")
