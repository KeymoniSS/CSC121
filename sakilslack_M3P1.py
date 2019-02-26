# This program will find the lowest, highest, total and average of 20 numbers
# Keymoni Sakil-Slack
# sakilslack_M3P1
# 02-26-2019

def getNums():
    mylist = []
    for i in range(20):
        num = int(input("Enter number #" + str(i+1)+": "))
        mylist.append(num)
    return mylist

def getHigh(listThing):
    highest = max(listThing)
    print("The highest number is " + str(highest))
     
def getLow(listThing):
    lowest = min(listThing)
    print("The lowest number is " + str(lowest))
    
def getTotal(listThing):
    total = 0
    for num in listThing:
        total += num
    print("The total is " + str(total))
    
def getAvg(listThing):
    total = 0
    count = 0
    avg = 0
    for num in listThing:
        count = count + 1
        total += num
    avg = total/count
    print("The average is " + str(avg))
    
def main():
    print("This program will find the lowest, highest, total and average of 20 numbers")
    print("Please enter 20 numbers")
    print("-" * 85)
    listThing = getNums()
    print("-" * 85)
    getHigh(listThing)
    getLow(listThing)
    getTotal(listThing)
    getAvg(listThing)
    
if __name__ == "__main__":
    main()
