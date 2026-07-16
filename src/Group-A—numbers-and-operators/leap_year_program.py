# '''This is a simple program checks for the leap year.'''

# '''Definiing the variables.'''
# year = 0
# while_flag = True

# def user_input():
#     global year
#     year = input("Please enter the year that you want to check for the leap year: ")
#     return year

# while while_flag:
#     try:
#         user_input()
#         year = int(year)
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 print(f"The {year} is divisible by 100, going to divisible by 400")
#                 if year % 400 == 0:
#                     print(f"{year} is a leap year because it now divisible by 100 and then 400")
#                 else:
#                     print(f"{year} is not a leap year because it not divisible by 400")
#             else:
#                 print(f"{year} is a leap year because it not divisible by 100")
#         else:
#             print("NULL")
#     except:
#         print(f"{year} is not a valid INTEGER, please re-enter")

# '''==================================================================================='''

'''Other ways to check for leap year'''
'''---------------------------------'''

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

while True:
    try:
        year = int(input("Please enter the year that you want to check for the leap year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")