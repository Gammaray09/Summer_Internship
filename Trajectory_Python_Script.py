import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import csv


def ReadLaserTrajectory(loc, s, h):
    print("runTraj")
    P0 = 400
    locF = loc + "\\"
    fnameP = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-power.csv"
    fnamex = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-x.csv"
    fnamey = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-y.csv"

    def read_csv_as_float(filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            data = np.array([list(map(float, row)) for row in reader])
        return data

    Fp = read_csv_as_float(fnameP)
    Fx = read_csv_as_float(fnamex)
    Fy = read_csv_as_float(fnamey)

    # Read data from the second column of the first CSV file
    Ft = Fx[:, 0]
    Fp = Fp[:, 1]
    Fx = Fx[:, 1]
    Fy = Fy[:, 1]

    dat = np.column_stack((Ft, Fx, Fy, Fp))

    return dat


def GetLaserTrajectory(dat, x0, y0, t0, dt, Nt, ap):
    nFac = 10
    ap1, ap2 = ap
    t = t0 + dt * np.linspace(0, Nt - 1, Nt)

    p = np.zeros(Nt)
    x = np.zeros(Nt)
    y = np.zeros(Nt)
    vx = np.zeros(Nt)
    vy = np.zeros(Nt)

    tLim, vxLim, vyLim, pLim = dat.T

    Nlim = len(dat)
    dtLim = np.diff(tLim)
    dtm = np.min(dtLim) / nFac
    tM = np.max(t)
    NtL = int(np.ceil(tM / dtm)) + 1

    tL = t0 + dtm * np.linspace(0, NtL - 1, NtL)

    # print(max(tL))
    # print(max(t))

    pL = np.zeros(NtL)
    xL = np.zeros(NtL)
    yL = np.zeros(NtL)
    vxL = np.zeros(NtL)
    vyL = np.zeros(NtL)

    for i in range(1, NtL):
        for j in range(Nlim - 1):
            if tL[i] < tLim[0]:
                pL[i], vxL[i], vyL[i] = pLim[0], vxLim[0], vyLim[0]
                break
            elif tLim[j] <= tL[i] < tLim[j + 1]:
                tFac = (tL[i] - tLim[j]) / (tLim[j + 1] - tLim[j])
                if ap1 == 1:
                    pL[i] = pLim[j] + tFac * (pLim[j + 1] - pLim[j])
                    vxL[i] = vxLim[j] + tFac * (vxLim[j + 1] - vxLim[j])
                    vyL[i] = vyLim[j] + tFac * (vyLim[j + 1] - vyLim[j])
                else:
                    pL[i], vxL[i], vyL[i] = pLim[j], vxLim[j], vyLim[j]
                break
            elif tL[i] >= tLim[Nlim - 1]:
                pL[i], vxL[i], vyL[i] = pLim[Nlim - 1], vxLim[Nlim - 1], vyLim[Nlim - 1]

    xL[0], yL[0] = x0, y0
    for i in range(1, NtL):
        if ap2 == 1:
            xL[i] = xL[i - 1] + 0.5 * dtm * (vxL[i - 1] + vxL[i])
            yL[i] = yL[i - 1] + 0.5 * dtm * (vyL[i - 1] + vyL[i])
        else:
            xL[i] = xL[i - 1] + dtm * vxL[i - 1]
            yL[i] = yL[i - 1] + dtm * vyL[i - 1]

    p = np.interp(t, tL, pL)
    vx = np.interp(t, tL, vxL)
    vy = np.interp(t, tL, vyL)
    x = np.interp(t, tL, xL)
    y = np.interp(t, tL, yL)

    pOn = p != 0

    datTraj = {"t": t, "x": x, "y": y, "vx": vx, "vy": vy, "p": p, "pOn": pOn}

    return datTraj


def runTraj():
    loc = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series"
    Nt = 356
    xCam = 0.02
    yCam = 0.02
    t0 = 0
    dt = 2e-5
    s = 1000
    h = 130
    dat = ReadLaserTrajectory(loc, s, h)
    datTrajCam = GetLaserTrajectory(dat, xCam, yCam, t0, dt, Nt, [1, 1])

    timeStep = datTrajCam.get("t")
    camXPos = datTrajCam.get("x")
    camYPos = datTrajCam.get("y")

    return timeStep, camXPos, camYPos


timeStep, camXPos, camYPos = runTraj()
print(camYPos)
