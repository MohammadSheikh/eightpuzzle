# Eight Tile Puzzle

## Introduction
The concept of “Eight Puzzle” derives from the actual game, “Fifteen Puzzle”. This consists of a grid that is 3x3 with 9 entries 0 through 8, with 0 being the “empty” one. This is so that each tile could be unique to its own integer. A tile next to 0 can be moved into its place, but that previous tile must be assigned to be 0.
Dr. Eamonn introduced an interesting first project idea in Fall 2021, CS 170 at UCR. This report consists of details through the completion of this project. Algorithms such as UCS, Manhattan Distance, and Misplaced Tiles were applied with the programming language Python.
## Comparison of Algorithms
Uniform Cost Search, A* using the Manhattan Distance heuristic, and A* using the Misplaced Tile heuristic are the algorithms that were implemented.
### Uniform Cost Search
The Uniform Cost Search strictly expands cheapest nodes only, and cost would be g(n). Also, h(n) will always be 0. This algorithm overall mimics the A* algorithm.
### Misplaced Tile
This algorithm simply searches for tiles that are misplaced in the puzzle. Of course, the empty tile isn’t counted since it’s blank. This is where the depth would be modified to its appropriate number of tiles that are not in the goal state.
### Manhattan Distance
This algorithm looks for misplaced tiles as well, but also keeps in mind regarding the amount of tiles that are not in the same position of the goal state. The depth in this case would be a summation of the cost of the distant tiles that are misplaced.
## Conclusion
After a brief comparison of the three algorithms implemented in this project, we can determine that the Manhattan Distance is the best since expanded the least amount of nodes while simultaneously not going through such a high solution depth. The next best was misplaced tile heuristic, and the worst was Uniform Cost Search, which is basically BFS but the heuristic cost being hardcoded to 0. Misplaced tile and Manhattan distance both start off initially similar, but start to veer off when the amount of depth reaches close to 12.
