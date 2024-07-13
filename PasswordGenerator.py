import string
import random

typeOfPassword = "1"

while typeOfPassword == "1" or typeOfPassword == "2":
    typeOfPassword = input("Would you like to generate a completely random password(1) or a random word password(2)? Enter anything else to quit the program. ")
    if typeOfPassword == "1":
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!" + "?" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "(" + ")"
        length = int(input("Enter a length for your password: "))
        password = ""

        for i in range(0, length):
            password+=letters[random.randint(0, len(letters))]
        print(password)

    elif typeOfPassword == "2":
        password = ""
        with open("C:\\Users\\limin\\Downloads\\words.txt", 'r') as file:
            numWords = int(input("How many words would you like your RWP to be? "))
            maxLenWord = int(input("Add a maximum length for words: "))
            words = []
            for i in range(0, numWords):
                for line in file:
                    line = line.strip()
                    if len(line) <= maxLenWord:
                        words.append(line)

        for i in range(0, numWords):
            password+=words[random.randint(0, len(words))] + " "
        print(password)
