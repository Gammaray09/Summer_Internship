import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


def ReadLaserTrajectory(loc, s, h):
    P0 = 350
    locF = loc + "\\"
    fnameP = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-power.csv"
    fnamex = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-x.csv"
    fnamey = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-y.csv"

    Fp = pd.read_csv(fnameP, header=None).values
    Fx = pd.read_csv(fnamex, header=None).values
    Fy = pd.read_csv(fnamey, header=None).values

    dat = np.column_stack((Fx, Fy[:, 1], Fp[:, 1]))

    return dat


def GetLaserTrajectoryMod(dat, x0, y0, t0, dt, Nt):
    t = t0 + dt * np.linspace(0, Nt - 1, Nt)
    p = np.zeros(Nt)
    x = np.zeros(Nt)
    y = np.zeros(Nt)
    vx = np.zeros(Nt)
    vy = np.zeros(Nt)

    tLim = dat[:, 0]
    vxLim = dat[:, 1]
    vyLim = dat[:, 2]
    pLim = dat[:, 3]

    Nlim = dat.shape[0]
    dtLim = np.diff(tLim)
    dtm = np.min(dtLim)
    tM = np.max(t)
    NtL = int(np.ceil(tM / dtm))
    tL = t0 + dtm * np.linspace(0, NtL - 1, NtL)

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
            elif tL[i] >= tLim[j] and tL[i] < tLim[j + 1]:
                # Commented out the interpolation code as it's commented in the original MATLAB code
                # tFac = (tL[i] - tLim[j]) / (tLim[j+1] - tLim[j])
                pL[i], vxL[i], vyL[i] = pLim[j], vxLim[j], vyLim[j]
                break
            elif tL[i] >= tLim[Nlim - 1]:
                pL[i], vxL[i], vyL[i] = pLim[Nlim - 1], vxLim[Nlim - 1], vyLim[Nlim - 1]

    xL[0], yL[0] = x0, y0
    for i in range(1, NtL):
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


loc = r"C:\Users\Aashman Sharma\Documents\Paraview\Time_Series"
Nt = 356
x0 = 0
y0 = 0
t0 = 0
dt = 2e-5
s = 1000
h = 130

dat = ReadLaserTrajectory(loc, s, h)
print(dat)
"""
datTrajMod = GetLaserTrajectoryMod(dat, x0, y0, t0, dt, Nt)

plt.figure(figsize=(10, 6))



# Plot t vs x Mod
plt.plot(datTrajMod["t"], datTrajMod["x"], label="x(t)", color="blue")

# Plot t vs y Mod
plt.plot(datTrajMod["t"], datTrajMod["y"], label="y(t)", color="red")

# Add labels, title, and legend
plt.xlabel("Time (t)")
plt.ylabel("Position")
plt.title("Position vs Time")
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
"""
