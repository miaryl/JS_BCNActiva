# defining functions

def greeting(name, department):
    print("welcome, " + name)
    print( "you are part of " + department)

greeting("mio", "developer")

# returning values

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("the sum of both areas is: " + str(sum))


def convert_seconds(seconds):
    hours = seconds // 3600
    mins = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - mins * 60
    return hours, mins, remaining_seconds

hours, mins, seconds = convert_seconds(5000)
print(hours, mins, seconds)

# principles of code reuse
def lucky_num(name):
    number = len(name) * 9
    print("Hi " + name + ". Ur lucky number is " + str(number))

lucky_num("Kay")
lucky_num("Cameron")


# code style

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

# study guide
def find_total_days(years, months, days):
    my_days = (years*365) + (months * 30) + days
    return my_days

print(find_total_days(37, 10, 21))


print("-----------------------------------------------")

def convert_volume(fluid_ounce):
    ml = fluid_ounce * 29.5
    return ml

print("the volume in milimeters is " + str(convert_volume(2)))

# practice quiz

# this function convers miles to kilometers(km)
def convert_distance(miles):
    km = miles * 1.6
    return km

my_trip_miles = 55
my_trip_km = convert_distance(my_trip_miles)

print("the distance in kilos is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(my_trip_km*2))

# This function compares two numbers and returns them in increasing order.
def order_numbers(num1, num2):
    if num2 > num1:
        return num1, num2
    else:
        return num2, num1
    
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

print(order_numbers(15, 20))








