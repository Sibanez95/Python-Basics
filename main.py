# your first line of code :) 
print ("Hello World!")

# variables 
wallet = 100
print (wallet)

wallet = 1000
print (wallet)

# prompt: make a varibale called day and set it equal to the date of the month
day = 2
print (day)

# integars can be positive or negative, whole numbers
temp = -15

# floats are decimals 
weight = 120.5

print (day + 3)
print (weight * 2)
print (weight / 2)
print (day - 1)

# prompt: find something around you in your life to represent an int and a float. Put them in variables. 
age = 27
weight = 125

# strings are '' or "" (be consistent)
shirt = "blue" 
print (shirt)

# store = "sonny's salon, the "best" there is!"
store = 'sonny\'s salon, the "best" there is!'
print (store)

# prompt: put the name of a movie you like into a variable called movie 
movie = "notebook"
print (movie)

# use an f string
day = 2 
month = "June" 
temp = 85
day_name = "Friday"

print (f"Today is {month} {day} and it's {temp} degrees outside.")

# prompt: make a variable called day_name and set it to day of the week like Tuesday and add it to the string we print

print (f"Today is {day_name} {month} {day} and it's {temp} degrees outside")

# boolean (this or that, yes or no, on or off, true or false = binary)

light_is_on = True

if light_is_on: 
  print ("This light is on!")
else:
  print ("The light is off!")

# prompt: find something around you that could be represented by a Boolean and make a variable for it

fridge_is_full = False

if fridge_is_full:
  print ("No groceries needed!")
else:
  print ("Go shopping!")

weight = 120.5

if weight < 125:
  print ("You are under weight")

# prompt: make a variable age, and if someone is 18 years or older, print that they are an adult. Otherwise print that they are a child. 

age = 27 

if age >= 18: 
  print ("Adult")
else: 
  print ("Child")