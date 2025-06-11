###Exercises - Day 3
#1
age = 19

#2
height = 1.62

#3
complex_number = 3 + 4j

#4
base = float(input())  # Enter base: 20
height_triangle = float(input())  # Enter height: 10
area = 0.5 * base * height_triangle
print("The area of the triangle is", area)

#5
a = float(input())  # Enter side a: 5
b = float(input())  # Enter side b: 4
c = float(input())  # Enter side c: 3
perimeter = a + b + c
print("The perimeter of the triangle is", perimeter)

#6
length = float(input())
width = float(input())
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area:", area_rectangle)
print("Perimeter:", perimeter_rectangle)

#7
radius = float(input())
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area:", area_circle)
print("Circumference:", circumference)

#8
x_intercept = 1
y_intercept = -2
slope = 2
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

#9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slope_2)
print("Euclidean distance:", distance)

#10
print(slope == slope_2)

#11
x_values = [-3, -2, -1, 0, 1, 2, 3]
for x in x_values:
    y = x**2 + 6*x + 9
    print("x:", x, "y:", y)

#12
print(len('python') != len('dragon'))

#13
print('on' in 'python' and 'on' in 'dragon')

#14
print('jargon' in 'I hope this course is not full of jargon')

#15
print('on' not in 'dragon' and 'on' not in 'python')

#16
length_python = len('python')
print(float(length_python))
print(str(length_python))

#17
number = int(input())
print(number % 2 == 0)

#18
print(7 // 3 == int(2.7))

#19
print(type('10') == type(10))

#20
print(int(float('9.8')) == 10)

#21
hours = float(input())  # Enter hours: 40
rate = float(input())   # Enter rate per hour: 28
pay = hours * rate
print("Your weekly earning is", pay)

#22
years = int(input())  # Enter number of years you have lived: 100
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
