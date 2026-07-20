# '''This is a simple program checks for sum of individual digits of a number.'''

user_input = input("Please enter a number to find the sum of its digits: ")



def sum_of_digits(user_input):
    total = 0
    num = int(user_input)  # Convert input to integer
    num = abs(num)  # Ensure the number is positive for digit extraction

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total


print(f"The sum of the digits of {user_input} is: {sum_of_digits(int(user_input))}")