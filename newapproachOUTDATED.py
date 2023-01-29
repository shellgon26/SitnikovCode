#required packages
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
#comment time BABY

def odes(x,tval):
    #reads in initial values for ode
    z=x[0]
    v=x[1]
    A=x[2]

    #calculates R via formula given in project outline
    r=0.5*(1-e*math.cos(A))
    
    #the ODEs given in the project outline
    dz=2*r*v
    dv=-(2*r*z/(z**2+r**2)**(3/2))
    dA=1

    #returns the result
    result =[dz,dv,dA]
    return result

#initial value for z
z0=0

#initial value for v
v0=0.5

#initial value for A
A0=0

#combines initial values into list to be given to odeint function
x0=[z0,v0,A0]

#creates a list of ts to evaluate the ODEs at
#Please ensure tmax is an integer
tmax=1000
pointsperhalfcycle=100
ts=np.linspace(0,2*tmax,2*tmax*pointsperhalfcycle+1)
print(ts)
#defines the eccentricity of plane orbits
e=0.2

#gets the numerical solutions to the ODEs given the inital values
#values at all the times within ts
x=odeint(odes,x0,ts*math.pi)



checkvals = []
for i in range(-1,2*pointsperhalfcycle*tmax,int(2*pointsperhalfcycle)):
    if i == -1:
        checkvals.append(0)
    else:
        checkvals.append(i)
#print(checkvals)

# #plots z and v on the same axis
print(ts[::2*pointsperhalfcycle])
plt.plot(ts,x[:,0])
plt.plot(ts,x[:,1])
plt.plot(ts[::2*pointsperhalfcycle],x[:,0][::2*pointsperhalfcycle],"bx")

#testing code
# plt.plot(ts,np.sin(ts))
# plt.plot(ts[checkvals],np.sin(ts)[checkvals],"bx")

#plot labels
plt.xlabel("time (s)")
plt.ylabel("z")

#display first plot
plt.show()

#plots phase space
#plt.plot(x[:,0],x[:,1],"b",linewidth=0.5)

#plots poincare section
plt.plot(x[:,0][::2*pointsperhalfcycle],x[:,1][::2*pointsperhalfcycle],"b.")

plt.xlabel("z")
plt.ylabel("v")

#display 2nd graph
plt.show()