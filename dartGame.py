def solution(dartResult):
    scorelist = []
    cnt=0
    for index,element in enumerate(dartResult):
        #print(element)
        if element.isdigit():
            ## Score
            cnt+=1
            if cnt<2:
                if index<len(dartResult)-1 and dartResult[index+1]=='0':
                    scorelist.append(int(element+'0'))
                else:
                    scorelist.append(int(element))
            else:
                continue
        elif element.isalpha():
            ## Bonus
            cnt=0
            if element == 'D':
                scorelist[-1] = scorelist[-1]**2
            elif element == 'T':
                scorelist[-1] = scorelist[-1]**3
        else:
            ## Option
            cnt=0
            if element == '*':
                if len(scorelist)==1:
                    scorelist[-1]*=2
                else:
                    for i in range(1,3):
                        scorelist[-i]*=2
            elif element == '#':
                scorelist[-1] = scorelist[-1]*-1
    #print(scorelist)
    return sum(scorelist)
