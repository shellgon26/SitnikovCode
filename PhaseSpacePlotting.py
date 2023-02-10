#required packages
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math
#comment time BABY

#initial value for z
z0=0

#initial value for v
v0=0.6200941
#defines the eccentricity of plane orbits
e=0.2

#if you want to see how z and v vary with time, set this to true
#If you want this graph, I reccomend setting tmax to a single digit number, else
#the x axis becomes unreadable due to the results being squished together
Plotzvtgraph=False

#if you want to see the phase space line, set this to true
Plotphasespacegraph=False
#if you want to see the Poincaré section points, set this to true
Plotpoincaresection=True

#Please ensure tmax is an integer
#tmx is the maximum time to calculate values for (divided by 2pi)
tmax=1000

#defines how many points to plot per pi
pointsperhalfcycle=100


#Set to True if you would like the phase space and the Poincaré section to have the same scale
ss=True

#Animates the phase space diagram
#NOTE: Do not try to close the graph while it is still animating, it will spawn a blank graph in its place, in this case you'll have to close your python to fix it
Animated = False


def odes(x,tval,e):
    #reads in initial values for ode
    z=x[0]
    v=x[1]
    A=x[2]

    #calculates r via formula given in project outline
    r=0.5*(1-e*math.cos(A))
    
    #the ODEs given in the project outline
    dz=2*r*v
    dv=-(2*r*z/(z**2+r**2)**(3/2))
    dA=1

    #returns the result
    result =[dz,dv,dA]
    return result

#initial value for A (It changing doesn't matter so i'm not allowing it to be changed)
A0=0
#combines initial values into list to be given to odeint function
x0=[z0,v0,A0]

#creates a list of ts to evaluate the ODEs at
ts=np.linspace(0,2*tmax*math.pi,2*tmax*pointsperhalfcycle+1)

#gets the numerical solutions to the ODEs given the inital values
#values at all the times within ts
x=odeint(odes,x0,ts,args=(e,))

#initialises a list to store indexes of the points that are multiples of 2pi within
checkvals = []
#finds and stores all the 2pi indexes
for i in range(-1,2*pointsperhalfcycle*tmax,int(2*pointsperhalfcycle)):
    if i == -1:
        #checkvals.append(0)
        H=1
    else:
        checkvals.append(i)

if Plotzvtgraph:
    # #plots z and v on the same axis
    plt.plot(ts,x[:,0],label="z")
    plt.plot(ts,x[:,1],label="v")

    #plot labels
    plt.xlabel("time (s)")
    #tells you which line is which
    plt.legend()
    #display first plot
    plt.show()

if Plotphasespacegraph:
    
    #If the phase space is being animates, this code will run, which 
    #replots the data and just adding another point
    if Animated:
        fix,ax=plt.subplots()
        for i in range(0,2000):
            #if you want to see all the points be animates change the 
            #2000 to 'len(ts)-1' without the quotation marks
            ax.plot(x[:,0][:i],x[:,1][:i],"b",linewidth=0.5)
            plt.xlabel("z")
            plt.ylabel("v")
            plt.pause(0.001)
            ax.clear()
    #titles the plot with the relevant variables and their values
    plt.title(f"e={e},z0={z0},v0={v0}, between 0 and {2*tmax}\u03C0")
    #plots the "full" phase space - the phase space for all the times calculated
    plt.plot(x[:,0],x[:,1],"b",linewidth=0.5)

if Plotpoincaresection:
    #plots poincare section
    if ss & ~Plotphasespacegraph:
        #plots an invisible version of the pase space plot to keep the scales the same
        plt.plot(x[:,0],x[:,1],"w",linewidth=0.5)
    #titles the graph with the relevant variables and their values
    plt.title(f"Poincaré section with e={e},z0={z0},v0={v0}, between 0 and {2*tmax}\u03C0")
    #plots all the points that are at a multiple of 2pi (in t)
    plt.plot(x[:,0][checkvals],x[:,1][checkvals],"b.")

#adds labels and displays the plot if it doesn't already exist
if ((Plotphasespacegraph& ~Animated) | Plotpoincaresection ):
    #adds labels to the plot
    plt.xlabel("z")
    plt.ylabel("v")

    #display 2nd graph
    plt.show()

