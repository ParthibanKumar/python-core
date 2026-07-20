# '''This is a simple program to find the longest common prefix'''


user_input_one = str(input("Please enter your first word: ").lower().replace(" ", ""))
user_input_two = str(input("Please enter your first word: ").lower().replace(" ", ""))

user_list = [ user_input_one, user_input_two ]
count = 0
long_word = ""


for word_length in user_list:
    if len(word_length) > count:
        count = len(word_length)
        long_word = word_length
        
j = []

for i in range(len(long_word)):
    if long_word[i] == user_input_two[i]:
        print(f"{long_word[i]} is same as {user_input_two[i]}")
        j.append(long_word[i])
    else:
        print(f"{long_word[i]} is not same as {user_input_two[i]}")
        break

print(j)