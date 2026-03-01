# Ödev 201 - Celaleddin Karakılıç

import numpy as np
import matplotlib.pyplot as plt

# Kol uzunluklarının tanımlanması
l1 = 1.0
l2 = 0.5
l3 = 0.25

hassasiyet = 15
thetalar = np.radians(np.arange(-180, 180 + hassasiyet, hassasiyet))

xler = []
yler = []

for theta1 in thetalar:
    for theta2 in thetalar:
        for theta3 in thetalar:
            p1 = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2) + l3 * np.cos(theta1 + theta2 + theta3)
            p2 = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2) + l3 * np.sin(theta1 + theta2 + theta3)

            xler.append(p1)
            yler.append(p2)

plt.figure(figsize=(10, 10))
plt.scatter(xler, yler, s=1, color='blue')
plt.title("Çalışma Alanı")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True, linestyle='-')
plt.axis('equal')
plt.legend()
plt.show()