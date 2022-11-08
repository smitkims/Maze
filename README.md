# Maze

The program will ask the user to enter shape of map, labyrinth map, initial position. 
The agent in the labyrinth should follow the ‘Left-hand rule’. The agent can go ahead with only the left wall.
The program should print the ‘number of steps’ to escape labyrinth if the agent can escape. If not, just print ‘impossible’

Input:
N M separated by a newline (‘\n‘), # of rows and columns each
- labyrinth map (each point is ‘=’ or ‘+’, consecutive string)
- initial position x, y (x and y separated by a newline (‘\n‘), starting
from zero)
- Guarantee following two statements
  1. The initial position is always on the edge (x == 0 or x ==
    M-1 or y == 0 or y == N-1).
  2. At the initial position, there is wall on the left side of the
    agent.
    
Output:
Number of steps to escape the labyrinth if escaping is possible by Left-hand rule
- Turning is not counted as a step
- Only the number of moving cells is counted as a step
- The escaping is completed after the agent go out of the
map
- At initial position, the step count is 0
- If impossible, only print ‘impossible’
- If initial position and last position (escaping position) is
same, print ‘impossible’, not the number of steps
