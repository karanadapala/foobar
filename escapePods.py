import numpy as np
from collections import deque

def FordFulkerson(augMatrix):
    parent = {}
    visited = []
    paths = deque([0])
    parentNode = -1
    MaxFlow = 0
    # count = 0
    while paths:
        # print(paths)
        currNode = paths.popleft()
        visited.append(currNode)
        parent[currNode]=parentNode
        # print(currNode)
        
        if currNode == len(augMatrix)-1:
            parent[currNode]=parentNode
            l = currNode
            tmp = float('inf')
            tmpPath = []
            while l>0:
                tmpPath.append(tuple((parent[l],l)))
                if augMatrix[parent[l]][l]<tmp:
                    tmp = augMatrix[parent[l]][l]
                l = parent[l]
            # print(tmp,'xxxxx')
            MaxFlow += tmp
            for m,n in tmpPath:
                augMatrix[m][n]-=tmp
            parent = {}
            visited = []
            paths = deque([0])
            parentNode = -1
            continue
        for i in range(0,len(augMatrix[currNode])):
            if augMatrix[currNode][i]!=0 and i not in visited:
                paths.appendleft(i)
                parentNode = currNode
        # count +=1
        # if count ==25:
        #     break
    return MaxFlow



def solution(entrances, exits, path):
    pathLen = len(path)
    source = []
    sink = []
    for _ in range(pathLen+2):
        source.append(0)
        sink.append(0)
    path.insert(0,source)
    path.append(sink)
    for i in entrances:
        path[0][i+1]=sum(path[i+1])
    for i in range(1,pathLen+1):
        path[i].insert(0,0)
        path[i].append(0)
    for i in exits:
        if sum(path[i+1])==0:
            path[i+1][-1]=float('inf')
        else:
            path[i+1][-1]=sum(path[i+1])
    # print(np.matrix(path))
    return FordFulkerson(path)

if __name__ == "__main__":
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))