from itertools import combinations

def solution(nums):
    answer = 0
    nlist = list(combinations(nums, 3))
    sumlist = []
    nonelist = []
    
    for i in range(0,len(nlist)):
        sumlist.append(sum(list(nlist[i])))
        
    ##소수 개수
    for n in sumlist:
        for i in range(2,n):
            if n%i==0:
                #소수 아님
                nonelist.append(n)
                break
                
    return len(sumlist)-len(nonelist)
