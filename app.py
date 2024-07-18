print('Hello Neema!')
print('*' * 10) # Expression is a piece of code that produces a value

# Variables (Converted to binary representation before storage)
price = 10 # Integer
rating = 4.9 #Float
name = 'Neema' #String
is_available = True # Boolean
price = 20
print(price)

patient = {
    'name': 'John Smith',
    'age': 20,
    'is_new_patient': True
}

name = input('What is your name? ')
favourite_colour = input('What is your favourite colour? ')
print(name + ' likes ' + favourite_colour)

birth_year = input('Birth year: ') # Input is always a string
age = 2024 - int(birth_year)
print('Your age is', age)

weight_lbs = input('Weight in pounds: ')
weight_kg = int(weight_lbs) * 0.45
print('Your weight in kilograms is', weight_kg)

#We use triple quotes for multi-line code
course = '''
Hi John,

This is an email to remind you about your upcoming course. The course is 'Introduction to Python' and it will be held on Tuesday, 14th October.

Best regards,
Neema
'''
print(course)

course_name = 'Python for "Beginners"'
print(course_name[-3])
print(course_name[0:-1])
print(course_name[3:-3])
print(course_name[0:3]) #excludes the last index
another = print(course_name[:]) #copy

#Formatted Strings
first = 'Neema'
last = 'Charity'
message = f'{first} [{last}] is a coder'
print(message)
print(len(first)) #len is not limited to strings only

#Methods
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.capitalize()) #only first letter
print(course.title()) #every first letter of a word
print(course.find('Beginners')) #returns index of the first occurence (case sensitive). Brings -1 if it doesn't exist
print(course.replace('Beginners', 'Advanced'))
print(course) #doesn't modify the string stored in the course variable
print('Python' in course) #returns boolean

#Arithmetic Operations
print(10 // 3) #produces integer
print(10 / 3) #produces float
print(10 % 3) #produces remainder
print(10 ** 3) #produces power
x = 10
x += 5 #same as x = x + 5 (Augmented code)
print(x)

#Order of Operations
# 1. Parenthesis
# 2. Exponention
# 3. Multiplication or division
# 4. Addition or subtraction
x = 10 + 3 * 2 ** 2
print(x)
x = (2 + 3) * 10 - 3
print(x)

# Math Functions
x = 2.9
print(round(x)) # rounds to nearest integer
print(abs(-5)) # absolute value
print(pow(2, 3)) # power
print(max(10, 5, 15, 20)) # maximum value
print(min(10, 5, 15, 20)) # minimum value
print(sum([1, 2, 3, 4, 5])) # sum of all elements
print(sum(range(1, 11))) # sum of first 10 natural numbers
# NB: Sum takes at most 2 arguements
# import math then use dot notation to access

# If Statements
is_hot = False
is_cold = False
if is_hot:
    print('It is hot outside.')
elif is_cold:
    print('It is cold outside.')
else:
    print('It is a lovely day.')
print('It is a lovely day.')

price_str = '$1M'
price = int(price_str.replace('$', '').replace('M', '000000'))
print(price)
good_credit = False
if good_credit:
    down_payment = int(price * 0.1)
else:
    down_payment = int(price * 0.2)
print(f'Down Payment: ${down_payment}')

# Logical Operators
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print('Eligible for loan.')
elif has_good_credit or has_high_income:
    print('Almost eligible for loan.')
elif has_high_income and not has_good_credit:
    print('Not eligible for loan due to poor credit.')

# Comparison Operators
temperature = 20 # Assignmentb is one equal sign
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print('It is a cold day')
else:
    print("It's neither hot nor cold")

name = 'Charity'
if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print('Name must be a maximum of 50 characters')
else:
    print('Name looks good!')

weight = int(input('Weight in Lbs or Kgs:'))
unit = input('(L)bs or (K)gs: ')
if unit.upper() == 'L':
    print(f'Your weight is {weight * 0.45} kilos')
else:
    print(f'Your weight is {weight / 0.45} kilos')

i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('Done')

guess_count = 1
while guess_count <= 3:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == 9:
        print('Correct!')
        break
else:
    print('Sorry, you failed.')

#Car game
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started...Ready to go!')
    elif command == 'stop':
        if not started:
            print('Car is already stopped.')
        else:
            started = False
            print('Car stopped.')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit the program
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")

#For loop
for character in 'Python':
    print(character)
for number in range(5,10):
    print(number)
for number in range(0,10,2): #optional argument of alternate
    print(number)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'Total price: ${total}')

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5,2,5,2,2]
for number in numbers:
    print('x' * number) #NB: not power

#OR
for number in numbers:
    stars = ''
    for star_count in range(number):
        stars += 'x'
    print(stars)

# Lists
numbers = [5,2,5,2,2]
print(numbers[1:-1])
print(max(numbers))

max = 0
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (matrix[1][2])
for row in matrix:
    for item in row:
        print(item)

# List Methods
numbers = [5, 2, 1, 7, 4]
numbers.append(1)
numbers.insert(2, 6) # index then object
numbers.remove(1) 
numbers.pop()
print(numbers.index(6)) # Prints the index of the number passed
print (50 in numbers) # Safer
print(numbers.count(1)) # Counts the occurrences of a number
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.clear() # Removes all elements
print(numbers)

numbers = [1,1,2,3,4,4,5]
new = [] # Use a list
for number in numbers:
    if number not in new:
        new.append(number)
print(new)

# Tuples
# Similar to lists but immutable (only has count and index methods)
numbers = (1,2,3,4,5)

# Unpacking (For lists and tuples)
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)

# Dictionaries 
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
print(customer.get('birthdate')) # If it doesn't exist, get method makes it to print None
print(customer.get('birthdate', 'Jan 1 1980'))
customer['name'] = 'Jack Smith'
print(customer['name'])

phone = input('Phone Number: ')
words = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
result = ''
for number in phone:
    result += words.get(number, '!') + ' '
print(result)

# Emoji Converter
message = input('>')
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':grinning:': '😀',
        ':smile:': '😊',
        ':laughing:': '😆',
        ':blush:': '😊',
        ':smiley_cat:': '😺',
        ':paw_prints:': '🐾',
        ':heart_eyes:': '😍',
        ':kissing_heart:': '💖',
        ':smiling_imp:': '😈',
        ':sunglasses:': '😎',
        ':revolving_hearts:': '💞',
        ':heart:': '❤️',
        ':broken_heart:': '💔',
        ':yellow_heart:': '💛',
        ':green_heart:': '💚',
        ':blue_heart:': '💙',
        ':purple_heart:': '💜',
        ':hearts:': '�'
    }
    converted = ''
    for word in words:
        converted += emojis.get(word, word) +' '
return converted
print(emoji_converter(message))

#Functions
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')

print('Start')
# greet_user('Neema') #Must be a string
greet_user('Neema', 'Charity')
calc_cost(total=50, shipping=5, discount=0.1) #Keyword arguements (after positional)
print('End')

# By default, all functions in Python return None






