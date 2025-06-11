first_name = 'Cristian'
last_name = 'Nain'
full_name = first_name + ' ' + last_name
country = 'Mexico'
city = 'Aguascalientes'
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = True
a, b, c = 1, 2.5, 'Python'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

print(len(first_name))
print(len(first_name) > len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radius = 30
pi = 3.1416
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print(area_of_circle)
print(circum_of_circle)

radius_input = float(input())
area_input = pi * radius_input ** 2
print(area_input)

first_name_input = input()
last_name_input = input()
country_input = input()
age_input = input()

print(first_name_input)
print(last_name_input)
print(country_input)
print(age_input)

help('keywords')
