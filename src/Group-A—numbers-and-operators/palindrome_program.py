# '''This is a simple program to palindrome string.'''


# while True:
#     try:
#         user_input = input("Please enter a string to reverse: ")
#         reversed_string = user_input[::-1]
#         if user_input == reversed_string:
#             print(f"{reversed_string} is a Palindrome")
#         else:
#             print(f"{reversed_string} is not a palindrome")
#     except ValueError:
#         print("Invalid input. Please enter a valid string.")









while True:
    try:
        user_input = input("Please enter a string to reverse: ")
        left = 0 
        right = len(user_input) - 1
        is_palindrome = True
        while left < right:
            if user_input[left] != user_input[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
        if is_palindrome:
            print("This string is a Palindrome")
        else:
            print("This string is a not a Palindrome")
    except ValueError:
        print("Invalid input. Please enter a valid string.")