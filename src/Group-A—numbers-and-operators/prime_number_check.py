# '''This is a simple program checks for Prime Number.'''

is_Prime = False

while True:
    try:
        user_input = int(input("Please enter a number to find its prime factors: "))
        if user_input <= 1:
            print(f"The number {user_input} is not a prime number. Please enter a number greater than 1.")
        else:
            is_Prime = True
            for i in range(2, user_input):
                if user_input % i == 0:
                    is_Prime = False
                    break           
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        
    if is_Prime:
        print(f"The number {user_input} is a prime number.")
    else:
        print(f"The number {user_input} is not a prime number.")
