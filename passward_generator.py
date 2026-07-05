import secrets
import string

print("\n*********************PASSWARD GENERATOR*******************************\n\n")
print("----------------------------------------------------------------------------")
length = int(input("Enter password length:\n"))
print("----------------------------------------------------------------------------\n")
characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += secrets.choice(characters)
print("----------------------------------------------------------------------------")
print("\nGenerated Password:\n", password)