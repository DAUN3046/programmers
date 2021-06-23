def solution(arr):
    answer = 0
    total = 0 # 합계
    for n in arr:
        total += n
    answer = total / len(arr)
    return answer