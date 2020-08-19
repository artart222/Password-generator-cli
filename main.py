from csv import reader , writer
from random import randrange


#These are lists of characters that program can use to generate password
smlLetters = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" ,
"k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" ,
"x" , "y" , "z"]

capLetters = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" ,
"L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" ,
"Y" , "Z"]

numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
symbols = ["!" , "@" , "#" , "$" , "%"]


#genpass function generate password.
def genpass(useNumbers , useSymbols , useCapLetters , useSmlLetters , numbers , symbols , capLetters , lenOfPassword , nameOfPassword):
    #This is password. every time program choose character for password program add character to password string.
    password = ""

    #This is list of characters that program can use
    liOfChars = []
    if useNumbers == True:
        liOfChars.append(numbers)
    if useSymbols == True:
        liOfChars.append(symbols)
    if useCapLetters == True:
        liOfChars.append(capLetters)
    if useSmlLetters == True:
        liOfChars.append(smlLetters)

    for char in range(lenOfPassword):
        #choose characters
        choosingList = liOfChars[(randrange(0 , (liOfChars.index(liOfChars[-1]) + 1)))]
        choosingChar = choosingList[(randrange(0 , (choosingList.index(choosingList[-1]) + 1)))]
        password += choosingChar

    #write password in file.txt
    with open("./file.csv" , "a") as csvFile:
        csvReader = reader(csvFile)
        csvWriter = writer(csvFile)
        password = [nameOfPassword , password]
        csvWriter.writerow(password)


def boolInput(prompt):
    inputVal = input(prompt).capitalize().strip()

    while inputVal != "True" and inputVal != "False":
        print("Input is not True of False. please write with True of False")
        inputVal = input(prompt).capitalize().strip()

    if inputVal == "True":
        inputVal = True
    elif inputVal == "False":
        inputVal = False

    return inputVal


numOfPasswords = input("Please enter how many password you want: ")
while not numOfPasswords.isdigit() and not numOfPasswords > 0:
    print("\n" + "Entered value is not natural number. please enter natural number")
    numOfPasswords = input("Please enter how many password you want: ")
numOfPasswords = int(numOfPasswords)


for run in range(numOfPasswords):
    useNumbers = boolInput("\n" + "Do you want to use numbers? True of False: ")
    useSymbols = boolInput("Do you want to use symbols? True of False: ")
    useCapLetters = boolInput("Do you want to use capital letters? True of False: ")
    useSmlLetters = boolInput("Do you want to use small letters? True of False: ")

    while useNumbers == False and useSymbols == False and useCapLetters == False and useSmlLetters == False:
        print("\n" + "\n" + "All of options of password was False. please make one of them True. \n")
        useNumbers = boolInput("Do you want to use numbers? True of False: ")
        useSymbols = boolInput("Do you want to use symbols? True of False: ")
        useCapLetters = boolInput("Do you want to use capital letters? True of False: ")
        useSmlLetters = boolInput("Do you want to use small letters? True of False: ")


    nameOfPassword = input("\n" + "What is name of this password? ")
    while nameOfPassword == "":
        nameOfPassword = input("You must choose name for password. please enter something: ")

    lenOfPassword = int(input("\n" + "How much is length of password?(maximum is 4096) "))
    while lenOfPassword > 4096 or lenOfPassword < 1:
        print("\n" + "You entered number that was bigger than 4096 or lower than 1. please enter smaller or bigger number.(maximum is 4096)")
        lenOfPassword = int(input("How much is length of password?(maximum is 4096) "))


    genpass(useNumbers , useSymbols , useCapLetters , useSmlLetters , numbers , symbols , capLetters , lenOfPassword , nameOfPassword)
