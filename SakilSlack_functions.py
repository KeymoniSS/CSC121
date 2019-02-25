# Keymoni Sakil-Slack
# 01/24/2019
# SakilSlack_functions
# This program calculates the gross pay for a user

FWT = .02
SWT = .01

def displayInfo():
    print("My name is Keymoni Sakil-Slack.\nThis program will caluclate your gross and net pay.")
    print("==================================================")
    
def getHours():
    hours = float(input("Enter the hours worked: "))
    return hours

def getRate():
    rate = float(input("Enter the rate worked: "))
    return rate
        
def getGrossPay(hours, rate):
    grossPay = hours * rate
    return grossPay

def getSWT(hours, rate):
    swt = (hours * rate) * SWT
    return swt

def getFWT(hours, rate):
    fwt = (hours * rate) * FWT
    return fwt

def getNetPay(grossPay, swt, fwt):
    netPay = grossPay - swt - fwt
    return netPay

def displayValues(grossPay, netPay):
    print("\nGross Pay:\t$", grossPay)
    print("SWT:\t\t$", (SWT * 100))
    print("FWT:\t\t$", (FWT * 100))
    print("Net Pay:\t$", netPay)
    
if __name__ == "__main__":
    main()

