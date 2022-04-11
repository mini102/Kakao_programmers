def solution(s):
    answer = 0
    lib = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    string = ''
    for index,i in enumerate(s):
        string+=i
        #print(string)
        if string in lib:
            s = s.replace(string,lib.get(string))
            # s[index-len(string)+1] = lib.get(string)
            string = ''
        elif string in lib.values():
            string = ''
            
    answer = int(s)
    return answer
