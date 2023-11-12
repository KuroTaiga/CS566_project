import queue

# Define possible movements (up, down, left, right) disableing : and diagonals)
MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]# (1, 1), (1, -1), (-1, 1), (-1, -1)]
class Node():
    def __init__(self,parent=None,position=None):
        self.position = position
        self.parent = parent
    def __eq__(self, other):
        return self.position==other.position
    
def reconstruct_path(currNode):
    path = []
    while currNode is not None:
        path.append(currNode.position)
        currNode = currNode.parent
    return path[::-1]

def bfs(grid,start,goal):
    nodecount = 0
    nodeQueue = queue.Queue()
    startNode = Node(None,start)
    goalNode = Node(None,goal)
    nodeQueue.put(startNode)
    while(not nodeQueue.empty()):
        currNode = nodeQueue.get()
        if currNode == goalNode:
            path = reconstruct_path(currNode)
            return (path,nodecount)
        for dx, dy in MOVEMENTS: # for each possible steps
            neighbor = (currNode.position[0] + dx, currNode.position[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]]!=1:
                nodecount += 1
                # when neighbor is a legal move put it in queue
                neighborNode = Node(currNode,neighbor)
                nodeQueue.put(neighborNode)
    return (None,nodecount) # no path found

#example call
if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0]]
    start = (0,0)
    goal  = (4,4)
    path,nodeexplored = bfs(grid,start,goal)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
    print(nodeexplored)

