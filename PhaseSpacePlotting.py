#required packages
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

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


def solveodes(z0,v0,tmax,pointsperhalfcycle,e):
    A0=0

    #combines initial values into list to be given to odeint function
    x0=[z0,v0,A0]

    #creates a list of ts to evaluate the ODEs at
    ts=np.linspace(0,2*tmax*math.pi,2*tmax*pointsperhalfcycle+1)

    #gets the numerical solutions to the ODEs given the inital values
    #values at all the times within ts
    x=odeint(odes,x0,ts,args=(e,))
    return x

def findcheckvals(pointsperhalfcycle,tmax):
    
    #initialises a list to store indexes of the points that are multiples of 2pi within
    checkvals = []
    #finds and stores all the 2pi indexes
    for i in range(-1,2*pointsperhalfcycle*tmax,int(2*pointsperhalfcycle)):
        if i == -1:
            checkvals.append(0)
        else:
            checkvals.append(i)
    return checkvals

def Pltzvtgraph(ts,zs,vs):
        # #plots z and v on the same axis
        plt.plot(ts,zs,label="z")
        plt.plot(ts,vs,label="v")

        #plot labels
        plt.xlabel("time (s)")
        #tells you which line is which
        plt.legend()
        #display first plot
        plt.show()

def pltphasespacegraph(zs,vs,e,z0,v0,tmax,Animated):
            
        #If the phase space is being animates, this code will run, which 
        #replots the data and just adding another point
        if Animated:
            fig,ax=plt.subplots()
            for i in range(0,2000):
                #if you want to see all the points be animates change the 
                #2000 to 'len(ts)-1' without the quotation marks
                ax.plot(zs[:i],vs[:i],"b",linewidth=0.5)
                plt.xlabel("z")
                plt.ylabel("v")
                plt.pause(0.001)
                ax.clear()
        #titles the plot with the relevant variables and their values
        plt.title(f"e={e},z0={z0},v0={v0}, between 0 and {2*tmax}\u03C0")
        #plots the "full" phase space - the phase space for all the times calculated
        plt.plot(zs,vs,"b",linewidth=0.5)

def PlotWhatYouNeed3D(z0:float,v0:float,e:float,tmax:int,pointsperhalfcycle:int,ax,ss:bool=True,Animated:bool=False,Plotzvtgraph:bool=False,Plotphasespacegraph:bool=False,Plotpoincaresection:bool=False):

    [zs,vs]=solveodes()

    checkvals=findcheckvals()

    if Plotzvtgraph:
        Pltzvtgraph()

    if Plotphasespacegraph:
        pltphasespacegraph()

 
    if Plotpoincaresection:
        PltPoincareSection(zs,vs,v0,checkvals,e,z0,v0,tmax)

    #adds labels and displays the plot if it doesn't already exist
    if ((Plotphasespacegraph& ~Animated) | Plotpoincaresection ):
        #adds labels to the plot
        plt.xlabel("z")
        plt.ylabel("v")

        #display 2nd graph
        
def PltPoincareSection(zs,vs,checkvals,e,z0,v0,tmax,ss,Plotphasespacegraph,ax=None,changevar=None):
    #plots poincare section
    if ss & ~Plotphasespacegraph:
        #plots an invisible version of the pase space plot to keep the scales the same
        plt.plot(zs,vs,z0,"w",linewidth=0.5)
    #titles the graph with the relevant variables and their values
    plt.title(f"Poincaré section with e={e},z0={z0},v0={v0}, between 0 and {2*tmax}\u03C0")
    #plots all the points that are at a multiple of 2pi (in t)
    if ax!=None:
        #print(ax)
        if changevar!=None:
            #print(changevar)
            ax.plot(zs[checkvals],vs[checkvals],changevar,"b.")
    else:
        plt.plot(zs[checkvals],vs[checkvals],"b.")

def DisplayPhaseSection(Plotphasespacegraph, Animated,Plotpoincaresection):
    #adds labels and displays the plot if it doesn't already exist
    if ((Plotphasespacegraph& ~Animated) | Plotpoincaresection ):
        #adds labels to the plot
        plt.xlabel("z")
        plt.ylabel("v")

        #display 2nd graph
        plt.show()

def PlotWhatYouNeed(z0:float,v0:float,e:float,tmax:int,pointsperhalfcycle:int,ss:bool=True,Animated:bool=False,Plotzvtgraph:bool=False,Plotphasespacegraph:bool=False,Plotpoincaresection:bool=False):

    [zs,vs]=solveodes()
    checkvals=findcheckvals()

    if Plotzvtgraph:
        Pltzvtgraph()

    if Plotphasespacegraph:
        pltphasespacegraph()

    if Plotpoincaresection:
        PltPoincareSection()

    DisplayPhaseSection()

def PltPoincareSection3D(z0,tmax,pointsperhalfcycle,e):

    fig=plt.figure()
    ax=plt.axes(projection='3d')
    #changevar=v
    vmin=0.6199
    vmax=0.6203
    for v in np.arange(vmin,vmax,1e-5):
        [zs,vs,ts]=np.transpose(solveodes(z0,v,tmax,pointsperhalfcycle,e))
        checkvals=findcheckvals(pointsperhalfcycle,tmax)
        PltPoincareSection(zs,vs,checkvals,e,z0,v,tmax,False,False,ax,v)
    plt.xlim(-vmax,vmax)
    plt.show()

z0=0
tmax=1000
pointsperhalfcycle=100
e=0.2

PltPoincareSection3D(z0,tmax,pointsperhalfcycle,e)