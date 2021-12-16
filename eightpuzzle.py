import heapq
from copy import deepcopy

def driver():
    choice = int(input("Welcome to Mahamadsaad's 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own: "))

    # Default choice
    if choice == 1:
        setup = [[1, 2, 3], 
        [4, 0, 6], 
        [7, 5, 8]]
    
    # User Input Criteria
    if choice == 2:
        print("Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles."
        " Enter the puzzle demilimiting the numbers with a space. Type RETURN only when finished.")

        first_line = (input("Enter the first row: ")).split(' ')
        second_line = (input("Enter the second row: ")).split(' ')
        third_line = (input("Enter the third row: ")).split(' ')

        for i in range(0,3):
            first_line[i] = int(first_line[i])
            second_line[i] = int(second_line[i])
            third_line[i] = int(third_line[i])
        
        setup = first_line, second_line, third_line
    
    algorithm_choice = int(input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) the Manhattan Distance Heuristic: "))

    searching(algorithm_choice, setup)

class Node:
    goal_test = [[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 0]]

    def __init__(self, init_state, depth, cost):
        self.init_state = init_state
        self.depth = depth
        self.cost = cost
        
    def __eq__(self, other):
        return ((self.init_state, self.depth, self.cost, self.goal_test) == (other.init_state, other.depth, other.cost, other.goal_test))
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return ((self.init_state, self.depth, self.cost, self.goal_test) < (other.init_state, other.depth, other.cost, other.goal_test))
    def __gt__(self, other):
        return ((self.init_state, self.depth, self.cost, self.goal_test) > (other.init_state, other.depth, other.cost, other.goal_test))
    def __le__(self, other):
        return ((self.init_state, self.depth, self.cost, self.goal_test) <= (other.init_state, other.depth, other.cost, other.goal_test))
    def __ge__(self, other):
        return ((self.init_state, self.depth, self.cost, self.goal_test) >= (other.init_state, other.depth, other.cost, other.goal_test))

def searching(algorithm_choice, setup):
    temp = []
    exp_nodes = 0
    max_size_queue = 0

    if algorithm_choice == 1:
        no_existing_heuristic_cost = 0
        starting_node = Node(setup, 0, no_existing_heuristic_cost)
    
    # Misplaced tile
    if algorithm_choice == 2:
        heuristic = misplaced_tile_heuristic(setup)
        starting_node = Node(setup, 0, heuristic)
    
    # Manhattan Distance
    if algorithm_choice == 3:
        heuristic = manhattan_distance_heuristic(setup)
        starting_node = Node(setup, 0, heuristic)

    # We want to push it onto the heap queue by making it into a list form
    heapq.heappush(temp, starting_node)

    while True:
        # Transform the list variable "temp" into a heap
        heapq.heapify(temp)
        # Popping off smallest item
        current_node = heapq.heappop(temp)
        print("The best state to expand with a g(n) = ", current_node.depth, " and h(n) = ", current_node.cost ," is:")
        for i in current_node.init_state:
            print(i)
        
        # The if-statement that kills the loop if goal is met.
        if current_node.init_state == starting_node.goal_test:
            break

        # Else, if goal isn't met, expand the node into lists, depending on top, bottom, left, and right rows and columns
        expansion = expand_it(current_node)

        # Iterating through the expanded list of nodes
        for k in range(len(expansion)):
            if k is not None:

                # Manhattan Distance
                if algorithm_choice == 3:
                    expansion[k].cost = manhattan_distance_heuristic(expansion[k].init_state)
                # Misplaced Tile
                if algorithm_choice == 2:
                    expansion[k].cost = misplaced_tile_heuristic(expansion[k].init_state)
                
                # UCS, in this case each expanded node as a h(n) of 1
                if algorithm_choice == 1:
                    expansion[k].cost = 1
            
            # Everytime there is a new entry in the list of nodes, that means a node has been expanded overall.
            exp_nodes += 1

            # Push expanded nodes back into heap temp list
            heapq.heappush(temp, expansion[k])

        # The size of the temp (i.e. current node) cannot exceed the size of the queue
        if len(temp) > max_size_queue:
            max_size_queue = len(temp)
        
    # Final stage/state
    print("Goal State.")
    for i in current_node.init_state:
        print(i)
    print("Solution Depth:", current_node.depth)
    print("Number of Nodes Expanded", exp_nodes)
    print("Maximum Queue Size:", max_size_queue)
            

