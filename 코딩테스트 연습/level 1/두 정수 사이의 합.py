def solution(a, b):
    if a > b: # a가 더 크면 순서를 바꿔준다.
        a, b = b, a
    answer = 0
    for num in range(a, b + 1):
        answer += num
    return answer