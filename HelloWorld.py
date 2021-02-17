hello = 'Hello World!'
print(hello)
#Ask user for name

name = input('What is your name?: ')

#ask user for age

age = input('What is your age?: ')
print(type(age))
#Ask user for City
City = input('Which city do you live in?: ')
#Ask user what they enjoy
Love = input('what do to love to do?; ')
# Output
Output = "Your name is " + name + ". You are of " + age + "years of age. you live in " + City + ". You love to" + Love + "."
Output1 = "My name is {0}. I am {1} of age. I live in {2}. I love to {3}.".format(name, age, City, Love)
#print Output to screen
print(Output)
print(Output1)
