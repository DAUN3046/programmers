def solution(nums):
    answer = 0

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
            # 소수인지 아닌지 판별
                cnt = 0
                for l in range(2, sum):
                    if sum % l == 0:
                        cnt += 1
                if cnt == 0:
                    answer += 1
                cnt = 0
    return answer