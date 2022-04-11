def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],[4, 5, 6],[7, 8, 9],['*', 0, '#']]
    Ls = [[3,0]]
    Rs = [[3,2]]
    for n in numbers:
        for fi,k in enumerate(keypad): 
            if n in k:
                now = [fi,k.index(n)]
                if k.index(n) == 0:
                    Ls.append(now)
                    answer += 'L'
                elif k.index(n) == 2:
                    Rs.append(now)
                    answer += 'R'
                else:
                    LD = 0
                    RD = 0
                    #print("Ls: {}, Rs: {}, now: {}".format(Ls[-1], Rs[-1],now))
                    for a, b, c in zip(Ls[-1], Rs[-1],now):
                        LD += abs(a-c)
                        RD += abs(b-c)
                    
                    # 왼손이 더 가까운 경우
                    if LD < RD :
                        answer += 'L'
                        Ls.append(now)
                        
                    # 오른손이 더 가까운 경우
                    elif LD > RD:
                        answer += 'R'
                        Rs.append(now)
                    
                    # 두 거리가 같은 경우
                    else:
                        # 왼손잡이 경우
                        if hand == 'left':
                            answer += 'L'
                            Ls.append(now)
                            
                        # 오른손잡이 경우
                        else:
                            answer += 'R'
                            Rs.append(now)
            else: 
                continue    
                    
    return answer
