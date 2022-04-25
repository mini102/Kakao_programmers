def solution(record):
    answer = []
    dic = {}
    # userID는 동일한데, nickname이 다르게 들어왔을 경우 해당 userID의 nickname 변경
    for r in record:
        string = r.split(' ')
        if string[0] == "Enter":
                dic[string[1]] = string[2] #해당 user가 가져온 nickname 부여
                answer.append(string[1]+"님이 들어왔습니다.")
        if string[0] == "Leave":
                if string[1] in dic.keys(): #채팅방에 들어왔던 사람이 나가는 경우
                    answer.append(string[1]+"님이 나갔습니다.")
        if string[0] ==  "Change":
                    dic[string[1]] = string[2] #해당 user가 가져온 nickname 부여
    print(dic)
    print(answer)
    for d in dic.keys():
        for idx,s in enumerate(answer):
                answer[idx] = s.replace(d,dic.get(d))
    return answer
