def solution(n, arr1, arr2):
    # arr1, arr2를 이진법 변환하여 합쳐서 출력하는 문제. #은 벽이다.
    answer = []
    list1 = [] # 이진법 변환에 쓰일 리스트1
    list2 = [] # 이진법 변환에 쓰일 리스트2
    list3 = [] # 이진법 변환 전, 두 리스트를 합친 리스트
    str1 = ""
    
    
    for i in range(n):
        while True:
            # print("arr1:", arr1)
            # print("arr2:", arr2)
            if arr1[i] == 0 and arr2[i] == 0:
                break
            list1.append(arr1[i] % 2)
            arr1[i] = arr1[i] // 2
            list2.append(arr2[i] % 2)
            arr2[i] = arr2[i] // 2
        if len(list1) < n: # 길이 맞춰주기
            for j in range(n - len(list1)):
                list1.append(0)
        if len(list2) < n:
            for j in range(n - len(list2)):
                list2.append(0)
        # 두 리스트를 합쳐준다.
        list3 = [0] * n
        for j in range(n):
            list3[j] = list1[j] + list2[j]
        # print("list1:", list1)
        # print("list2:", list2)
        # print("list3:", list3)
        
        # 이진법이므로 리스트를 뒤집어준다.
        list3.reverse()
        print(list3)
        
        # 0, 1을 #, 공백으로 변환
        for j in list3:
            if j == 0:
                str1 += " "
            else:
                str1 += "#"
        answer.append(str1)
        
        # 변수 초기화
        list1 = []
        list2 = []
        str1 = ""
            
            
        
    return answer