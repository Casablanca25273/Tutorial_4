# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:22:57 2018

@author: tankiso
"""

import numpy
from matplotlib import pyplot as plt

class Particles:
    def __init__(self,npart=300,xmax=1.0,u=1.0):
        self.x=numpy.arange(npart)/(0.0+npart)*xmax
        self.u=u*(xmax-self.x)/xmax
        
    def update(self,dt=0.01):
        self.x+=self.u*dt
        
    def get_density(self,dx=0.01):
        xmin=numpy.min(self.x)
        xmax=numpy.max(self.x)
        nbin=numpy.round(1+(xmax-xmin)/dx)
        myind=numpy.round( (self.x-xmin)/dx)
        rho=numpy.zeros(nbin)

        assert(myind.max()<nbin) 
        for i in numpy.arange(0,myind.size):
            rho[myind[i]]+=1.0
        xvec=numpy.arange(0,nbin)*dx+xmin
        return rho,xvec
        
if __name__=='__main__':
    part=Particles(npart=30000)
    plt.ion()
    plt.plot(part.x)
    plt.show()
    plt.clf()
    
    for ii in range(0,200):
        part.update(dt=0.01)
        rho,x=part.get_density()
        plt.plot(x,rho)
        plt.draw()