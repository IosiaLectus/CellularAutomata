# -*- coding: utf-8 -*-
"""
Created on Fri Nov 07 14:23:29 2014

@author: Josiah
"""

import random

class Automata1D:
    
    dim = 1
    n = 1
    numNeighbors = 3
    
    past = [];
    present = [];
    future = [];
    
    ruleNum = 0
    
    def __init__(self,n,d):
        self.dim = d
        self.numNeighbors = 3**d
        self.past = [0 for i in range(0,n**self.dim)]
        self.present = list(self.past)
        self.future = list(self.present)
        self.n = n
        self.ruleArray = self.parseRule(self.ruleNum)
        
    def setRule(self,r):
        self.ruleNum = r%(2**(2**self.numNeighbors))
        self.ruleArray = self.parseRule(self.ruleNum)
    
    def Neighbors(self,m):
        ret = []
        mm = m
        coords = [0 for i in range(0,self.dim)]
        for i in range(0,self.dim):
            coords[i] = mm%self.n
            mm = mm-mm%self.n
            mm = mm/self.n
        for i in range(0,self.numNeighbors):
            nary = self.Base3(i)
            coordsN = coords[:]
            mmm = 0
            for j in range(0,len(nary)):
                coordsN[j] += nary[j]
            for j in range(0,len(coordsN)):
                coordsN[j] += (self.n -1)
                coordsN[j] = coordsN[j]%self.n
                mmm += (2**j)*coordsN[j]
            ret.append(mmm)
        #return [(m-1)%self.n,m%self.n,(m+1)%self.n]
        return ret
        
    def rule(self,n):
        nbrs = self.Neighbors(n)
        state = 0
        for i in range(0,len(nbrs)):
            state += (2**i)*self.present[nbrs[i]]
        return self.ruleArray[state]
        
    def Base3(self,x):
        y = x
        ret = []
        while(y>0):
            ret.append(y%3)
            y = y - y%3
            y = y/3
        return ret
        
    def parseRule(self, x):
        y = x
        ret = [0 for i in range(0,2**self.numNeighbors)]
        i = 0
        while(y>0):
            ret[i] = y%2
            i = i + 1
            y = y - y%2
            y = y/2
        return ret
    
    def step(self):
        for i in range(0,self.n):
            self.future[i] = self.rule(i)
        self.past = list(self.present)
        self.present = list(self.future)
        
    def populate(self,n):
        self.present[n] = 1
        
    def populateRandom(self,x):
        for i in range(0,x):
            self.populate(random.randint(0,self.n-1))
            
    def play(self,t):
        for i in range(0,t):
            self.step()
            print(self.present)
            print

def Main():
    a = Automata(5,2)
    a.setRule(110)
    a.populate(0)
    print
    print a.ruleNum
    print
    print a.ruleArray
    print
    print
    print a.present
    print
    a.play(1)
    print "\nThe main function executed\n"
    
if __name__ == "__main__":
    Main()
