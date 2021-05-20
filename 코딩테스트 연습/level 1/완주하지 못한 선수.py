def solution(participant, completion):
    answer = ''
    # 시간초과남...
    # for i in completion:
    #     participant.remove(i)
    # answer = participant[0]
    
    # 정렬 후에 해보는건?
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]: # 이름이 다르면 다른 이름을 출력
            return participant[i]
    return participant[-1] # 끝까지 이름이 같으면 마지막 이름을 출력
    # return answer