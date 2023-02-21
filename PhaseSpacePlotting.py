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
        #plot the z and v vs time graph
        Pltzvtgraph()

    if Plotphasespacegraph:
        #plot the phase space graph
        pltphasespacegraph()

 
    if Plotpoincaresection:
        #plot the Poincaré section
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
    if ax!=None & changevar!=None:
        #plots the 3D poincare section - I wouldn't do it if i were you it's laggy and really hard to read
        #also you'd have to change the axis cause i don't have the code written and commented out , if you still
        #really want to do it, message me in the group chat and i'll make a version where you can
        #but please, don't do it
        ax.plot(zs[checkvals],vs[checkvals],changevar,"b.")
    else:
        #if the function isn't called in a very specific way, this line will run and just plot it normally
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
    #this is the version of the function you should be using 99% of the time
    #solves the odes
    [zs,vs,ts]=np.transpose(solveodes(z0,v0,tmax,pointsperhalfcycle,e))
    #finds the values to plot for the poincaré section
    checkvals=findcheckvals(pointsperhalfcycle,tmax)

    if Plotzvtgraph:
        #plots the z and v vs t graph
        Pltzvtgraph(ts,zs,vs)

    if Plotphasespacegraph:
        #plots the phase space
        pltphasespacegraph(zs,vs,e,z0,v0,tmax,Animated)

    if Plotpoincaresection:
        #plots the poincaré section
        PltPoincareSection(zs,vs,checkvals,e,z0,v0,tmax,ss,Plotphasespacegraph)

    #displays the axis if needed
    DisplayPhaseSection(Plotphasespacegraph,Animated,Plotpoincaresection)

def PltPoincareSection3D(z0,tmax,pointsperhalfcycle,e):
    #this is a funcrtion that shoudl never really be called, please don't look here, it's messy because
    #i have no reason to actually make it look good or work better
    fig=plt.figure()
    ax=plt.axes(projection='3d')
    vmin=0.6199
    vmax=0.6203
    for v in np.arange(vmin,vmax,1e-5):
        [zs,vs,ts]=np.transpose(solveodes(z0,v,tmax,pointsperhalfcycle,e))
        checkvals=findcheckvals(pointsperhalfcycle,tmax)
        PltPoincareSection(zs,vs,checkvals,e,z0,v,tmax,False,False,ax,v)
    plt.xlim(-vmax,vmax)
    plt.show()

def PltBifurcationDiagram(varmin,varmax,tmax,pointsperhalfcycle,e,z0=0,v0=0):
    #gets a set of values for the varaible to change
    xvals=np.arange(varmin,varmax,2e-2)
    #plots the z values for each value of the variable to change by
    for v in xvals:
        #solving the odes
        [zs,vs,ts]=np.transpose(solveodes(z0,v,tmax,pointsperhalfcycle,e))
        #finding the values of the phase space to plot
        checkvals=findcheckvals(pointsperhalfcycle,tmax)
        #duplicates the current value of the chainging variable to match the size of the z values
        xvar=np.array([v for i in zs[checkvals]])
        #plots the set of data for that value of the chaning variable
        plt.plot(xvar,zs[checkvals],"b.")
    #scales and labels the axis
    plt.ylim(-varmax,varmax)
    plt.xlabel("v0")
    plt.ylabel("z")
    #shows the plot
    plt.show()

tmax=1000
pointsperhalfcycle=100
e=0.2
varmin=0
varmax=4

#PltBifurcationDiagram(varmin,varmax,tmax,pointsperhalfcycle,e)

for v in np.arange(1.244,1.251,0.001):
    PlotWhatYouNeed(0.5,v,e,tmax,pointsperhalfcycle,Plotphasespacegraph=True)
