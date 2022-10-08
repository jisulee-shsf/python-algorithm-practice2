# 주사위 3개를 던져 아래의 규칙으로 상금을 받을 때, 가장 높은 상금 출력하기
# - 주사위 눈 3개가 같을 경우, 10,000원 + 같은 주사위 눈 * 1,000원
# - 주사위 눈 2개가 같을 경우, 1,000원 + 같은 주사위 눈 * 100원
# - 주사위 눈이 모두 다를 경우, 가장 큰 주사위 눈 * 100원

# Input :
# 3
# 3 3 6
# 2 2 2
# 6 2 5

# Output :
# 12000

import sys

n = int(input())
res = -sys.maxsize

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money
print(res)
