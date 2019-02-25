# This program will create a schedule
# Keymoni Sakil-Slack
# sakilslackFE1
# 01-31-2019


def displayMenu():
    print("File Assisnments Menu")
    print("=========================================")
    print("1. Create Schedule File")
    print("2. Create Report File")
    print("3. Exit")
    print("=========================================" + "\n")

def createSchedule():
    fname = (input("Enter your first name: "))
    lname = (input("Enter your last name: "))
    num = int(input("How many classes do you want to enter: "))
    wname = fname.lower() + lname.lower()
    with open("schedule.txt", "w") as outfile:
        for count in range(1,num +1):
            course = (input("Enter a class name(EX: cis115): "))
            days = (input("Enter the days the class meet(EX: mtwthf): "))
            sTime = (input("Enter the start time of the class(EX: 10): "))
            eTime = (input("Enter the end time of the class(EX: 12): "))
            time = sTime + eTime
            course = course.lower()
            days = days.lower()
            outfile.write (wname.ljust(20) + course.ljust(6) + days.ljust(6) + time + "\n")

def createReport():
    fname = (input("Enter your first name: "))
    lname = (input("Enter your last name: "))
    num = int(input("How many classes do you want to enter: "))
    wname = fname.lower() + lname.lower()
    header = ("Student Name 2019 Spring Schedule")
    className = ("Class name")
    meetingDays = ("Meeting Days")
    meetingTimes = ("Meeting Times")
    with open("report.txt", "w") as outfile:
        outfile.write (header.center(60) + "\n")
        outfile.write (className.ljust(10) + "  " + meetingDays.ljust(10)  +  "  "
                       +  meetingTimes.ljust(10) + "\n")
        for count in range(1,num +1):
            course = (input("Enter a class name(EX: cis115): "))
            days = (input("Enter the days the class meet(EX: mtwthf): "))
            sTime = (input("Enter the start time of the class(EX: 10): "))
            eTime = (input("Enter the end time of the class(EX: 12): "))
            time = sTime + eTime
            course = course.lower()
            days = days.lower()
            #for count in range(1,num +1):
            outfile.write (course.ljust(12) + days.ljust(14)
                       + sTime.ljust(2) + "-" + eTime.ljust(2) + "\n")

def main():
    contain = "y"
    while contain.lower() == "y":
        displayMenu()
        menuChoice = input("Enter your menu choice: ")
        if menuChoice == "1":
            createSchedule()
            print("\n")
        elif menuChoice == "2":
            createReport()
            print("\n")
        elif menuChoice == "3":
            break
        else:
            print ("You chose a invalid choice")
            contain = (input("Would you like to make another choice? (y/n): "))
            print("\n")

if __name__ == "__main__":
    main()
