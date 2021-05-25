def solution(n):
    answer = 0
    n3 = []
    while n > 0:
        n3.append(n % 3)
        n = n // 3
    print(n3)
    length = len(n3)
    for i in range(length):
        answer +=  n3[i] * (3 ** (length - 1 - i))
    return answer