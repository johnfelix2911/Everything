import numpy as np
import cv2

def isNearWall(pt):
    if img[i[1]][i[0]+5][0]<10 and img[i[1]][i[0]+5][1]<10 and img[i[1]][i[0]+5][2]<10:
        return True
    if img[i[1]+5][i[0]][0]<10 and img[i[1]+5][i[0]][1]<10 and img[i[1]+5][i[0]][2]<10:
        return True
    if img[i[1]][i[0]-5][0]<10 and img[i[1]][i[0]-5][1]<10 and img[i[1]][i[0]-5][2]<10:
        return True
    if img[i[1]-5][i[0]][0]<10 and img[i[1]-5][i[0]][1]<10 and img[i[1]-5][i[0]][2]<10:
        return True
    return False

def isCollisionFree(pt1, pt2, img):
    line = np.linspace(pt1, pt2, num=10, dtype=int)
    for i in line:
        if np.any(img[i[1]][i[0]])==0:
            return 0
    return 1

def retracePath(img, parentTracker, node, start):
    if (node == start):
        return
    else:
        cv2.line(img, node, parentTracker[node], (0, 255, 0), 2)
        cv2.imshow("hehe", img)
        cv2.waitKey(100)
        retracePath(img, parentTracker, parentTracker[node], start)

def allNeighboursInVisited(list_of_neghbours, vis):
    for i in list_of_neghbours:
        if i[0] not in vis:
            return False
    return True

def Astar(img, node, goal, neighbours, map, parentTracker, vis, start):
    vis.append(node)
    if (node == goal):
        retracePath(img, parentTracker, goal, start)
    for i in neighbours[node]:
        g_score = map[node][0] + i[1]
        h_score =round(((goal[0] - i[0][0])**2 + (goal[1] - i[0][1])**2)**0.5)
        if i[0] not in map.keys():
            map[i[0]] = [g_score, h_score]
        else:
            if (map[i[0]][0] + map[i[0]][1])>(h_score + g_score):
                map[i[0]][0] = g_score
                map[i[0]][1] = h_score
    min = 10000
    next_node = node
    for i in neighbours[node]:
        f_score = map[i[0]][0] + map[i[0]][1]
        if f_score<min:
            if i[0] not in vis:
                min = f_score
                next_node = i[0]
    parentTracker[next_node] = node
    cv2.line(img, node, next_node, (0,0,255), 2)
    cv2.imshow("hehe", img)
    cv2.waitKey(100)
    Astar(img, next_node, goal, neighbours, map, parentTracker, vis, start)

#(14, 30), (14, 502), (670, 502), (670, 30)
#(62, 500) to (154, 500) is easy
#(244, 34) to (666, 458) is hard
r = 40
k = 10
img = cv2.imread("maze.png")
img = cv2.resize(img, (round(img.shape[1]*1.5), round(img.shape[0]*1.5)))
cv2.imshow("hehe", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
x = np.random.rand(1000, 2) * (img.shape[1]-1, img.shape[0]-1)
x = x.astype(int)
nodes = []
for i in x:
    if (i[0]>=14 and i[0]<=670):
        if (i[1]>=30 and i[1]<=502):
            if img[i[1]][i[0]][0]>10 and img[i[1]][i[0]][1]>10 and img[i[1]][i[0]][2]>10:   
                if not isNearWall(i):   
                    cv2.ellipse(img, i, (2,2), 0, 0, 360, (0,0,255), -1)
                    nodes.append((i[0], i[1]))
start  = (62, 500)
cv2.ellipse(img, start, (2,2), 0, 0, 360, (0,0,255), -1)
goal = (154, 500)
cv2.ellipse(img, goal, (2,2), 0, 0, 360, (0,0,255), -1)
nodes.append(start)
nodes.append(goal)
#print(nodes)
neighbours = {}
neighbours_count = {}
for i in nodes:
    neighbours[i] = []
    neighbours_count[i] = 0
    for j in nodes:
        if (i!=j and neighbours_count[i]<=k):
            dist = np.linalg.norm(np.array(i) - np.array(j))
            if (dist<=r):
                    check = isCollisionFree(i, j, img)
                    if (check):
                        neighbours[i].append((j, int(dist)))
                        neighbours_count[i] = neighbours_count[i] + 1
                        cv2.line(img, i, j, (255,0,0), 1)
#print(neighbours)
map = {}
parentTracker = {}
vis = []
map[start] = [0, abs(start[0] - goal[0]) + abs(start[1] - goal[1])] #(g_score, h_score)
Astar(img, start, goal, neighbours, map, parentTracker, vis, start)
cv2.imshow("hehe", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
