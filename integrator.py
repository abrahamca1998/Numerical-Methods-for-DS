import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def dP_dt(P, t):
    return [P[1], -P[0],P[3],P[5],-P[2],-P[4]]

ts = np.linspace(0, 12, 1000)
tsbw=ts[::-1]


x_values=np.linspace(0,4,100)
y_values=np.linspace(0,4,100)
a_values=np.linspace(0,4,100)
b_values=np.linspace(0,4,100)
c_values=np.linspace(0,4,100)
d_values=np.linspace(0,4,100)
for i in range(len(x_values)):
    Ps=odeint(dP_dt,(x_values[i],y_values[i],a_values[i],b_values[i],c_values[i],d_values[i]),ts)
    plt.scatter(Ps[:,0],Ps[:,1])
plt.show()