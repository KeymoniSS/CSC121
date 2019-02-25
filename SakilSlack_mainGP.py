# Keymoni Sakil-Slack
# 01/24/2019
# SakilSlack_mainGP
# This program calculates the gross pay for a user

import SakilSlack_functions as GP

def main():
    GP.displayInfo()
    hours = GP.getHours()
    rate = GP.getRate()
    grossPay = GP.getGrossPay(hours, rate)
    swt = GP.getSWT(hours, rate)
    fwt = GP.getFWT(hours, rate)
    netPay = GP.getNetPay(grossPay, swt, fwt)
    display_values = GP.displayValues(grossPay, netPay)

if __name__ == "__main__":
    main()
