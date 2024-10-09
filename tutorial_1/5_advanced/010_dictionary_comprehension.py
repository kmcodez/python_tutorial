# dictionary comprehensions = create dictionaries using an expression
#                             can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}


# case 1
# dictionary = {key: expression for (key, value) in iterable}
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5 / 9)) for key, value in cities_in_F.items()}
print(cities_in_C)


# case 2
# dictionary = {key: expression for (key, value) in iterable if conditional}
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for key, value in weather.items() if value == 'sunny'}
print(sunny_weather)


# case 3
# dictionary = {key: (if/else) for (key, value) in iterable}
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: "WARM" if value >= 40 else "COLD" for key, value in cities.items()}
print(desc_cities)


# case 4
# dictionary = {key: function(value) for (key, value) in iterable}
def check_temp(temp):
    if temp >= 70:
        return 'HOT'
    elif 69 >= temp >= 40:
        return "WARM"
    else:
        return 'COLD'


cities_2 = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# for some complex logic, use the function to form a expression, just like Vue template
desc_cities = {key: check_temp(value) for (key, value) in cities_2.items()}
print(desc_cities)
