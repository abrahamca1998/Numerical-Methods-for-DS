import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_vec=[]
y_vec=[]
def normalize_point(point):
    normalized_point=[]
    normalized_point.append(0)
    normalized_point.append(0)
    if point[0]<0:
        normalized_point[0]=-np.mod(np.abs(point[0]),2*np.pi)
        if normalized_point[0]<(-np.pi):
            normalized_point[0]+=normalized_point[0]+2*np.pi
    if point[1]<0:
        normalized_point[1]=-np.mod(np.abs(point[0]),2*np.pi)
        if normalized_point[1]<(-np.pi):
            normalized_point[1]+=2*np.pi
    if point[0]>=0:
        normalized_point[0]=np.mod(np.abs(point[0]),2*np.pi)
        if normalized_point[0]>(np.pi):
            normalized_point[0]-=2*np.pi
    if point[1]>=0:
        normalized_point[1]=np.mod(np.abs(point[1]),2*np.pi)
        if normalized_point[1]>(np.pi):
            normalized_point[1]-=2*np.pi
        
    return normalized_point
def system(a,initialconditions,iterations):
    x_vec=[]
    y_vec=[]
    xo=initialconditions[0]
    yo=initialconditions[1]
    x_vec.append(xo)
    y_vec.append(yo)
    for i in range(iterations):

        x=xo+a*np.sin(xo+yo)
        y=xo+yo

        x,y=normalize_point([x,y])


        x_vec.append(x)
        y_vec.append(y)
        xo=x
        yo=y
    df=pd.DataFrame(columns=['x','y'])
    df['x']=x_vec
    df['y']=y_vec
    df.to_csv("test.csv")
    return x_vec,y_vec

xmin=-np.pi
xmax=np.pi
a=-0.7
iterations=500
NP=100
initialconditionsx=np.linspace(xmin,xmax,NP)
plt.figure()
for i in range(NP):
    initialconditions=[initialconditionsx[i],0]
    x_vec=[]
    y_vec=[]
    x_vec,y_vec=system(a,initialconditions,iterations)

    plt.scatter(x_vec,y_vec)
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-2*np.pi,2*np.pi)
plt.show()