import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

# 1st version

# def randomGenerator(x):
#     return random.randint(0,len(x)-1)

# for letter in range(0,nr_letters):
#     randLetter = randomGenerator(letters)
#     s_letters = letters[randLetter]
#     password.append(s_letters)

# for number in range(0,nr_numbers):
#     randNumber = randomGenerator(numbers)
#     s_numbers = numbers[randNumber]
#     password.append(s_numbers)

# for symbol in range(0,nr_symbols):
#     randSymbol= randomGenerator(symbols)
#     s_symbols = symbols[randSymbol]
#     password.append(s_symbols)


# 2nd version


for letter in range(1,nr_letters+1):
    # += is eqauivalent of arr.append() in python 
    password+=random.choice(letters)

for number in range(1,nr_numbers+1): 
    password+=random.choice(numbers)

for symbol in range(1,nr_symbols+1):
    password+=random.choice(symbols)

random.shuffle(password)
# join takes any iterable as a argument and join them in one string
final_password ="".join(password)
print(f"Your password is:\n{final_password}")

