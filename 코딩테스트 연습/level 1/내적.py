def solution(a, b):
    answer = 0
    length = len(a) # 배열의 길이
    for i in range(length):
        answer += a[i] * b[i] 
    return answer