# import math
# # print ("HELOOOO")
# # x = 9
# # y = 4
# # z = x + y
# # print (z)
# # print("OUTPUT IS", z ,"haha")
# # # str = "helooo hashammm"
# # print(len(str))

# # print(str[9]) #from start
# # print(str[-7]) #from end
# # print(str[0:4]) #range (end index not included)
# # print(str[3:]) #last index will be considered as the end range
# # print(str[:4])  #first index will be considered as the start range

# ##formatted strings
# a = 6
# b = 7
# fstr = f"The result of {a} + {b} is {a + b}"
# print (fstr)

# #string methods
# str="helooo hashamm"
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
# print(str.find("hel"))
# print(str.replace("h","l"))
# print("hel" in str)
# print("has" not in str)
# print (math.factorial(5))
# print (math.fabs(-5))
# # x = input("x : ")
# # x = int(x)
# # print(f"x: {x}, y: {x + 3}")

# #conditionals
# temp = 30
# # if temp > 20:
# #     print("its warm")
# # elif temp < 5:
# #     print("its v cold")
# # else:
# #     print("its normal")
# # print("end of if")
 

# #terniary operators

# print("warm") if temp > 20 else print("cold")

# if   20 <= temp <= 30:
#     print("moderate temp")

# # logical operators
# eighteen_plus = True
# has_liscence = True
# student = False

# # if eighteen_plus and has_liscence:
# #     print("Eligible for driving")
# # else:
# #     print("Not Eligible")


# if (eighteen_plus and has_liscence) and not student:
#     print("Eligible for driving")
# else:
#     print("Not Eligible")

# #for loop

# for i in range(1, 10, 2): #(start, end, step/gap)
#     print("Attempt", i, i* ".")
# success = True
# for i in range(3):
#     print("Attempt")
#     if success:
#         print("Successful")
#         break
# else:
#     print("Failed")

# #nested loop (printing cordinates)

# for x in range(3):
#     for y in range(3):
#         print(f"({x}, {y})")

# for s in "String":
#     print(s)

# for num in [3,5,6,7,5]: #list
#     print(num)

#while loop

# inp = ""
# while inp != "end":
#     inp = input("Enter:")
#     print(inp)

# count = 0
# for i in range(1, 10):
#     if i % 2 ==0:
#         print(i)
#         count += 1
# print(f"We have {count} even numbers")

#functions

# def sum(num1, num2):
#     return f"Sum = {num1 + num2}"
# print(sum(4, 6))


def ArrayAdditionI(arr):
    max_num = max(arr)
    arr.remove(max_num)
    n = len(arr)
    
    # Generate all possible non-empty subsets and check their sums
    for i in range(1, 1 << n):
        total = 0
        for j in range(n):
            if (i >> j) & 1:
                total += arr[j]
        if total == max_num:
            return "true"
    return "false"

# Test cases
print(ArrayAdditionI([4, 6, 23, 10, 1, 3]))  # Output: true
print(ArrayAdditionI([5, 7, 16, 1, 2]))      # Output: false
