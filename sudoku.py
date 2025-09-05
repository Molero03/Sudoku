import time
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
            if i < 3 and j < 3:
                for x in range(3):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i < 3 and j>2 and j < 6:
                for x in range(3):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i < 3 and j>5 and j < 9:
                for x in range(3):
                    for y in range(6,9):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i >2 and i < 6 and j < 3:
                for x in range(3,6):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>2 and i < 6 and j>2 and j < 6:
                for x in range(3, 6):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>2 and i < 6 and j>5 and j < 9:
                for x in range(3, 6):
                    for y in range(6,9):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>5 and i < 9 and j < 3:
                for x in range(6, 9):
                    for y in range(3):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>5 and i < 9 and j>2 and j < 6:
                for x in range(6, 9):
                    for y in range(3,6):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
            elif i>5 and i<9 and j>5 and j<9:
                for x in range(6,9):
                    for y in range(6,9):
                        if M[i,j]==M[x,y] and x!=i and y!=j:
                            E=E+1
    return E



#H= -sum_{ij} delta_{ij} 
q=9
n=500000
numbers=np.array([])
conver=5000
beta=3.

Mo= np.matrix([[0,0,0,0,9,0,0,0,0],
             [0,1,8,7,0,0,0,0,0],
             [4,0,0,8,0,0,0,0,0],
             [0,6,0,0,0,8,0,0,0],
             [1,0,0,4,0,0,3,0,0],
             [0,7,0,0,0,0,8,2,9],
             [0,2,0,0,1,0,0,0,0],
             [0,0,0,9,0,4,2,7,0],
             [6,0,0,0,5,0,1,0,0]])

for i in range(q):
        for j in range(q):
            if Mo[i,j]!=0:
                numbers=np.append(numbers, '('+str(i) + ',' +str(j) +')')



start=time.time()

m=False
while m==False:

    M=Mo.copy()


    for i in range(q):
        for j in range(q):
            if M[i,j]==0:
                M[i,j]= np.random.randint(1,q+1)


    E0=energy(M)  
    #E=np.zeros(n, dtype=np.int16)
    #l=0    
    steps=0
    for i in range(n):
    
        x=np.random.randint(q)
        y=np.random.randint(q)
        number= '('+str(x) + ',' +str(y) +')'
        while number in numbers:
            x=np.random.randint(q)
            y=np.random.randint(q)
            number= '('+str(x) + ',' +str(y) +')'
        
        for k in range(1, q+1):
            
            a=M[x,y]
            if a!=k:
                M[x,y]=k
                dE=energy(M)-E0
                p=min(1, np.exp(-dE*beta))
                #p= 1/(1+np.exp(dE*beta))
                if np.random.random() < p:
                    E0=E0+dE
                    if dE!=0:
                        steps=0
                    break
                else:
                    M[x,y]=a
                    
        #print(E0)            
        #E[i]=int(E0)
        #l=l+1
        

        if steps==conver:
            print('Doesn\'t converge. Approximate solution: ')
            break

        if E0==0:
            print('Completed. Solution: ')
            m=True
            break 

        steps=steps+1

    print(M)
    print(E0)



    #plt.xlabel('steps')
    #plt.ylabel('Energy')
    #plt.xlim((0,l))
    #plt.plot(np.arange(n), E, color='b', marker='.', markersize=0.1)
    #plt.show()


tiempo=time.time()-start
print(str(tiempo) + ' seconds')







