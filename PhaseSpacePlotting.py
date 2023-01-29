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
v0=1.91705

#initial value for A
A0=0

#combines initial values into list to be given to odeint function
x0=[z0,v0,A0]

#creates a list of ts to evaluate the ODEs at
ts=np.linspace(0,3*math.pi,900)

#defines the eccentricity of plane orbits
e=0.2

#gets the numerical solutions to the ODEs given the inital values
#values at all the times within ts
x=odeint(odes,x0,ts)

#plots z and v on the same axis
plt.plot(ts,x[:,0])
plt.plot(ts,x[:,1])

#plot labels
plt.xlabel("time (s)")
plt.ylabel("z")

#display first plot
plt.show()

poincarepoints=ts%math.pi<=0.005

#plots phase space
plt.plot(x[:,0],x[:,1],"b",linewidth=0.5)

#plots poincare section
#plt.plot(x[:,0][poincarepoints],x[:,1][poincarepoints],"b.")

plt.xlabel("z")
plt.ylabel("v")

#display 2nd graph
plt.show()