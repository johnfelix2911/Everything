import cv2
import numpy as np
import random
import math

# Read the image
img = cv2.imread("map123.jpg")
k=img.copy()
last=img.copy()

_, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
img = cv2.imread("map123.jpg", cv2.IMREAD_GRAYSCALE)
# Convert the image to a NumPy array
np.save("map1234.npy", img)
grid= np.load("map1234.npy")

#obstacle 1 and road 0
grid[grid >= 128] = 1
grid[grid < 128] = 0

         

it = 1000000
grid = np.array(img)
goal = (337, 11)
ss = 45
start = (296, 293)


class treenode():
    def __init__(self, locx, locy):
        self.locx = locx
        self.locy = locy
        self.children = []
        self.parent = None


class RRT():
    def __init__(self, start, goal, it, grid, ss):
        self.randomtree = treenode(start[0], start[1])
        self.goal = treenode(goal[0], goal[1])
        self.nearestnode = None
        self.it = min(it, 10000000)
        self.grid = grid
        self.rho = ss
        self.path_dis = 0
        self.nearestdist = 10000
        self.numway = 0
        self.waypoint = []

    def add_child(self, locnx, locny):
        if (locnx == self.goal.locx):
            self.nearestnode.children.append(self.goal)
            self.goal.parent = self.nearestnode
        else:
            child = treenode(locnx, locny)
            self.nearestnode.children.append(child)
            child.parent = self.nearestnode

    def sample_point(self):
        locnx = random.randint(1, grid.shape[1])
        locny = random.randint(1, grid.shape[0])
        point = np.array([locnx, locny])
        return point

    def steer(self, locstart, locend):
        offset = self.rho * self.unitvec(locstart, locend)
        point = np.array([locstart.locx + offset[0], locstart.locy + offset[1]])
        if point[0] >= grid.shape[1]:
            point[0] = grid.shape[1] - 1
        if point[1] >= grid.shape[0]:
            point[1] = grid.shape[0] - 1
        return point

    def isinobs(self, locnstart, locnend):
        u = self.unitvec(locnstart, locnend)
        test = np.array([0.0, 0.0])
        for i in range(self.rho):
            test[0] = locnstart.locx + u[0] * i
            test[1] = locnstart.locy + u[1] * i
            if test[0]>=grid.shape[1]:
                test[0]=grid.shape[1]-1
            if test[1]>=grid.shape[0]:
                test[1]=grid.shape[0]-1
            if self.grid[int(round(test[1])), int(round(test[0]))] == 1:
                return True
        return False

    def unitvec(self, locnstart, locnend):
        x = locnstart.locx - locnend[0]
        y = locnstart.locy - locnend[1]
        v = np.array([x, y])
        u = v / np.linalg.norm(v)
        return u

    def find_nearest(self, root, point):
        if not root:
            return
        d = self.dis(root, point)
        if d <= self.nearestdist:
            self.nearestdist = d
            self.nearestnode = root
        for child in root.children:
            self.find_nearest(child, point)

    def dis(self, node1, point):
        d = np.sqrt((node1.locx - point[0]) * (node1.locx - point[0]) + (node1.locy - point[1]) * (
                node1.locy - point[1]))
        return d

    def goalFound(self, point):
        if self.dis(self.goal, point) <= self.rho:
            return True
        pass

    def resetnearest(self):
        self.nearestnode = None
        self.nearestdist = 10000

    def retrace(self, goal):
        if goal.locx == self.randomtree.locx:
            return
        self.numway += 1
        currp = np.array([goal.locx, goal.locy])
        self.waypoint.insert(0, currp)
        self.retrace(goal.parent)


# Initialize OpenCV window


# Display the gridr
cv2.circle(k,(int(start[0]),int(start[1])),2,(0,0,255),-1)

cv2.circle(k,(int(goal[0]),int(goal[1])),1,(255,0,0),3)

 
rrt = RRT(start, goal, it, grid, ss)

for i in range(rrt.it):
    rrt.resetnearest()
    print("iteration no.", i + 1)
    point = rrt.sample_point()
    rrt.find_nearest(rrt.randomtree, point)
    new = rrt.steer(rrt.nearestnode, point)
    bool = rrt.isinobs(rrt.nearestnode, new)
    if not bool:
        rrt.add_child(new[0], new[1])
        cv2.line(k, (int(rrt.nearestnode.locx), int(rrt.nearestnode.locy)),
                 (int(new[0]), int(new[1])), (0, 255, 0), 1)
        cv2.circle(k,(int(new[0]),int(new[1])),2,(255,0,0),-1)

    else:
        i = i - 1
        continue
    if rrt.goalFound(new):
        rrt.add_child(goal[0], goal[1])
        print("Goal found!")
        break

    cv2.imshow('RRT', k)
    cv2.waitKey(1)

rrt.retrace(rrt.goal)
rrt.waypoint.insert(0, start)
for i in range(len(rrt.waypoint) - 1):
    cv2.line(last, (int(rrt.waypoint[i][0]), int(rrt.waypoint[i][1])),
             (int(rrt.waypoint[i + 1][0]), int(rrt.waypoint[i + 1][1])), (0, 255, 0), 2)
    cv2.imshow('RRT', last)
    cv2.waitKey(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
