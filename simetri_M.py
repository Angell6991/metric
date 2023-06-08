from sympy import*
import os

os.system("clear")

n   =  int(input("Dimention: "))
A   =  []
B   =  []

for i in range(n):
    for j in range(n):
        if i <= j: 
            A.append(input(f"Introduc A{i+1}{j+1}: "))
        elif i > j: 
            A.append(0)

A   =   Array(A, (n,n))

for i in range(n):
    for j in range(n):
        if i > j:
            B.append(A[j,i])
        elif i <= j:
            B.append(0)

B   =   Array(B, (n,n))

C   =   A + B
print(C)

