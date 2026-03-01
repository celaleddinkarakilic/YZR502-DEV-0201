# Ödev 201 - Celaleddin Karakılıç

import numpy as np
import random

# Kol uzunluklarının tanımlanması
l1 = 1.0
l2 = 0.5
l3 = 0.25

p1 = 0
p2 = 0
#Hedef son efektör konumları:
hedef_p1 = 0.81
hedef_p2 = 1.15
tolerans = 0.01

theta1 = 0
theta2 = 0
theta3 = 0

while(abs(p1 - hedef_p1) > tolerans or abs(p2 - hedef_p2) > tolerans):
    theta1 = random.uniform(-np.pi, np.pi)
    theta2 = random.uniform(-np.pi, np.pi)
    theta3 = random.uniform(-np.pi, np.pi)
    p1 = l1 * np.cos(theta1) + l2 * np.cos(theta1  + theta2) + l3 * np.cos(theta1+theta2+theta3)
    p2 = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2) + l3 * np.sin(theta1 + theta2 + theta3)


# Açıları radyandan dereceye çevirmek
theta1 = theta1*180/np.pi
theta2 = theta2*180/np.pi
theta3 = theta3*180/np.pi

print("Son efektör p1:", p1)
print("Son efektör p2:", p2)
print("Theta 1:", theta1)
print("Theta 2:", theta2)
print("Theta 3:", theta3)

