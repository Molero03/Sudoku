<h1>Sudoku Solver</h1>

<h2>Description</h2>
The project consists on a python program that solves a given sudoku problem using a probabilistic algorithm based on the Potts model. The main idea of algorithm is to define an energy for the system and the propose a change for one of its elements, obtaining a new energy in the process. Then, the probability of finally performing the change is given by the minimum value between 1 and e^(-the energy difference). In this way, the system will be more likely evolve into a minimum energy state. In this case the energy is defined as follows:  <br />

<img src="https://i.imgur.com/GLiEH3l.jpeg" height="50%" width="50%"/>

Given an element of the system (blue mark), the energy contribution of that element to the system will be the number of "neighbours" (red marks) with the same number as the original element. A similar energy definition can be made for the Mini Sudoku problem. <br />

Sometimes the system can get stuck in an approximate solution with low energy. To avoid that, a convergence check has been added in the program. Thus, if the energy remains the same for a set number of steps, the program is restarted and the approximate solution is displayed along with its corresponding energy. You can change the convergence length by changing the value of the variable named 'conver'. <br />

<h2>How to use the program</h2> 

To use the program you just have to write the sudoku problem in the matrix 'Mo', treat each blank space in your sudoku as a 0 in the matrix. Once the sudoku problem is set you just have to run the program. A message will appear when the solution is found. <br />

<img src="https://i.imgur.com/hXtSd9f.png" height="50%" width="50%"/>

<img src="https://i.imgur.com/2OnEraI.png" height="50%" width="50%"/>






