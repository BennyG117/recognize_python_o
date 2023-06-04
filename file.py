
#! Example Comments:
# this is a single line comment
"""
This is
a multiline
comment
"""



#! Example Output:
my_new_favorite_language = 'Python' # variable declaration, initialize string



#! HW Start:
num1 = 42     # variable declaration, data type = primitive = number

num2 = 2.3     # variable declaration, data type = primitive = float

boolean = True     # variable declaration, data type = primitive = boolean = true = 1

string = 'Hello World'     # variable declaration, data type = primitive = string 

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']     # variable declaration, data type = composite = list, initialize value, string(s) *5 

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}     #variable declaration, data type = composite = dictionary, initialize values, declaration string, declaration string, declaration number, declaration boolean, false = 0

fruit = ('blueberry', 'strawberry', 'banana')     #variable declaration, data type = composite = tuples, initialize value, string, string, string 

print(type(fruit))     #log statement, type check, data type = composite = tuples, initialize tuples 

print(pizza_toppings[1])     #log statement, data type = composite = list, access value of index 1 of list
pizza_toppings.append('Mushrooms')     #data type = composite = list, add value, add string 'Mushrooms'

print(person['name'])     #log statement, data type = composite = dictionary, access value string, string = 'name'

person['name'] = 'George'     #variable declaration, data type = composite = dictionary, change value of index name, changing string name from John to George

person['eye_color'] = 'blue'     #variable declaration, data type = composite = dictionary, add value, initialize value eye_color, add value of 'blue to eye_color

print(fruit[2])     #log statement, data type = composite = tuples, access value, access value of index 2 = 'banana'

if num1 > 45:     # conditional statement, if, data type = primitive = number > number, then... 
    print("It's greater")     # log statement, data type = primitive = string, log string "It's greater"
else:     #conditional else, then log statement...
    print("It's lower")     # log statement, data type = primitive = string, log string "It's lower"

if len(string) < 5:     # length check of letters in string, conditional statement, if, data type = primitive = string, return number of letters in string, conditional if, number characters in the string < 5, then log statement...
    print("It's a short word!")     # log statement, data type = primitive = string, log string "It's a short word!"
elif len(string) > 15:     # length check of letters in string, conditional else if, data type = primitive = string, return number of letters in string, conditional if, number of characters in the string > 15 then log statement...
    print("It's a long word!")     # log statement, data type = primitive = string, log string "It's a long word!"
else:     # conditional else, then log...
    print("Just right!")     #log statment, data type = porimitive = string, log string "Just right!"

for x in range(5):     #conditional for loop start, length check to check if number is within range of 0-4, if within 4, then log statement...
    print(x)     # log statemenet, data type = primitive = number, log number that x is
for x in range(2,5):     #conditional for loop, check if number is between 2 & 4, if yes (boolean), then log statement...
    print(x)     # log statement result number
for x in range(2,10,3):     #conditional, for loop, if x between numbers 2-9 (checking in increments of "3"), then log statment...
    print(x)     #llog statement result number (aka "x")
x = 0     #assign variable, x = number (0)
while(x < 5):     # Conditional while loop start, if value of x < number (5) then log statement...
    print(x)     #log statement result number (aka "x"), then...
    x += 1     # increment x by adding x + 1 = new x value to restart while loop

pizza_toppings.pop()     #list, delete last value on list
pizza_toppings.pop(1)     #list, delete value of index 1 on the list

print(person)     # log statment person(dictionary)
person.pop('eye_color')     # delete value of eye_color from the dictionary of person
print(person)     #log statment, access value,log updated dictionary of person

for topping in pizza_toppings:     #conditional for loop, access value in list
    if topping == 'Pepperoni':     #conditional if, value of topping equals, value of string pepperoni, then continue sequence
        continue     #continuing sequence...
    print('After 1st if statement')     #log statement, string, log string "After 1st if statement"
    if topping == 'Olives':     #conditional if, list equals string olives, then break
        break     #break...

def print_hello_ten_times():     #define, assign value, log statement of the function
    for num in range(10):     #conditional for loop, number between 0-9, then log statment...
        print('Hello')     #log statement, string, log "Hello"

print_hello_ten_times()     #log statement, log function

def print_hello_x_times(x):     #define, assign value, add parameter of number "x"
    for num in range(x):     #conditional for loop, if number is within range of "x", then log statement...
        print('Hello')     #log statement, string, log string "Hello"

print_hello_x_times(4)     #log statement, parameter assigned as "4", log statement 4 times

def print_hello_x_or_ten_times(x = 10):     #define, assign value, add parameter of knewly assigned variable, x = 10
    for num in range(x):     #conditional for loop, if numnber is within range of 0-9, then continue...
        print('Hello')     #log statement, string, log "Hello"

print_hello_x_or_ten_times()     ##log statement, log function
print_hello_x_or_ten_times(4)     #log statement, parameter assigned as "4", log statement 4 times


"""
Bonus section
"""

# print(num3)  // log statment, log the tuples named "num3"

# num3 = 72  // variable declaration, assigning num3 the value of the number 72, the tuples num3 = 72

# fruit[0] = 'cranberry'  // assign value of a composite value for a tuples, will receive an error sinc it's already defined as "blueberry"

# print(person['favorite_team'])  // 
# print(pizza_toppings[7])  // 
#   print(boolean)  // 
# fruit.append('raspberry')  // 
# fruit.pop(1)  // 
