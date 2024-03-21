# Simplex-Algorithm
This repository contains a concise implementation of the simplex algorithm in python using only Numpy. Solve linear programming problems efficiently with this easy-to-understand codebase.
The is a really simple Complex procedural algorithm that takes simple 6 Steps : 
## Initialization:
Begin with a basic feasible solution. This involves selecting a set of basic variables and setting them to their non-negative values, while setting the non-basic variables to zero. This forms the initial basic feasible solution.

## Calculation of the Reduction Cost:
Calculate the reduction cost (or shadow price) for each non-basic variable. This is done by determining how much the objective function value would change if a small positive amount of the corresponding variable were added to the current basic feasible solution.

## Determine the Vector Entering the Base:
Select the variable with the most negative reduction cost (if maximizing) or the most positive reduction cost (if minimizing). This variable will enter the base and become a basic variable in the next iteration.

## Pivoting:
Determine the pivot element by selecting a row where the ratio of the right-hand side to the entering variable's coefficient is the smallest non-negative value. This row corresponds to the constraint that will be relaxed to make the entering variable positive.
Perform a pivot operation to update the basic and non-basic variables, moving towards a better solution.

## Iteration:
Repeat the process of calculating reduction costs, determining the entering variable, and pivoting until an optimal solution is found or it is determined that the problem is infeasible or unbounded.

The algorithm terminates when an optimal solution is found, or when it is determined that the problem is infeasible or unbounded.
