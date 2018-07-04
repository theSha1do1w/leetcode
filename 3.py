import numpy as np
import matplotlib.pyplot as plt
l_1 = 69.5
l_2 = 77.35

def forword_kinematics(j_1, j_2, j_3):
    j_1 = j_1 * np.pi / 180.0
    j_2 = j_2 * np.pi / 180.0
    j_3 = j_3 * np.pi / 180.0
    martex_t1 = np.mat([
        [np.cos(-j_1), 0, np.sin(-j_1), 0],
        [0, 1, 0, 0],
        [-np.sin(-j_1), 0, np.cos(-j_1), 0],
        [0, 0, 0, 1]])

    martex_t2 = np.mat([
        [1, 0, 0, 0],
        [0, np.cos(j_2), -np.sin(-j_2), 0],
        [0, np.sin(j_2), np.cos(j_2), 0],
        [0, 0, 0, 1]])

    martex_t3 = np.mat([
        [np.cos(-j_3), 0, np.sin(-j_3), 0],
        [0, 1, 0, 0],
        [-np.sin(-j_3), 0, np.cos(-j_3), -l_1],
        [0, 0, 0, 1]])

    martex_t4 = np.mat([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -l_2],
        [0, 0, 0, 1]])
    res = martex_t1* martex_t2* martex_t3* martex_t4* np.mat([[0],[0],[0],[1]])
    return res


'''fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlabel('X')
plt.ylabel('Z')
for i in range(-130,116):
    for j in range(-25,123):
            x = forword_kinematics(i, 0, j)
            ax.scatter(x[0,0],x[2,0],color='b',s=1)
plt.show()'''

print(forword_kinematics(-111,0, 20))