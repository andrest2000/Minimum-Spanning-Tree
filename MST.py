import math
import numpy as np
import matplotlib.pyplot as plt
import random as r
def MST(points):
    n=points[0].size
    nt=((n*n)+n)/2
    diff=np.zeros((n,n))
    diffe=np.zeros((n,n))
    mm=np.zeros(nt)
    naux=0
    for i in range (n):
        for j in range (n):
            dx=points[0,i]-points[0,j]
            dy=points[1,i]-points[1,j]
            dist=pow(pow(dx,2)+pow(dy,2),0.5)
            diff[i][j]=dist
    mxp=diff.max()
    for i in range (n):
        diff[i][i]=mxp+1 
    for i in range (n):
        for j in range (n):
            if i>j:
                diffe[i][j]=diff[i][j]+mxp
            else:
                diffe[i][j]=diff[i][j]
    mnp=diffe.min()
    mnpin=diffe.argmin()
    if mnpin>=n:
         jin=mnpin%n
         iin=((mnpin-jin)/n)
    else:
         jin=mnpin
         iin=0
    sizef=(np.ones((n,n)))*mxp
    vertf=np.zeros(n)
    vertf[0]=iin
    vertf[1]=jin
    vertff=np.zeros((2,n-1))
    vertff[0][0]=iin
    vertff[1][0]=jin
    kkk=0
    while kkk!=n-2:
     kkk=kkk+1
     for i in range(kkk+1):
        for j in range(n):
            sizef[vertf[i]][j]=diff[j][vertf[i]]
     for i in range (kkk+1):
        for j in range (kkk+1):
                sizef[vertf[i]][vertf[j]]=sizef[vertf[i]][vertf[j]]+mxp
     mnp=sizef.min()
     mnpin=sizef.argmin()
     if mnpin>=n:
         jin=mnpin%n
         iin=((mnpin-jin)/n)
     else:
         jin=mnpin
         iin=0
     vertff[0][kkk]=iin
     vertff[1][kkk]=jin
     vertf[kkk+1]=jin
    "return vertf, vertff"
    print(vertff)
def main():
    n=input("Indicar el numero de nodos: ")
    points=np.zeros((2,n))
    for i in range (n):
        px=input("Posicion x del nodo "+str(i)+": ")
        py=input("Posicion y del nodo "+str(i)+": ")
        points[0][i]=px
        points[1][i]=py
    print("La lista 2x"+str(n)+" resultante nos indica la conexion de los nodos de la fila 1 con los nodos de la fila 2, siguiendo la numeracion antes descrita")
    MST(points)
main()



    


           
