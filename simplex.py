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
    
    def simplex(self):
    # Use simplex pivot rules until we either find the solution (-c_j >= 0)
    # or we find the problem is unbounded feasible (all a_ij<=0 for -c_j<0)
        while np.any(self.c < 0):
            # Case I: b >= 0
            if np.all(self.b >= 0):
                pivot_cols = np.where(self.c < 0)[0]
                
                # Create list of possible pivots and ratios b_i/a_ij
                poss_pivots = []
                poss_pivot_ratios = []
                for col in pivot_cols:
                    rows = np.where(self.a[:,col] > 0)[0]
                    for row in rows:
                        # Push tuple of row,col to pivots list
                        poss_pivots.append((row, col))
                        poss_pivot_ratios.append(self.b[row]/self.a[row,col])
                
                if len(poss_pivots) == 0:
                    raise Exception("Problem is unbounded feasible")
                min_ratio_index = np.argmin(poss_pivot_ratios)
                curr_pivot = poss_pivots[min_ratio_index]

                # Now pivot at the pivot we've chosen
                self.pivot(curr_pivot[0], curr_pivot[1])
            # Case II: some b_i < 0
            else:
                k = np.where(self.b < 0)[0][0] # b_k is first b_i<0
                neg_a_kj0 = np.where(self.a[k,:] < 0)[0]
                if len(neg_a_kj0) == 0:
                    raise Exception("Problem is infeasible")
                pivot_col = neg_a_kj0[0] # j_0 is the pivot column
                
                pivot_rows_1 = np.where(self.b >= 0)[0]
                pivot_rows_2 = np.where(self.a[:,pivot_col] > 0)[0]
                # We want rows where both conditions are true, so get their intersection
                pivot_rows = np.append(np.intersect1d(pivot_rows_1, pivot_rows_2), [k])

                pivot_row_ratios = np.divide(self.b[pivot_rows], self.a[pivot_rows,pivot_col].T)
                
                min_ratio_index = np.argmin(pivot_row_ratios)
                pivot_row = pivot_rows[min_ratio_index]

                # Now pivot at the pivot we've chosen
                self.pivot(pivot_row, pivot_col)
        
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
    
    def print_results(self):
        print("b", self.b)
        print("c", self.c)
        print(self.getX())
        print(self.getY())

def p22_ferguson_example():
    # problem from bottom of pg.22, Ferguson
    # Good example of pivoting in Case I
    b = np.array([6., 4., 7.])
    a = np.array([1., 3., -1., 0., 1., 1., 3., 1., 0.]).reshape(3,3)
    c = np.array([-5., -2., -1.])
    t = Tableau(3,3)
    t.b = b
    t.a = a
    t.c = c
    t.simplex()
    # t.pivot(2,0)
    # t.pivot(1,2)
    t.print_results()

def p26_ferguson_example():
    # problem from top of pg.26 Ferguson
    # Good example of pivoting in Case II
    b = np.array([3.,-2.,5.])
    a = np.matrix([[0.,1.,2.],[-1.,0.,-3.],[2.,1.,7.]])
    c = np.array([-1.,-1.,-5.])
    t = Tableau(3,3)
    t.b = b
    t.a = a
    t.c = c
    t.simplex()
    t.print_results()

def main():
    p22_ferguson_example()
    print()
    p26_ferguson_example()

if __name__ == '__main__':
    main() 