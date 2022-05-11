from itertools import product

def solution(n):
    answer = ''
    # share = int(n/3)
    # remain = int(n%3)
    i=0
    if n==1:
        return '1'
    if n==2:
        return '2'
    if n==3:
        return '4'
    
    for o in range(0,10000000000):
        #print("i: {} o: {}".format(i,o))
        if i<=n<i+3**o:
            tmp = list(product([1,2,4], repeat=o))
            #print(tmp)
            sum=0
            for k in range(0,o):
                sum+=3**k
            #print(sum)
            idx = n-sum 
            for j in tmp[idx]:
                answer += str(j)
            return answer 
        else: 
            i+=3**o
