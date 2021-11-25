import random

length = int(input("How long do you want your password? "))

x = input("Do you want symbols? Yes/No ")
if x == "Yes":
    isSymbol = True
else:
    isSymbol = False

x = input("Do you want numbers? Yes/No ")
if x == "Yes":
    isNumber = True
else:
    isNumber = False

x = input("Do you want uppercase characters? Yes/No ")
if x == "Yes":
    isUpper = True
else:
    isUpper = False

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
symbols = ["!", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "|", "@", "#", "~", "{", "[", "]", "}", "+", "*", "ç", ",",
           ";", "─", ".", ":", "-", "_"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]

if isNumber:
    for n in numbers:
        chars.append(n)
if isSymbol:
    for s in symbols:
        chars.append(s)
if isUpper:
    for u in upper:
        chars.append(u)

password_array = []
for i in range(length):
    password_array.append(random.choice(chars))

password = "".join(password_array)
print(password)
