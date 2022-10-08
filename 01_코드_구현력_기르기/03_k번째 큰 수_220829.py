# 1부터 100 사이 자연수 카드 n장 중, 3장을 뽑은 합이 k번째로 큰 수 출력하기
# 숫자의 합이 중복될 경우, 포함하지 않음 > e.g. 25 25 23 23 22 20 ・・・ k가 3일 경우, 답은 22로 출력

# Input :
# 10 3
# 13 15 34 23 45 65 33 11 26 42

# Output :
# 143

n, k = map(int, input().split())
nums = list(map(int, input().split()))

ret = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            ret.add(nums[i] + nums[j] + nums[m])

ret = list(ret)
ret.sort(reverse = True)
print(ret[k - 1])
