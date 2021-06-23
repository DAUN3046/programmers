def solution(x):
    answer = True
    sum = 0 # 자릿수의 합
    xList = list(str(x)) # 계산용 변수
    
    for i in xList:
        sum += int(i)
    if x % sum != 0:
        answer = False
    
    return answer