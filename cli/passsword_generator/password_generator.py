import random  
# this is a random module

# pip install pyfiglet
import pyfiglet

## generate ascii text
def print_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

print_ascii_art("Password Generator!")
print("---------------------------------------------------")
print("Generate a Password")

### list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz0123456789~@#$%^&*_+()"

## promt user 
passlength = int(input("Enter Password Length: "))

## generate password
newpassword = []

for x in range(passlength):
    ## append a random character to the password string
    newpassword.append(random.choice(characters))

## joint the whole list back into a string
finalpassword = ''.join(map(str, newpassword))

## showing the generated password
print("this is your new password: ", finalpassword)

