def solution(absolutes, signs):
    answer = 0
    print(signs)
    for i in range(len(absolutes)):
        if signs[i] is True:
            answer += absolutes[i]
            print(answer)
        else:
            answer -= absolutes[i]
            print(answer)
    return answer