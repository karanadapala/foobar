def solution(h, q):
    # Your code here
    tree = {}
    for i in range(0,h):
        tree[i]=[]
    height = 0
    num = 1
    while num<2**h:
        if len(tree[height])==0:
            tree[height].append(num)
        else:
            if len(tree[height])%2==0:
                height +=1
                tree[height].append(num)
            else:
                height = 0
                tree[height].append(num)
        print(tree)
        num+=1
    FinalList = []
    for j in q:
        for k in tree:
            if j in tree[k]:
                if k==h-1:
                    FinalList.append(-1)
                else:
                    temp=int(tree[k].index(j)/2)
                    FinalList.append(tree[k+1][temp])

    return FinalList

print(solution(3, [19, 14, 28]))