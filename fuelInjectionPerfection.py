import math

def solution(n):
    # Your code here
    n = int(n)
    global count
    count = 0
    pwr = math.log(n,2)
    if pwr.is_integer():
        count = pwr
    else:
        solve(n,pwr)
    return int(count)

def solve(n,exp):
    global count
    nearest = round(exp)
    pwr2value = 2**nearest
    if pwr2value>n and pwr2value-n==1:
        count=count+1+nearest
        return count
    else:
        if pwr2value>n:
            prevPwr = nearest
            pwr2value /=2
            nearest -= 1
        else:
            prevPwr = nearest+1
        diff = n-pwr2value
            
        while True:
            if 2**prevPwr-n==1:
                count = count+1+prevPwr
                return count
            if diff%2==1 and diff!=1:
                diff -= 1
                count +=1
            diff /= 2
            prevPwr = nearest
            nearest-=1
            count +=1
            if diff==1:
                count = count+1+nearest
                return

print(solution(30))