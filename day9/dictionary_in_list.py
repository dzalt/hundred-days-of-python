travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(country, visits, cities):
    my_dict = {}
    my_dict["country"] = country
    my_dict["visits"] = visits
    my_dict["cities"] = cities
    travel_log.append(my_dict)


# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
