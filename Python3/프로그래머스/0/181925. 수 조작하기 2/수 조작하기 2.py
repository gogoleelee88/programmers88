def solution(numLog):
   #W면 수에 1더하기
    #s면 수에 1빼기
    #d면 수에 10더하기
    #a면 수에 10빼기
    commands = []      
    for i in range(len(numLog) - 1):
        A = numLog[i+1] - numLog[i]    
        key = dict(zip([+1,-1,+10,-10],['w','s','d','a']))
        if A in key:  # A가 key에 있으면 출력
            commands.append(key[A])
    
    return ''.join(commands)