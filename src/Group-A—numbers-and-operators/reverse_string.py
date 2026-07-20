# '''This is a simple program to reverse string.'''


while True:
    try:
        user_input = input("Please enter a string to reverse: ")
        reversed_string = user_input[::-1]
        print(f"here we go  {reversed_string}")
    except ValueError:
        print("Invalid input. Please enter a valid string.")