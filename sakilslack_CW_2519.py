# This program will create a schedule
# Keymoni Sakil-Slack
# 02-5-2019

num = int(input("How many employees do you want to enter: "))

def main():
    with open("employee_pay.txt", "w") as outfile:
        for count in range(1,num +1):
            print ("Employee " + str(count))
            fname = (input("Enter the employee's first name: "))
            lname = (input("Enter the employee's last name: "))
            etitle = (input("Enter the employee's title: "))
            payRate = float(input("Enter the employee's pay rate (up to 99.99): "))
            if payRate > 99.99:
                print("Please enter a valid pay rate.")
                payRate = float(input("Enter the employee's pay rate (up to 99.99): "))
            hours = int(input("Enter the hours the employee worked this week (up to 99): "))
            if hours > 99:
                print("Please enter valid hours.")
                hours = int(input("Enter the hours the employee worked this week (up to 99): "))
            grossPay = payRate * hours 
            wname = fname.lower() + lname.lower()
            etitle = etitle.lower()
            outfile.write ("Employee " + str(count) + "\n")
            outfile.write ("===============================================\n")
            outfile.write (str("Name").ljust(20))
            outfile.write (str("Title").ljust(10))
            outfile.write (str("Pay").ljust(5))
            outfile.write (str("Hrs").ljust(3))
            outfile.write (str("Gross Pay").ljust(8))
            outfile.write ("\n===============================================\n")
            outfile.write (wname.ljust(20))
            outfile.write (etitle.ljust(10))
            outfile.write ("$" + str(int(payRate)).ljust(4) + "|")
            outfile.write ("$" +str(int(hours)).ljust(2) + "|")
            outfile.write ("$" +str(int(grossPay)).ljust(6) + "\n\n")
        
if __name__ == "__main__":
    main()
