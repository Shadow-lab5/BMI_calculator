import random

print("Welcome to Password Generator")

char_lowercase = "abcdefghijklmnopqrstuvwxyz"

char_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

int_digit = "0123456789"

punctuation = "!@#$%^&*"

password_length = int(input("Enter the required length of password\n"))

total_characters = []
total_characters.extend(list(char_lowercase))
total_characters.extend(list(char_uppercase))
total_characters.extend(list(int_digit))
total_characters.extend(list(punctuation))
 
random.shuffle(total_characters)

print("your password with desired length", password_length,"is")

print("".join(total_characters[0:password_length]))                                                                                                                                                              
