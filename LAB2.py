#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:31:55 2020

@author: ministore
"""

import networkx as nx
import numpy as np
import numpy.linalg as lina
import math as mt
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_edges_from([(0,1),(2,3),(3,1),(3,0),(2,4)])

nx.draw(G,with_labels=True)
plt.show()

A=[]

#ex 1
for n in G:
    B=[]
    for n1 in G:
           B.append(int((n1,n) in G.edges))
    A.append(B)  
print("Adj G:",A)

#1.a
def matrix(A):
    return isinstance(A, list) and len(A)>0  and all(isinstance(a, list) for a in A)

def sameDimMatrices(A,B):
    if matrix(A) and matrix(B):
        if len(B)==len(A):
            if all(len(A[i])==len(B[i]) for i in range(len(A))):
                return True
    return False

A=[[1],[2]]
print()
def sumM(A,B):
    if sameDimMatrices(A,B):
        return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return []
print("Sum A+A:",sumM(A,A))

#1.b
def rowsM(A):
    if matrix(A):
        return len(A)
    return 0
def colsM(A):
    if matrix(A):
        return len(A[0])
    return 0

A=[[1,2],[3,4]]
V=[2,3]

def prodMV(A,V):
    if matrix(A) and isinstance(V, list):
        if colsM(A)==len(V):
            return [sum(A[i][j]*V[j] for j in range(len(V))) for i in range(len(A))]
    return []
print("ProdMV:",prodMV(A,V))

#1.c
def prodM(A,B):
    if matrix(A) and matrix(B) and colsM(A)==rowsM(B):
        C=[[] for i in range(rowsM(A))]
        for j in range(colsM(B)):
            V=prodMV(A,[B[i][j] for i in range(rowsM(B))])
            for i in range(len(V)):
                C[i].append(V[i])
        return C
    return []
print("Prod AxA:",prodM(A,A))

#1.d
def squareM(A):
    return matrix(A) and rowsM(A)==colsM(A)

def minor(A,i,j):
    if squareM(A) and -1<i<rowsM(A) and -1<j<colsM(A):
        return [[A[n][m] for m in range(colsM(A)) if m!=j] for n in range(rowsM(A)) if n!=i]
    return [-1]

print("Minor:",minor(A,0,0))
def det(A):
   if squareM(A):
       if colsM(A)==rowsM(A)==1:
           return A[0][0]
       return sum(mt.pow(-1,i)*A[i][0]*det(minor(A,i,0)) for i in range(rowsM(A)))
   return -1

print("det:",det(A))

#ex2

A=np.matrix("2 3; 4 6")
def ex2(G):
    A=nx.to_numpy_matrix(G)
    #A=np.matrix("1 2 3 4; 5 6 7 8 ; 9 10 11 12 ; 13 14 15 16")
    print("Adj G:",A)
    print("Element a_1,2: ",A[0,1])
    print("First Column: ",A[:,0].T)
    print("Vector [a_1,2, a_2,3, a_3,4]: ", A[[0,1,2],[1,2,3]])

ex2(G)  

#ex3

#3.a
A=nx.to_numpy_matrix(G)
def degree(A):
     i=1
     for a in A:
         print("Degree node ",i, ":", sum(b for b in np.nditer(a)))
         i+=1
degree(A)

#3.b
def path2(A,i,j):
    print("Path of length 2 (",i,",",j,") :",(A*A)[i,j]>0)

path2(A,0,4)

#3.c
def triangles(A):
    B=A*A*A
    print("Number of triangles: ", sum(B[i,i] for i in range(len(B)))/6)
triangles(A)

#3.d

def connected(A):
    return not 0 in lina.matrix_power(np.identity(len(A))+A,len(A)-1)
print("Connected:", connected(A))

#3.e

#note that if you count the walks of lengt 4 you need to remove all of
# the walks of the type:
# u->x->u->x>u for some x
# u->x->y->x->u for some x=\=y
# u->x->u->y->u for some x=\=y
# there are:
# k walks of type 1
# k(k-1) walks of type 2 and 3
# so we count all the 4 walks and remove nk(2k-1) wolks
G1=nx.random_regular_graph(3,6)
#G1.add_edges_from([(1,2),(2,3),(3,4),(4,1)])
nx.draw(G1,with_labels=True)
plt.show()

def fourwalks(A,k):
    B=lina.matrix_power(A,4)
    return (sum(B[i,i] for i in range(len(B)))-(len(B)*k*(2*k-1)))/8

print(fourwalks(nx.to_numpy_array(G1),3))

#3.g
F=nx.fiedler_vector(G1)
P=[]
P1=[]
i=0
for n in G1:
    if F[i]>0:
        P.append(n)
    else:
        P1.append(n)
    i+=1
print(P)
print(P1)
#print(lina.eigvals(A),"\n")
#print(np.linalg.eig(A),"....")
