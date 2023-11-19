import heapq
import time

# Define possible movements (up, down, left, right) disableing : and diagonals)
MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]# (1, 1), (1, -1), (-1, 1), (-1, -1)]

class Node():
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.g=0
        self.h=0
        self.f=0
    def __eq__(self, other):
        return self.position == other.position
    def __hash__(self):
        return hash(self.position)
    def __lt__(self,other):
        return self.f<other.f

def heuristic(node, goal):
    # This is a simple heuristic (Manhattan distance), because we not allowing diagnoal movement at the moment
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(grid, start, goal):
    nodecount =pushcount = 0
    # grid is the map
    # start is the starting postion
    # goal is the target postion
    start_node = Node(None, start)
    start_node.h = heuristic(start, goal)
    start_node.f = start_node.g+start_node.h
    end_node = Node(None,goal)
    
    open_list = [] # this is the expending "tip" of the search, use heap because we checking lowest f val neighbor
    close_set = set() # this is searched, no need to keep it as heap, but rather set
    
    heapq.heappush(open_list, start_node)#organized based on f score

    while open_list: #keep searching until path is found
        current = heapq.heappop(open_list) #consider the node with lowest f score
        if current == end_node:
            path = reconstruct_path(current)
            return (path,nodecount,pushcount)
        #put currnode into the closed list andd look at its neighbors
        close_set.add(current)

        for dx, dy in MOVEMENTS: # for each possible steps
            neighbor = (current.position[0] + dx, current.position[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]]!=1:
                #don't run into walls and keep within bounds

                neighborNode = Node(current,neighbor)
                if neighborNode in close_set:
                    #ignore node in close set already
                    continue
                nodecount +=1                
                neighborNode.h = heuristic(neighbor,goal)
                neighborNode.g = current.g + 1 # Assuming uniform cost for all movements
                neighborNode.f = neighborNode.h+neighborNode.g
                add_flag = True
                for i in range(0,len(open_list)):
                    openNode = open_list[i]
                    if openNode == neighborNode :
                        add_flag = False
                        #when neighborNode is already in open list
                        # if new g score is lower, the new path is better update parent and scores
                        if neighborNode.g<=openNode.g:
                            open_list[i] = neighborNode
                            heapq.heapify(open_list)
                            pushcount+=1
                            break
                if add_flag: #neighborNode not in open list
                    pushcount+=1
                    heapq.heappush(open_list, neighborNode)
    return (None,nodecount,pushcount)  # No path found

def reconstruct_path(currNode):
    path = []
    while currNode is not None:
        path.append(currNode.position)
        currNode = currNode.parent
    return path[::-1]

# Example usage:
if __name__ == "__main__":
    grid1 = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0]]
    grid2 = [[0,1,1,0,1,0,1],
             [0,0,0,0,0,0,0],
             [0,1,1,0,1,1,0],
             [0,0,1,0,0,1,0],
             [1,0,1,0,1,1,0],
             [1,0,0,0,1,0,0]]
    grid3 = [[0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0]]
    gridLs = [grid1,grid2,grid3]

    start = (0, 0)
    for grid in gridLs:
        goal = (len(grid)-1, len(grid[0])-1)
        starttime = time.time()
        path,nodeexplored,heapCount = astar(grid, start, goal)
        endtime = time.time()
        if path:
            print("Path found:", path)
        else:
            print("No path found.")
        print("Number of node explored: ",nodeexplored)
        print("The number of time the a node is push to a heap or heapify is called: ",heapCount)
        print("Execution time:", endtime-starttime)
