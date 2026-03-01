# Ödev 201 - Celaleddin Karakılıç

import numpy as np

# Kol uzunluklarının tanımlanması
l1 = 1.0
l2 = 0.5
l3 = 0.25

# Kol açılarının Tanımlanması
theta1 = 30
theta2 = 45
theta3 = 60

# dereceleri radyana çevirmek
theta1 = theta1*np.pi/180
theta2 = theta2*np.pi/180
theta3 = theta3*np.pi/180

# A1 A2 A3 matris çarpımı sonucu elde edilen tablo
p1 = l1 * np.cos(theta1) + l2 * np.cos(theta1  + theta2) + l3 * np.cos(theta1+theta2+theta3)
p2 = l1 * np.sin(theta1) + l2 * np.sin(theta1  + theta2) + l3 * np.sin(theta1+theta2+theta3)

print("Son efektör p1:", p1)
print("Son efektör p2:", p2)
