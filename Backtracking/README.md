# Backtracking

A backtracking algorithm is a problem solving algorithm that uses a brute force approach for finding the desired output

The brute force approach tries out all the possible and choose the desired/best solution.

the term backtracking suggests that if the current solution is not suitable, then backtrack and try other solution. thus, recursion is used in this approach

this approach is used to solve problems that have multiple solutions. if you want an optimal solution, you must go for dynamic programming

## 1. Basic Concept of Backtracking

Backtracking is essentially a depth-first search (DFS) with the ability to backtrack when it hits a dead end. It involves:

- Exploring options: Trying to build a solution incrementally.
- Constraints: Checking if the current solution is valid.
- Backtracking: Abandoning the current path and trying another path if it doesn't lead to a solution.

## 2. When to Use Backtracking

Backtracking is useful in scenarios where:

- The problem can be broken down into smaller, similar sub-problems.
- You need to find all solutions to a problem.
- The problem requires a trial-and-error approach.

## 3.Key Components of Backtracking

1. Choice: Make a choice.
2. Constraints: Validate the choice.
3. Goal: Check if the goal is reached.
4. Backtrack: If not valid, undo the choice and try another.

## Example

```python
def printPermutation(str, per = "", index = 0):
    count = 0
    if len(str) == 0:
        print(per)
        count += 1
        return
    for i in range(len(str)):
        curr = str[i]
        newString = str[:i] + str[i+1:]
        printPermutation(newString, per + curr, index + 1)

str = "ABCD"
printPermutation(str)
```
