# This program will create a file and test for exceptions
# Keymoni Sakil-Slack
# sakilslackFE2
# 02-12-2019


def displayMenu():
    print("Menu")
    print("=" * 55)
    print("1. Create text file")
    print("2. Average Values")
    print("3. Total Values")
    print("4. Test for File Exception")
    print("5. Test for Value Error Exception")
    print("6. Exit Program")
    print("=" * 55 + "\n")

def createTextFile():
    print("\n")
    try:
        num = int(input("Enter how many numbers you want to get from the user: "))

        with open("numbers.txt", "w") as outfile:
            for count in range(1, num +1):
                number = int(input("enter a number: "))
                outfile.write(str(number) + "\n")
    except ValueError:
        print("Incorrect entry. Entries should be integers!")
    
def getAverage():
    print("\n")
    with open("numbers.txt", "r") as infile:
        total = 0
        count = 0
        average = 0
        for line in infile:
            value = int(line)
            count = count + 1
            total = total + value
        average = total/count
        print("The average is " + str(average))
            
def getTotal():
    print("\n")
    with open("numbers.txt", "r") as infile:
        total = 0
        count = 0
        for line in infile:
            value = int(line)
            count = count + 1
            total = total + value
        print("The total is " + str(total))

def testFileException():
    print("\n")
    try:
        with open("numbernot.txt", "r") as infile:
            print("I found some data in a file. Here's all the data listed in the file: ")
            total = 0
            count = 0
            for line in infile:
                value = int(line)
                count = count + 1
                total = total + value
                print(value)    
    except IOError:
        print("-" * 75)
        print("File not found or corrupt")
        print("Please recheck the file name, make sure you have chose the correct file,")
        print("or make sure the file has been created")
        print("-" * 75)
        
def testValueErrorException():
    print("\n")
    try:
        with open("numberserror.txt", "r") as infile:
            total = 0
            count = 0
            for line in infile:
                value = int(line)
                count = count + 1
                total = total + value

    except ValueError:
        with open("numberserror.txt", "r") as infile:
            lines = infile.readlines()
            error = lines[count]
            error = error.rstrip()
        print("-" * 55)
        print("!!ERROR: Bad Data!!")
        print("The character '" + str(error) + "' is bad data. It is present in line " + str(count + 1))
        print("Please note, all entries should be integers!" )
        print("-" * 55)

    else:
        print("There's no errors present in this file")

def main():
    contain = "y"
    while contain.lower() == "y":
        displayMenu()
        menuChoice = input("Enter your menu choice: ")
        if menuChoice == "1":
            createTextFile()
            print("\n")
        elif menuChoice == "2":
            getAverage()
            print("\n")
        elif menuChoice == "3":
            getTotal()
            print("\n")
        elif menuChoice == "4":
            testFileException()
            print("\n")
        elif menuChoice == "5":
            testValueErrorException()
            print("\n")
        elif menuChoice == "6":
            print ("You have exited the program. Thank you, have a nice day!")
            break
        else:
            print ("\nYou chose a invalid choice")
            print ("Please choose a valid menu option.\n")
            
if __name__ == "__main__":
    main()
