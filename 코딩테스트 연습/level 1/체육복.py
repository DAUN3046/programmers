def solution(n, lost, reserve):
    answer = 0 
    # 시간 초과된다. 66.7점
    clothes = [1] * (n + 2) # 각 번호 학생들의 체육복 개수를 담은 리스트. 기본으로 1개씩 다 들고 왔다고 가정한 상태에서 시작. 번호와 인덱스를 맞추기 위해 n + 1 칸 생성.
    clothes[0], clothes[-1] = -999, -999 # 0번과 마지막 번 학생은 존재하지 않음 <-- 이 부분 중요!
    
    for i in reserve:
        clothes[i] += 1
    for i in lost:
        clothes[i] -= 1
        
    for i in range(1, n + 1):
        if clothes[i] == 0:
            if clothes[i + 1] == 2: # 옷 없는 학생의 앞뒤번호에 여벌 체육복 있는 학생이 있으면 빌려주는 작업
                clothes[i], clothes[i + 1] = 1, 1
            elif clothes[i - 1] == 2:
                clothes[i - 1], clothes[i] = 1, 1
        if clothes[i] >= 1: # 옷 한 벌 이상 가진 학생들을 카운트
            answer += 1
            
    return answer