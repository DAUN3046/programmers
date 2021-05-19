def solution(d, budget):
    # 작은 순서대로(오름차순) 정렬한뒤 예산에서 빼가면서 0보다 작아지면 멈춘다.
    answer = 0
    d1 = sorted(d) # 오름차순 정렬
    for i in d1:
        budget -= i
        answer += 1
        if budget < 0:
            answer -= 1
            break
    
    # 더하는 방법도 됨
    # money = 0
    # for i in d1:
    #     money += i
    #     answer += 1
    #     if money > budget:
    #         answer -= 1
    #         break
    #     if money == budget:
    #         break
    # return answer