def expand_it(setup):
    expansion = []
    column = 0
    row = 0

    # We need to identify WHERE potential 0's are located in the eight-puzzle
    for i in range(len(setup.init_state)):
        for j in range(len(setup.init_state)):
            if setup.init_state[i][j] == 0:
                row = i
                column = j
    
    if column != len(setup.init_state) - 1 : # the right-most column
        right_column = deepcopy(setup.init_state)
        # sliding over the stuff from the column right 
        right_column[row][column] = right_column[row][column + 1] 
        # now zero-ing it out
        right_column[row][column + 1] = 0

        # Node creation for the sole right side itself
        right_side = Node(right_column, setup.depth+1, 0)
        expansion.append(right_side)

    if row != len(setup.init_state) - 1: # the bottom-most row
        bottom_row = deepcopy(setup.init_state)
        # sliding over the stuff from the row bottom 
        bottom_row[row][column] = bottom_row[row + 1][column] 
        # now zero-ing it out
        bottom_row[row + 1][column] = 0

        # Node creation for the sole bottom side itself
        bottom_side = Node(bottom_row, setup.depth+1, 0)
        expansion.append(bottom_side)
    if column != len(setup.init_state) - 3: # the left-most column
        left_column = deepcopy(setup.init_state)
        # sliding over the stuff from the column left 
        left_column[row][column] = left_column[row][column - 1] 
        # now zero-ing it out
        left_column[row][column - 1] = 0

        # Node creation for the sole left side itself
        left_side = Node(left_column, setup.depth+1, 0)
        expansion.append(left_side)
    if row != len(setup.init_state) - 3: # the top-most row
        top_row = deepcopy(setup.init_state)
        # sliding over the stuff from the row top 
        top_row[row][column] = top_row[row - 1][column] 
        # now zero-ing it out
        top_row[row - 1][column] = 0

        # Node creation for the top right side itself
        top_side = Node(top_row, setup.depth+1, 0)
        expansion.append(top_side)
    
    # Return a list of however many nodes were created, which would range between 0 to 4.
    return expansion



def misplaced_tile_heuristic(setup):
    # Need to access "goal state"
    temp = Node(setup,0,0)

    num = 0
    for i in range(len(setup)):
        for j in range(len(setup)):

            # if the current state and goal state isn't equal, meaning if it's not in the proper setting,
            #   then it is "misplaced"
            # AND if the current state's tiles don't contain an empty (0) tile, 
            if setup[i][j] != temp.goal_test[i][j]:
                if setup[i][j] != 0:
                    # increase 1 to the cost counter everytime
                    num += 1
    return num

def manhattan_distance_heuristic(setup):
    num = 0
    length = 1
    init_i = 0
    init_j = 0
    goal_i = 0
    goal_j = 0

    # Need to access "goal state"
    temp = Node(setup,0,0)

    # 3 x 3 tiles = 9
    tiles_amount = 9

    while length != tiles_amount: 
        # Double for loop for rows and columns
        for i in range(len(setup)):
            for j in range(len(setup)):

                #Compare current state and goal states
                if temp.goal_test[i][j] == length:
                    goal_i = i
                    goal_j = j

                if setup[i][j] == length:
                    init_i = i
                    init_j = j

        # Differentiating between init current state and goal state
        difference_of_i = abs(goal_i - init_i)
        difference_of_j = abs(goal_j - init_j)

        # Adding onto the number of steps for the cost (heuristic). AKA the manhattan distance
        num += difference_of_i + difference_of_j

        length += 1

    return num



driver()
