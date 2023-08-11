xVel = []
yVel = []
xPos = []
yPos = []
time = [0]


def createData(speed, hatch):
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

    createXPos(speed)
    createYPos(hatch)

    print("Speed:", speed, "     ", "Hatch:", hatch)
    print("Time             X         Y")
    print("----------------------------------")
    i = 0
    while i < len(time):
        print(time[i], "    ", xPos[i], "   ", yPos[i])
        i = i + 1


def createXPos(speed):
    prevPos = 0.02
    xPos.append(prevPos)

    i = 0
    while i < len(time) - 1:
        if abs(xVel[i]) == speed and abs(xVel[i + 1]) == speed:
            distance = (time[i + 1] - time[i]) * xVel[i]
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
    while i < len(time):
        if yVel[i] == speed and yVel[i + 1] == speed:
            prevPos += hatch
            yPos.append(round(prevPos, 6))
        elif yVel[i] == speed and yVel[i + 1] == 0:
            prevPos += 0.0001
            yPos.append(round(prevPos, 6))
        else:
            yPos.append(round(prevPos, 6))

        i = i + 1


createData(100, 0.013)
