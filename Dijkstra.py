import time
inf = float('inf')

dirc = [[0,1],[1,0],[0,-1],[-1,0]]
#direction = ["right", "down", "left", "up"]

path = []
pre = []

def create(maze, start):
    Q = []
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[i][j] != 1:
                Q.append(i*len(maze[0])+j)
    dis = [inf] * len(Q)
    dis[Q.index(start)] = 0
    return Q, dis

def Path(S, pre, start, end):
    path = []
    point = end
    while point != start:
        path.insert(0, pre[S.index(point)-1])
        point = pre[S.index(point)-1]
    path.append(end)
    return path

def Dijkstra(maze, start, end):
    nodecount=0
    S = []
    dis_determ = []
    start = start[0] * len(maze[0]) + start[1]
    end = end[0] * len(maze[0]) + end[1]
    Q, dis = create(maze, start)
    temp1  = []
    temp2  = []
    pre = []
    while(Q != []):
        point = Q[dis.index(min(dis))]
        S.append(point)
        dis_determ.append(dis[Q.index(point)])
        if temp1 != []:
            pre.append(temp1[temp2.index(point)])
        if point == end:
            path = Path(S, pre, start, end)
            return (path,nodecount)
        dis.pop(Q.index(point))
        Q.pop(Q.index(point))
        for point in S:
            for i in range (0,4):
                nodecount +=1
                nextpoint = [int(point/len(maze[0]))+ dirc[i][0], point%len(maze[0]) + dirc[i][1]]
                if nextpoint[0] < 0 or nextpoint[1] < 0 or nextpoint[0] > len(maze) - 1 or nextpoint[1] > len(maze[0]) - 1:
                    continue
                elif nextpoint[0]*len(maze[0])+nextpoint[1] in Q:
                    dis[Q.index(nextpoint[0]*len(maze[0])+nextpoint[1])] = dis_determ[S.index(point)]+1
                    temp1.append(point)
                    temp2.append(nextpoint[0]*len(maze[0])+nextpoint[1])


    return False

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
        path,nodeexplored = Dijkstra(grid, start, goal)
        endtime = time.time()
        if path:
            print("Path found:", path)
        else:
            print("No path found.")
        print("Number of node explored: ",nodeexplored)
        print("The number of time the a node is push to a heap or heapify is called: ",nodeexplored)
        print("Execution time:", endtime-starttime)