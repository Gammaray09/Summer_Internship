import numpy
import csv

xVel = []
yVel = []
camXPos = []
camYPos = []
clipXPos = []
clipYPos = []
timeValues = []
timeStep = []
power = []
checkPower = []
numSteps = 355


def readCsv():
    xCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-x.csv"
    yCsv = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-y.csv"
    pCsv = (
        r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series\400_1000_130-power.csv"
    )

    with open(xCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            timeValues.append(float(row[0]))
            xVel.append(float(row[1]))
    with open(yCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            yVel.append(float(row[1]))
    with open(pCsv, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            power.append(float(row[1]))

    for x in power:
        print(x)


def createData(speed, hatch):
    timeValues.append(0)
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
                timeValues.append(rounded_number)
            xVel.append(curSpeed)
            yVel.append(0)
            prevtime += xduration
            xVel.append(curSpeed)
            yVel.append(0)
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)
            check = True
        else:
            prevtime += 0.0000008
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)
            yVel.append(125)
            xVel.append(0)
            prevtime += yduration
            yVel.append(125)
            xVel.append(0)
            rounded_number = round(prevtime, 8)
            timeValues.append(rounded_number)

        count += 1
    prevtime += 0.0000008
    rounded_number = round(prevtime, 8)
    timeValues.append(rounded_number)
    yVel.append(0)
    xVel.append(0)


def createXPos(speed, initialPos, xArr):
    arrFull = False
    if len(timeStep) > 1:
        arrFull = True

    dt = 0.00002
    prevPos = initialPos
    xArr.append(prevPos)

    i = 0

    curTimeStep = 0

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
                dx = dt * xVel[i]
                prevPos += dx
                xArr.append(round(prevPos, 6))
            else:
                xArr.append(round(prevPos, 6))
            curTimeStep += dt

            if arrFull == False:
                timeStep.append(curTimeStep)
        i = i + 1


def createYPos(initialPos, yArr):
    dt = 0.00002
    speed = 125
    prevPos = initialPos
    yArr.append(prevPos)

    i = 0

    curTimeStep = timeStep[i]

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if yVel[i] == speed and yVel[i + 1] == speed:
                dy = dt * yVel[i]
                prevPos += dy
                yArr.append(round(prevPos, 6))
            else:
                yArr.append(round(prevPos, 6))
            curTimeStep += dt

        i = i + 1


def createPowerPos():
    dt = 0.00002
    i = 0

    curTimeStep = i

    while i < len(timeValues) - 1:
        while timeValues[i + 1] > curTimeStep:
            if power[i] > 0:
                checkPower.append(True)
            else:
                checkPower.append(False)
            curTimeStep += dt

        i = i + 1


def fillValues():
    dt = 0.00002
    prevTime = timeStep[len(timeStep) - 1]
    camPrevXPos = camXPos[len(timeStep) - 1]
    camPrevYPos = camYPos[len(timeStep) - 1]
    clipPrevXPos = clipXPos[len(timeStep) - 1]
    clipPrevYPos = clipYPos[len(timeStep) - 1]

    if len(timeStep) != numSteps:
        while len(timeStep) != numSteps + 1:
            prevTime += dt
            timeStep.append(prevTime)
            camXPos.append(camPrevXPos)
            camYPos.append(camPrevYPos)
            clipXPos.append(clipPrevXPos)
            clipYPos.append(clipPrevYPos)
            checkPower.append(True)


readCsv()
# createData(100, 0.013)
createPowerPos()
createXPos(100, 0.02, camXPos)
createYPos(0.02, camYPos)
createXPos(100, -0.015, clipXPos)
createYPos(-0.015, clipYPos)
fillValues()


print("Speed:", 100, "     ", "Hatch:", 0.013)
print("#       Time             X         Y")
print("-------------------------------------")
i = 0
while i < len(timeStep):
    time = timeStep[i]
    scientific_notation = format(time, ".2e")
    print(
        i,
        "     ",
        scientific_notation,
        "        ",
        camXPos[i],
        "   ",
        camYPos[i],
        "      ",
    )
    i = i + 1
