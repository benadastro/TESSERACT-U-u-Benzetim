import numpy as np
import matplotlib.pyplot as plt
##LİSTELER
ZList = []
XList = []
##BAŞLANGIÇ KOŞULLARI
X = 0  # [m]
Y = 0  # [m]
baslangicZ = 0
Z = baslangicZ  # [m]
gX = 0  # x yönünde yer çekimi ivmesi [m/s^2]
gZ = -9.801  # z yönünde yer çekimi ivmesi [m/s^2]
hiz = 100  # [m/s]
aci = 70 * (np.pi/180)  # [radyan]
hizX = hiz * np.cos(aci)  # x yönündeki hız [m/s]
hizZ = hiz * np.sin(aci)  # z yönündeki hız [m/s]
zaman = 0.0  # [s]
dt = 0.01  # similasyon zaman adımı [s]
maxzaman = 100
maxZ = 0  # başlangıçta irtifa (zamana bağlı güncellenecektir)
while zaman < maxzaman and Z >= baslangicZ:
    ##HIZ
    hizX = hizX + gX * dt
    hizZ = hizZ + gZ * dt
    hiz = np.sqrt(hizX**2 + hizZ**2)
    ##KONUM
    X = X + hizX * dt + 0.5 * gX * dt**2
    Z = Z + hizZ * dt + 0.5 * gZ * dt**2
    ##AÇI
    aci = np.arctan(hizZ/hizX)
    aci = aci * (180/np.pi)
    ##MAX DEĞERLERİN GÜNCELLENMESİ
    if Z >= maxZ:
        maxZ = Z
        maxX = X
        zamanApogee = zaman
        hizApogee = hiz
        apogeeZ = Z
    ZList.append(Z)
    XList.append(X)
    zaman += dt

print("Tepe Noktası Yüksekliği: " + str(np.round(apogeeZ, decimals=2)) + ' m')
print("Tepe Noktası Hızı: " + str(np.round(hizApogee, decimals=2)) + ' m/s')
print("Tepe Noktası Zamanı: " + str(np.round(zamanApogee, decimals=2)) + ' s')
print("Son Pozisyon: " + str(np.round([X,Y,abs(np.round(Z))], decimals=2)) + ' m')
print("Son Uçuş Yolu Hızı: " + str(np.round(hiz, decimals=2)) + ' m/s')
print("Son Uçuş Yolu Açısı: " + str(np.round(aci, decimals=2)) + ' derece')
print("Son Uçuş Zamanı: " + str(np.round(zaman, decimals=2)) + ' s')

plt.plot(XList, ZList, 'k-', lw=2)
plt.xlabel("Menzil [m]")
plt.ylabel("Yükseklik [m]")
plt.title("Uçuş Profili")
plt.grid()
plt.show()
