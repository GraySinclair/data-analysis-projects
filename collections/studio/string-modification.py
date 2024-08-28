my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
""" first3 = my_string[:3]
leftover = my_string[3:]
newstr = leftover + first3
print(newstr)

# Use a template literal to print the original and modified string in a descriptive phrase.
print(f'The original string is {my_string} and the new string is {newstr}.') """

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
default_input = input('How many letters should I remove from the front and add to the end?:')

if default_input > len(my_string):
    default_input = 3
else:
    changestr = my_string[:default_input]

my_string.remove(changestr)

print(my_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
