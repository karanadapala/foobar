import math
def solution(total_lambs):
    # Your code here
    return maxPoss(total_lambs)-minPoss(total_lambs)
def minPoss(total_lambs):
    count = 0
    n = 0
    sum = 0
    while True:
        if sum>total_lambs:
            break
        sum += 2**n
        count+=1
        n+=1
    print(count-1)
    return count-1
def maxPoss(total_lambs):
    count = 0
    n = 2
    n0 = 1
    sum = 0
    while True:
        if sum>total_lambs:
            break
        if count < 2:
            sum += 1
            count+=1
            continue
        sum += n
        n=n+n0
        n0=n-n0
        count+=1
    print(count-1)
    return count-1

print(solution(143))