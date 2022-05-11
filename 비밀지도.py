def solution(n, arr1, arr2):
    answer = ['' for i in range(n)]
    
    firstMap = []#[[0]*n for i in range(n)]
    secondMap = []#[[0]*n for i in range(n)]
    
    for i in arr1:
        if len(bin(i)[2:])<n:
            row = bin(i)[2:]
            for r in range(0,n-len(bin(i)[2:])):
                row = '0'+row
            firstMap.append(row)
            continue
        firstMap.append(bin(i)[2:])
    #print(firstMap)    
    for i in arr2:
        if len(bin(i)[2:])<n:
            row = bin(i)[2:]
            for r in range(0,n-len(bin(i)[2:])):
                row = '0'+row
            secondMap.append(row)
            continue
        secondMap.append(bin(i)[2:])
    # print(firstMap)  
    # print(secondMap)
    
    for i in range(n):
        for j in range(n):
            if int(firstMap[i][j]) + int(secondMap[i][j]) >= 1:
                answer[i] += '#'
            else:
                answer[i] += ' '
    
    return answer
