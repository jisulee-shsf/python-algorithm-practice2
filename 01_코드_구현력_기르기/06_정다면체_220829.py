# 두 개의 정 n면체와 정 m면체의 주사위를 던져 나올 수 있는 눈의 합 중, 가장 확률이 높은 합의 수 출력하기
# 수가 중복될 경우, 오름차순으로 출력

# Input :
# 4 6

# Output :
# 5 6 7

import sys

n, m = map(int, input().split())

cnt = [0] * (n + m + 1)
max_num = -sys.maxsize

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1
for i in range(len(cnt)):
    if cnt[i] > max_num:
        max_num = cnt[i]
for i in range(len(cnt)):
    if cnt[i] == max_num:
        print(i, end =' ')
