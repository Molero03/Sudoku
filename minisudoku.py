import numpy as np
from numba import njit
import matplotlib.pyplot as plt


@njit
def energy(M):
    E=0
    for i in range(0,q):
        for j in range(0,q):
            for k in range(0,q):
                if M[i,j]==M[i,k] and j!=k:
                    E=E+1
                if M[i,j]==M[k,j] and i!=k:
                    E=E+1
            if i < 2 and j < 3:
                for x in range(2):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i < 2 and j>2 and j < 6:
                for x in range(2):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i >1 and i < 4 and j < 3:
                for x in range(2,4):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>1 and i < 4 and j>2 and j < 6:
                for x in range(2, 4):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>3 and i < 6 and j < 3:
                for x in range(4, 6):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>3 and i < 6 and j>2 and j < 6:
                for x in range(4, 6):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
                    

    return E


#H= -sum_{ij} delta_{ij} 
q=6
n=500000
numbers=np.array([])
conver=5000
beta=3.


m=False
while m==False:

    M= np.matrix([[0,0,0,0,0,0],
             [2,3,0,0,1,4],
             [4,5,0,0,2,3],
             [0,0,0,0,0,0],
             [1,0,0,0,0,6],
             [0,2,3,4,5,0]])


    for i in range(q):
        for j in range(q):
            if M[i,j]!=0:
                numbers=np.append(numbers, '('+str(i) + ',' +str(j) +')')
                continue
            M[i,j]= np.random.randint(1,q+1)


    E0=energy(M)  
    E=np.zeros(n, dtype=np.int16)
    l=0    
    Es=0
    for i in range(n):

            
        x=np.random.randint(q)
        y=np.random.randint(q)
        number= '('+str(x) + ',' +str(y) +')'
        if number in numbers:
            E[i]=int(E0)
            continue
        for k in range(1,q+1):
            a=M[x,y]
            if a!=k:
                M[x,y]=k
                dE=energy(M)-E0
                p=min(1, np.exp(-dE*beta))
                #p= 1/(1+np.exp(dE*beta))
                if np.random.random() < p:
                    E0=E0+dE
                    break
                else:
                    M[x,y]=a
                    
        #print(E0)            
        E[i]=int(E0)
        l=l+1

        if i%conver==0:
            if Es==E0:
                print('Doesn\'t converge. Approximate solution: ')
                break
            else:
                Es=E0

        if E0==0:
            print('Completed. Solution: ')
            m=True
            break 

    print(M)
    print(E0)

    #plt.xlabel('n')
    #plt.ylabel('Energía')
    #plt.xlim((0,l))
    #plt.plot(np.arange(n), E, color='b', marker='.', markersize=0.1)

    #plt.show()

