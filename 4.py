import numpy as np

l_1 = 69.5
l_2 = 77.35

def inverse_kinematics(x, y, z):
    prev = np.arccos(
        (np.power(x, 2) + np.power(y, 2) + np.power(z, 2) - np.power(l_1, 2) - np.power(l_2, 2)) / (2 * l_1 * l_2))
    prev = prev * 180 / np.pi
    if prev >= -25 and prev <= 123:
        j_3 = np.arccos(
            (np.power(x, 2) + np.power(y, 2) + np.power(z, 2) - np.power(l_1, 2) - np.power(l_2, 2)) / (2 * l_1 * l_2))
        flag = -1
    j_3_2 = 0
    if - prev>=-25 and -prev<=123:
        j_3_2 = - np.arccos((np.power(x, 2) + np.power(y, 2) + np.power(z, 2) - np.power(l_1, 2) - np.power(l_2, 2)) / (2*l_1*l_2))
    j_2 = np.arcsin(y / (l_1 + l_2 * np.cos(j_3)))
    j_1 = np.arctan2(x, -z) + flag * np.arccos(
        (l_1 + l_2 * np.cos(j_3)) * np.cos(j_2) / (np.sqrt(np.power(x, 2) + np.power(z, 2))))
    if j_3_2 != 0:
        j_2_2 = np.arcsin(y / (l_1 + l_2 * np.cos(j_3)))
        j_1_2 = np.arctan2(x, -z) + np.arccos(
            (l_1 + l_2 * np.cos(j_3)) * np.cos(j_2) / (np.sqrt(np.power(x, 2) + np.power(z, 2))))
    j_1 = j_1 * 180 / np.pi
    j_2 = j_2 * 180 / np.pi
    j_3 = j_3 * 180 / np.pi
    if j_3_2 != 0:
        j_1_2 = j_1_2 * 180 / np.pi
        j_2_2 = j_2_2 * 180 / np.pi
        j_3_2 = j_3_2 * 180 / np.pi
        return (j_1, j_2, j_3), (j_1_2, j_2_2, j_3_2)
    else:
        return j_1, j_2, j_3





x = 69.5
y = 0
z = 77.35

print(inverse_kinematics(x, y, z))
