# This program will create a report for users that will list their student id number, last name, and first name, username and email address. 
# Keymoni Sakil-Slack
# sakilslackM4P1
# 03-05-2019

def main():
    school = ("@student.faytechcc.edu")
    header = ("Student Login Information")
    with open("studentReport.txt", "w") as outfile:
        outfile.write (header.center(78) + "\n")
        outfile.write ("Last".ljust(10) + "First".ljust(10) + "ID Num".ljust(10) + "login ID".ljust(14) + "Email".ljust(34) + "\n")
        with open("studentinfo.txt", "r") as infile:
            for line in infile:
                row = line[0:28]
                lname = line[0:10]
                fname = line[10:20]
                studentId = line[20:28]
                #Finds the first 7 letters of last name, first letter of first name, and last 4 digits of student ID
                trimlname = lname[0:7].lower().rstrip()
                trimfname = fname[0:1].lower().rstrip()
                trimId = studentId[4:8]
                #Combine trim to construct login
                login = trimlname + trimfname + trimId 
                email = login + school
                outfile.write (lname.ljust(10) + fname.ljust(10) + studentId.ljust(10) + login.ljust(14) + email.ljust(34) + "\n")

if __name__ == "__main__":
    main()
