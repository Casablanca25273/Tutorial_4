# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:53:01 2018

@author: Tankiso
"""

import numpy
from matplotlib import pyplot as plt

class advection:
    def __init__(self,npart=100,u=-1.0,dx=1.0):
        x=numpy.zeros(npart)
        x[npart/3:2*npart/3]=1.1;
        self.x=x
        self.u=u
        self.dx=dx
        
    def get_bc_periodic(self):
        self.x[0]=self.x[-2]
        self.x[-1]=self.x[1]
        
    def update(self,dt=1.0):
        self.get_bc_periodic()
        delt=self.x[1:]-self.x[0:-1]
        self.x[1:-1]+=self.u*dt/self.dx*delt[1:]

if __name__=='__main__':
    material=advection()
    plt.ion()
    plt.plot(material.x)
    plt.show()
    for i in range(0,100):
        material.update()
        plt.clf()
        plt.plot(material.x)
        plt.draw()