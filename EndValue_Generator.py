import csv

xVel = []
yVel = []
xPos = []
yPos = []
timeValues = []


def readData(speed, hatch):
    xCsv = r"C:\Users\aashm\Documents\Paraview\Time_Series\350_1000_130-x.csv"
    yCsv = r"C:\Users\aashm\Documents\Paraview\Time_Series\350_1000_130-y.csv"
    

    with open(xCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            timeValues.append(float(row[0]))
            xVel.append(float(row[1]))
    with open(yCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yVel.append(float(row[1]))
    

    
    createXPos(speed)
    createYPos(hatch)

    print("Speed:", speed, "     ", "Hatch:", hatch)
    print("Time             X         Y")
    print("----------------------------------")
    i = 0
    while i < len(timeValues):
        print(yPos[i])
        i = i + 1


def createXPos(speed):
    prevPos = 0.02
    xPos.append(prevPos)

    i = 0
    while i < len(timeValues) - 1:
        if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
            distance = (timeValues[i + 1] - timeValues[i]) * xVel[i]
            prevPos += distance
            xPos.append(round(prevPos, 6))
        elif xVel[i] == speed and xVel[i + 1] == 0:
            prevPos += 0.0001
            xPos.append(round(prevPos, 6))
        elif (xVel[i] * -1) == speed and xVel[i + 1] == 0:
            prevPos -= 0.0001
            xPos.append(round(prevPos, 6))
        else:
            xPos.append(round(prevPos, 6))

        i = i + 1


def createYPos(hatch):
    speed = 125
    prevPos = 0.02
    yPos.append(prevPos)

    i = 0
    while i < len(timeValues):
        if yVel[i] == speed and yVel[i + 1] == speed:
            prevPos += hatch
            yPos.append(round(prevPos, 6))
        elif yVel[i] == speed and yVel[i + 1] == 0:
            prevPos += 0.0001
            yPos.append(round(prevPos, 6))
        else:
            yPos.append(round(prevPos, 6))

        i = i + 1


readData(100, 0.013)