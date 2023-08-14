import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd


def ReadLaserTrajectory(loc, s, h):
    P0 = 400
    locF = loc + "\\"
    fnameP = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-power.csv"
    fnamex = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-x.csv"
    fnamey = locF + str(P0) + "_" + str(s) + "_" + str(h) + "-y.csv"

    Fp = pd.read_csv(fnameP, header=None).values
    Fx = pd.read_csv(fnamex, header=None).values
    Fy = pd.read_csv(fnamey, header=None).values

    dat = np.column_stack((Fx, Fy[:, 1], Fp[:, 1]))

    return dat


def GetLaserTrajectory(dat, x0, y0, t0, dt, Nt):
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
    for i0 in range(Nt - 1):
        i = i0 + 1
        for j in range(Nlim - 1):
            if t[i] >= tLim[j] and t[i] < tLim[j + 1]:
                tFac = (t[i] - tLim[j]) / (tLim[j + 1] - tLim[j])
                p[i] = pLim[j] + tFac * (pLim[j + 1] - pLim[j])
                vx[i] = vxLim[j] + tFac * (vxLim[j + 1] - vxLim[j])
                vy[i] = vyLim[j] + tFac * (vyLim[j + 1] - vyLim[j])
                break

    x[0] = x0
    y[0] = y0
    for i in range(1, Nt):
        # x[i] = x[i-1] + 0.5*dt*(vx[i-1] + vx[i])
        # y[i] = y[i-1] + 0.5*dt*(vy[i-1] + vy[i])
        x[i] = x[i - 1] + dt * vx[i - 1]
        y[i] = y[i - 1] + dt * vy[i - 1]

    pOn = p != 0

    datTraj = {"t": t, "x": x, "y": y, "vx": vx, "vy": vy, "p": p, "pOn": pOn}

    print(p)

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
datTraj = GetLaserTrajectory(dat, x0, y0, t0, dt, Nt)

# plt.figure(figsize=(10, 6))

# Plot t vs x
# plt.plot(datTraj["t"], datTraj["x"], label="x(t)", color="blue")

# Plot t vs y
# plt.plot(datTraj["t"], datTraj["y"], label="y(t)", color="red")

# Add labels, title, and legend
# plt.xlabel("Time (t)")
# plt.ylabel("Position")
# plt.title("Position vs Time")
# plt.legend()

# Display the plot
# plt.grid(True)
# plt.tight_layout()
# plt.show()
