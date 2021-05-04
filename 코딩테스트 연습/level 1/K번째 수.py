def solution(array, commands):
    answer = []
    newArray = []
    newArray2 = []
    idx = 0
    for row in range(len(commands)):
        newArray = array[commands[row][0] - 1:commands[row][1]]
        print("newArray:",newArray)
        newArray2 = sorted(newArray)
        print("newArray2:", newArray2)
        idx = commands[row][2]
        print("idx:", idx)
        print("newArray2[idx]:", newArray2[idx - 1])
        answer.append(newArray2[idx - 1])
        print(answer)
    return answer