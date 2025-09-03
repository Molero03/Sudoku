# Sudoku Solver

## Description
The project consists of a Python program that solves a given Sudoku problem using a probabilistic algorithm based on the Potts model. The main idea of the algorithm is to define an energy for the system and minimize it.

<img src="https://i.imgur.com/GLiEH3l.jpeg" height="50%" width="50%"/>

Given an element of the system (blue mark), the energy contribution of that element to the system will be the number of "neighbours" (red marks) with the same number as the original element. A similar rule is applied throughout the board.

Sometimes the system can get stuck in an approximate solution with low energy. To avoid that, a convergence check has been added to the program. Thus, if the energy remains the same for a set number of iterations, the program will restart from a new random state. In order to change the convergence length, just change the value of the variable 'conver'. 

## How to use the program

To use the program you just have to write the Sudoku problem in the matrix 'Mo', treating each blank space in your Sudoku as a 0 in the matrix. Once the Sudoku problem is set, you just have to run the program.

<img src="https://i.imgur.com/hXtSd9f.png" height="50%" width="50%"/>

<img src="https://i.imgur.com/2OnEraI.png" height="50%" width="50%"/>

Note: If the input problem is too hard, the program may take a while to solve it.

