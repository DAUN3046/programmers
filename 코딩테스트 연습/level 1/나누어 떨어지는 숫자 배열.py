def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0: # 나누어 떨어지는 수를 배열에 추가
            answer.append(num)
    if len(answer) > 0: # 배열에 수가 있으면 정렬
        answer.sort()
    else: # 배열에 수가 없으면 -1 담음
        answer.append(-1)
    return answer