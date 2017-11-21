# -*- coding: utf-8 -*-
"""
Simplex Algorithm

"""

import numpy as np

class Tableau:    
    def __init__(self, mrows, ncols):
        self.m = mrows
        self.n = ncols
        self.b = np.zeros((1, mrows))
        # 1x a placeholder for left col, y's
        self.t = np.arange(10, 10+mrows, 1)
        # 2x a placceholder for top row, x's
        self.r = np.arange(20, 20+ncols, 1)
        self.c = np.zeros((1, ncols))
        self.a = np.zeros((mrows, ncols))
        self.objVal = 0
    
    def pivot(self, i, j):
        if self.a[i,j] == 0:
            print("Pivot error: a[i,j] must not be 0")
            return
        tmp = self.r[j]
        self.r[j] = self.t[i]
        self.t[i] = tmp
        #calculate new coefficients for matrix
        ahat = np.copy(self.a)
        for n in range(0,self.m):
            for k in range(0,self.n):
                if n==i and k==j:
                    ahat[n,k] = 1/self.a[i,j]
                elif n==i:
                    ahat[n,k] /= self.a[i,j]
                    
                elif k==j:
                    ahat[n,k] /= -self.a[i,j]
                else:
                    ahat[n,k] -= self.a[i,k]*self.a[n,j]/self.a[i,j]
        # calculate new b values
        bhat = np.copy(self.b)
        for n in range(0, self.m):
            if n==i:
                bhat[n] /= self.a[i,j]   
            else:
                bhat[n] -= self.b[i]*self.a[n,j]/self.a[i,j]
        # calculate new cost values
        chat = np.copy(self.c)
        for k in range(0, self.n):
            if k==j:
                chat[k] /= -self.a[i,j]
            else:
                chat[k] -= self.a[i,k]*self.c[j]/self.a[i,j]
        # set new tableau
        self.objVal -= self.b[i]*self.c[j]/self.a[i,j]
        self.a = ahat
        self.b = bhat
        self.c = chat
        
    # solution to maximum problem
    def getX(self):
        x = np.zeros((1, self.n))
        for k in range(0,self.n):
            if self.r[k] == 0:
                x[k] = 0
            else:
                for n in range(0, self.m):
                    if self.t[n] == 20+k:
                        x[0][k] = self.b[n]
        return(x)
    
    # solution to minimum problem
    def getY(self):
        y = np.zeros((1,self.m))
        for n in range(0, self.m):
            if self.t[n] == 0:
                y[n] = 0
            else:
                for k in range(0, self.n):
                    if self.r[k] == 10+n:
                       y[0][n] = self.c[k]
        return(y)

# problem from bottom of pg.22, Ferguson
b = np.array([6., 4., 7.])
a = np.array([1., 3., -1., 0., 1., 1., 3., 1., 0.]).reshape(3,3)
c = np.array([-5., -2., -1.])
t = Tableau(3,3)
t.b = b
t.a = a
t.c = c
t.pivot(2,0)
t.pivot(1,2)
print("b", t.b)
print("c", t.c)
print(t.getX())
print(t.getY())