base = int(input("Enter base: "))
height = int(input("Enter height: "))
print(f"The area of triangle is {base * height}")

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print(f"The perimeter of triangle is {side_a + side_b + side_c}")

radius = int(input("Enter radius of circle: "))
pi = 3.14
area = pi* radius ** 2
curcumference = 2 * pi * radius
print(f"Area of cirlce is: {area}")
print(f"Circumference of cirlce is: {curcumference}")

point1 = [2, 2]
point2 = [6, 10]

x1 = point1(0)
y1 = point1(1)

x2 = point2(0)
y2 = point2(1)

import math
slope = (y2 - y1) / (x2 - x1)
euc_dis = math.sqrt((y2 - y1)**2 - (x2 - x1)**2)

print(f"slope = {slope}")
print(f"Euclidean Distance = {euc_dis}")

if  'on' in 'python' and 'dragon':
    print("yes")

sentence = 'I hope this course is not full of jargon'
if 'jargon' in sentence:
    print("yes it is")

text = "There is no 'on' in both dragon and python"
len_text = len(text)
float_val = float(len_text)
str_val = str(float_val)
print(f"Types: {len_text}, {float_val}, {str_val} ")

def check_even(num):
    print("even") if num % 2 == 0 else print("odd")

check_even(7)
check_even(6)
        
    




