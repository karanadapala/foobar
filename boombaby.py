def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)
    if x==1 and y==1:
        return "0"
    if x == y:
        return "it would be not possible"
    if x ==1 or y ==1 :
        if x>y:
            return "{}".format(x-1)
        else:
            return "{}".format(y-1)
    else:
        if y%2==0:
            y +=1
        OriginLevel = x-1
        if y>x:
            addition = int((y-1)/x)
            return "{}".format(OriginLevel+addition)
        else:
            if x%2==1:
                z = x-1
            if z==y:
                return "{}".format(z-1)
            if y<z/2:
                deletion = x-(int(z/2 + (z/2-y)))
                return "{}".format(OriginLevel-deletion)
            else:
                deletion = x-y
                return "{}".format(OriginLevel-deletion)

print(solution('{}'.format(13),'21'))




    
    