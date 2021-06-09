def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                hap = numbers[i] + numbers[j] # 두 수의 합
                if hap not in answer:
                    answer.append(hap)
    answer.sort()
    return answer