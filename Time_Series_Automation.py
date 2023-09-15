import csv
import matplotlib.pyplot as plt

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
    xCsv = r"C:\Users\aashm\Documents\Paraview\Time_Series\350_1000_130-x.csv"
    yCsv = r"C:\Users\aashm\Documents\Paraview\Time_Series\350_1000_130-y.csv"
    pCsv = (
        r"C:\Users\aashm\Documents\Paraview\Time_Series\350_1000_130-power.csv"
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
        intialPos = prevPos
        while timeValues[i + 1] > curTimeStep:
            if yVel[i] == speed and yVel[i + 1] == speed:
                print(prevPos-initialPos)
                dy = dt * yVel[i]
                prevPos += dy
                yArr.append(round(prevPos, 6))
            elif yVel[i] == speed and yVel[i + 1] == 0:
                prevPos += 0.0001
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
    prevTime = timeStep[len(timeStep) - 2]
    camPrevXPos = camXPos[len(timeStep) - 1]
    camPrevYPos = camYPos[len(timeStep) - 1]
    clipPrevXPos = clipXPos[len(timeStep) - 1]
    clipPrevYPos = clipYPos[len(timeStep) - 1]

    if len(timeStep) != numSteps:
        while len(timeStep) != numSteps:
            prevTime += dt
            timeStep.append(prevTime)
            camXPos.append(camPrevXPos)
            camYPos.append(camPrevYPos)
            clipXPos.append(clipPrevXPos)
            clipYPos.append(clipPrevYPos)
            checkPower.append(True)



readCsv()
#createData(100, 0.013)
createPowerPos()
createXPos(100, 0.02, camXPos)
createYPos(0.02, camYPos)
createXPos(100, -0.015, clipXPos)
createYPos(-0.015, clipYPos)
fillValues()
timeStep.insert(0, 0)
clipXPos.insert(0, -0.015)
clipYPos.insert(0, -0.015)
camXPos.insert(0, 0.02)
camYPos.insert(0, 0.02)


print("Speed:", 100, "     ", "Hatch:", 0.013)
print("#       Time             Xcam        Ycam        Xclip        YClip")
print("-------------------------------------")
i = 0

while i < len(timeStep):
    time = timeStep[i]
    scientific_notation = format(time, ".2e")
    timeStep[i]=scientific_notation
    
    i = i + 1

print(timeStep)


def remove_last_two_elements(input_array):
    # Check if the input_array has at least two elements
    if len(input_array) >= 2:
        # Use slicing to remove the last two elements and create a new list
        result_array = input_array[:-1]
        return result_array
    else:
        # If the input_array has less than two elements, return an empty list
        return []


endTimes =[0.0,0.001,0.0010008,0.0011048,0.0011056,0.0021056,0.0021064,0.0022104,0.0022112,0.0032112,0.003212,0.003316,0.0033168,0.0043168,0.0043176,0.0044216,0.0044224,0.0054224,0.0054232,0.0055272,0.005528,0.006528,0.0065288]
camXEndPoints= [0.02,0.12,0.1201,0.1201,0.1201,0.0201,0.02,0.02,0.02,0.12,0.1201,0.1201,0.1201,0.0201,0.02,0.02,0.02,0.12,0.1201,0.1201,0.1201,0.0201,0.02]
camYEndPoints =[0.02,0.02,0.02,0.033,0.0331,0.0331,0.0331,0.0461,0.0462,0.0462,0.0462,0.0592,0.0593,0.0593,0.0593,0.0723,0.0724,0.0724,0.0724,0.0854,0.0855,0.0855,0.0855]

fig, axs = plt.subplots(1, 2)

axs[0].plot(remove_last_two_elements(clipXPos), clipYPos)
axs[0].set_title('Line Plot of X and Y Clip')

axs[1].plot(camXEndPoints, camYEndPoints,'o', markersize=1, label='Data Points')

axs[1].plot(remove_last_two_elements(camXPos), camYPos)
axs[1].set_title('Line Plot of X and Y Cam')


plt.grid(True)  # Add gridlines (optional)
plt.tight_layout()
plt.show()
