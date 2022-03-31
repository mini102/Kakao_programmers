def solution(s):
    answer = 0
    nlist = []
    for i in range(1,len(s)):  #parsing 단위
        sl = list(s)
        sy = []
        num = 0 
        #### sl을 i에 따라 parsing #######
        k=0
        while k<len(s):
            sy.append(sl[k:k+i])
            k+=i
        for idx,st in enumerate(sy):
            if idx != len(sy)-1:
                if sy[idx] == sy[idx+1]: #연속으로 같을 경우
                    num += 1
                elif num!=0:
                    del sy[idx]
                    sy.insert(idx-num,list(str(num+1)))
                    num = 0
            elif sy[idx] == sy[idx-1] and num!=0:
                del sy[idx-num:idx]
                sy.insert(idx-num,list(str(num+1)))
        m = 0
        for f in sy:
            for si in f:
                m+=1
        nlist.append(m)
    answer = min(nlist)      
    return answer
