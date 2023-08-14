import numpy
import csv

xVel = []
yVel = []
xPos = []
yPos = []
time = []
timeStep = []
numSteps = 355


def readCsv():
    xCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-x.csv"
    yCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-y.csv"

    with open(xCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            time.append(float(row[0]))
            xVel.append(float(row[1]))
    with open(yCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yVel.append(float(row[1]))


def createData(speed, hatch):
    time.append(0)
    timeStep.append(0)

    xduration = 0.1 / speed
    yduration = hatch / 125

    count = 0
    prevtime = 0

    check = False

    for x in range(11):
        curSpeed = speed

        if count % 2 == 0:
            if count % 4 != 0:
                curSpeed *= -1

            if check:
                prevtime += 0.0000008
                rounded_number = round(prevtime, 8)
                time.append(rounded_number)
            xVel.append(curSpeed)
            yVel.append(0)
            prevtime += xduration
            xVel.append(curSpeed)
            yVel.append(0)
            rounded_number = round(prevtime, 8)
            time.append(rounded_number)
            check = True
        else:
            prevtime += 0.0000008
            rounded_number = round(prevtime, 8)
            time.append(rounded_number)
            yVel.append(125)
            xVel.append(0)
            prevtime += yduration
            yVel.append(125)
            xVel.append(0)
            rounded_number = round(prevtime, 8)
            time.append(rounded_number)

        count += 1
    prevtime += 0.0000008
    rounded_number = round(prevtime, 8)
    time.append(rounded_number)
    yVel.append(0)
    xVel.append(0)


def createXPos(speed):
    dt = 0.00002
    prevPos = 0
    xPos.append(prevPos)

    i = 0

    curTimeStep = 0

    while i < len(time) - 1:
        while time[i + 1] > curTimeStep:
            if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
                dx = dt * xVel[i]
                prevPos += dx
                xPos.append(round(prevPos, 6))
            else:
                xPos.append(round(prevPos, 6))
            curTimeStep += dt
            timeStep.append(round(curTimeStep, 6))
        i = i + 1


def createYPos():
    dt = 0.00002
    speed = 125
    prevPos = 0
    yPos.append(prevPos)

    i = 0

    curTimeStep = timeStep[i]

    while i < len(time) - 1:
        while time[i + 1] > curTimeStep:
            if yVel[i] == speed and yVel[i + 1] == speed:
                dy = dt * yVel[i]
                prevPos += dy
                yPos.append(round(prevPos, 6))
            else:
                yPos.append(round(prevPos, 6))
            curTimeStep += dt

        i = i + 1


readCsv()
# createData(100, 0.013)
createXPos(100)
createYPos()

print("Speed:", 100, "     ", "Hatch:", 0.013)
print("#       Time             X         Y")
print("-------------------------------------")
i = 0
while i < len(timeStep):
    print(i, "     ", timeStep[i], "        ", xPos[i], "   ", yPos[i])
    i = i + 1
