def solution(map):
    h = len(map)
    w = len(map[0])
    moves = [(0,0,0)]
    iterations = len(moves)
    paths = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [(0,0,0)]
    pathCount = 0
    while True:
        pathCount +=1
        for _ in range(iterations):
            cx,cy,brokenWalls = moves.pop(0)
            for (x,y) in paths:
                nx,ny = cx+x, cy+y
                if ifValid(nx,ny,h,w):
                    nextMove = (nx,ny,brokenWalls+map[nx][ny])
                    if nextMove[2]<=1 and nextMove not in visited:
                        moves.append(nextMove)
                        visited.append(nextMove)
                if foundEnd(nx,ny,h,w):
                    return pathCount+1
                    
        iterations = len(moves)
        # visited += tmpVisited
    


def foundEnd(x,y,h,w):
    if y==w-1 and x==h-1:
        return True
    return False

def ifValid(x,y,h,w):
    if 0<=x<h and 0<=y<w:
        return True
    else:
        return False





x = solution([
            [0,1,1,1,1,1,1,1,1,1], 
            [0,0,0,0,1,0,1,1,1,1],
            [1,1,1,0,1,1,1,1,1,1], 
            [1,1,1,0,1,1,0,0,0,0],
            [1,1,1,0,1,1,0,1,1,0],
            [1,1,1,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,0,1,1,1],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,1,1,1],
            [1,1,1,1,1,1,0,1,0,0],
            ])
print(x)