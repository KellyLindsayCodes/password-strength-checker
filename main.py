"""
Password Strength Checker

Project Scope: User is prompted by the terminal to enter in their password. 
Terminal outputs if password is weak, moderate or strong.

The strength of the password is determined by a scoring system.

Factors that influence password strength:
- password length
- password contains at least 1 uppercase
- password contains at least 1 lowercase
- password contains at least 1 number 
- password contains at least 1 symbol 

Please note if there is a space at either one or both the start and end of the password,
or if an accented character is used, then the terminal will tell the user that the password is invalid.
The user will be then prompted to enter a new password. 

"""
#I will first define what I want the terminal to output. This will also define password as a variable for future functions. 
#Input is used so that the user can then input their own password into the terminal.
#Rounded brackets are used here to indicate that input is a function. 
#Double quotations are used for "Enter your password: " to indicate a string. What the user types in response is stored as a string in the password variable. 
password = input("Enter your password: ")

#Now I will create functions for the password strength variables, which will determine the overall score of the password.
#I will begin with the boolean variables. Password Length is not a boolean variable as it will have multiple conditonals. This will be covered afterwards.

#Variables for uppercase, lowercase, numbers and symbols list.
#First I will define all password-related character sets as strings to specify what the function will need to check.    
# List of all possible upper case characters
alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# List of all possible lower case characters
alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# List of all numeric characters
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# List of all symbol characters
symbols_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "/", "<", ">", "?", "\\", "|"]

# Now I will create a function based on these variables. In this case, I will use a for loop. 
# Each variable, except for the password length is a boolean, i.e yes (True) = 1 point and no (False) = 0 points. 
# In order for the for loop to work, I need to define each boolean as false so that it has a starting score of 0.
# The for loop runs through each character in the password and determines which category it fits into using if else statements.
# When the loop registers a true, e.g. it has found a lowercase letter, it will set the relevant boolean to true.
# Once all characters have been checked, the total number of true booleans is summed.

lower_found = False
upper_found = False
number_found = False
symbol_found = False

for current_character in password:
    if current_character in alphabet_lower:
        lower_found = True
    elif current_character in alphabet_upper:
        upper_found = True
    elif current_character in number_list:
        number_found = True
    elif current_character in symbols_list:
        symbol_found = True

score = lower_found + upper_found + number_found + symbol_found

# Now I will create the password length variable. 
# To define password length, I will use len or length as a built-in function, just like you would use 'input' or 'print'. (I will leave an acknowledgement at the end of the file for where I found this, in case you want to have a look too.)  
# len will calculate the number of characters in the password string. It will give you an integer value that is stored in password_length. 
# Next, I've created the variable threshold_list. This contains a list of integers.
# Each integer in threshold_list is a threshold for rewarding a point based on the length of the password. e.g. a threshold of 8 will reward a point if the password is at least 8 characters long.
# The for loop is used to run through each integer (as n) in the threshold_list. If the password length is equal to or greater than the threshold, then 1 point is added to the score using "score+1".
# For example, the loop would run and if the password is more than 8 characters or equal to ( >= ) then it would provide 1 point. The loop would then run again and if it has more than 12 characters or equal to then it would provide another point, and so on.  

password_length = len(password)
threshold_list = [8,12,16,20]

for n in threshold_list:
    if password_length>=n:
        score = score+1 

# Please note, I have added a password strength score here for testing purposes to ensure that the points are adding up correctly. I'm not sure yet whether I will keep this in the final draft. 

print("Password strength score:", score)

# Finally, I will need to determine the strength of the password. 
# I have used an if/else statement for this.
# elif is used as there are three conditionals. 
# Weak = rating/overall score of less than 3, Moderate = 3 or more and less than 5, Strong = 5 or more. 
# Print function is used to tell the user the strength rating that has been allocated to their password. 

if score < 3:
    strength = 'Weak'
elif score < 5:
    strength = 'Moderate'
else:
    strength = 'Strong'

print(strength)


"""
Issues to still consider - 
- I haven't added a feature as to having no spaces at the start and end of the password.
- I haven't added a feature as to disallowing the use of accented characters.
- I don't have anything set in place to prevent the use of common words, or common passwords etc. 
- In the original plan, I had a section for feedback to suggest how the user could improve their password. Moving forward, I'm not sure whether I want to add this back in or not. 

"""

"""
Acknowledgements/ References 
I googled what makes a strong password, which I then used to base my variables and conditions on of what makes a weak, moderate or strong password. 

According to Microsoft -
A strong password is: At least 12 characters long but 14 or more is better. A combination of uppercase letters, lowercase letters, numbers, and symbols. Not a word that can be found in a dictionary or the name of a person, character, product, or organization.
Source : Create and use strong passwords - Microsoft Support
https://support.microsoft.com/en-au/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb#:~:text=A%20strong%20password%20is%3A,character%2C%20product%2C%20or%20organization.

Likewise Google suggests - 
Use a combination of uppercase and lowercase letters, numbers, and symbols (except symbols or characters with accents, like ñ or â).
Avoid common passwords like “password123”; they will be easier to guess.
Don’t create a password beginning or ending with a blank space.
Make it harder to guess your password by avoiding very common words, phrases, and patterns. These might include words like “password” or “letmein”, sequences like “abcdef” or “123456”, or keyboard patterns like “qwerty” or “qazwsx”.

https://guidebooks.google.com/online-security/protect-your-google-account/create-strong-password?hl=en


For the len function as per line 70, I googled "list of built in functions in python" and found this website - 
https://www.w3schools.com/python/python_ref_functions.asp


"""