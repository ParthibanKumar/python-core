


'''Using a simple sorted function'''

while True:
    try:
        user_input_one = str(input("Please enter your first word: ").lower().replace(" ", ""))
        user_input_two = str(input("Please enter your second word: ").lower().replace(" ", ""))
        
        if len(user_input_one) != len(user_input_two):
            print("Not an anagram")
        else:
            if sorted(user_input_one) == sorted(user_input_two):
                print("It is Anagram")
            else:
                print("It is not a anagram")
    except ValueError:
        print("Invalida string")



'''Using a dictionary and comparison'''

my_dict1 = {}
my_dict2 = {}

user_input_one = str(input("Please enter your first word: ").lower().replace(" ", ""))
user_input_two = str(input("Please enter your first word: ").lower().replace(" ", ""))

for letter in user_input_one:
    if letter in my_dict1:
        my_dict1[letter] += 1
    else:
        my_dict1[letter] = 1

for letters in user_input_two:
    if letters in my_dict2:
        my_dict2[letters] += 1
    else:
        my_dict2[letters] = 1

print(my_dict1)
print(my_dict2)

if my_dict1 == my_dict2:
    print("ANAGRAM")
else:
    print("Not an ANAGRAM")