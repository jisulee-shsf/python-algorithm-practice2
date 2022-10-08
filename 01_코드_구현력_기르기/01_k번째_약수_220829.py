# 두 개의 자연수 n과 k가 주어졌을 때, n의 약수 중 k번째로 작은 수 출력하기
# n의 약수가 k보다 작아 k번째 약수가 없을 경우, -1 출력

# Input :
# 6 3

# Output :
# 3

n, k = map(int, input().split())

cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
