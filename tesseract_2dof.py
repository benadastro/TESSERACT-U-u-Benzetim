import numpy as np
import matplotlib.pyplot as plt
##Lists
ZList = []
XList = []
##Initial positions
X = 0  # [m]
Y = 0  # [m]
startZ = 0
Z = startZ  # [m]
gX = 0  # gravity in x [m/s^2]
gZ = -9.801  # gravity in z [m/s^2]
vel = 100  # [m/s]
ang = 70 * (np.pi/180)  # [rad]
velX = vel * np.cos(ang)  # vel in x [m/s]
velZ = vel * np.sin(ang)  # vel in z [m/s]
time = 0.0  # [s]
dt = 0.01  # time step [s]
maxtime = 100
maxZ = 0  # initial pos in z (updated depending on time)
while time < maxtime and Z >= startZ:
    ##Velocity calculations
    velX = velX + gX * dt
    velZ = velZ + gZ * dt
    vel = np.sqrt(velX**2 + velZ**2)
    ##Position calculations
    X = X + velX * dt + 0.5 * gX * dt**2
    Z = Z + velZ * dt + 0.5 * gZ * dt**2
    ##Angle calculations
    ang = np.arctan(velZ/velX)
    ang = ang * (180/np.pi)
    ##Update max values
    if Z >= maxZ:
        maxZ = Z
        maxX = X
        timeApogee = time
        velApogee = vel
        apogeeZ = Z
    ZList.append(Z)
    XList.append(X)
    time += dt

print("Apooge position: " + str(np.round(apogeeZ, decimals=2)) + ' m')
print("Apogee velocity: " + str(np.round(velApogee, decimals=2)) + ' m/s')
print("Apogee time: " + str(np.round(timeApogee, decimals=2)) + ' s')
print("Last position: " + str(np.round([X,Y,abs(np.round(Z))], decimals=2)) + ' m')
print("Last velocity: " + str(np.round(vel, decimals=2)) + ' m/s')
print("Last angle: " + str(np.round(ang, decimals=2)) + ' degree')
print("Last time: " + str(np.round(time, decimals=2)) + ' s')

plt.plot(XList, ZList, 'k-', lw=2)
plt.xlabel("Range [m]")
plt.ylabel("Yükseklik [m]")
plt.title("Uçuş Profili")
plt.grid()
plt.show()
