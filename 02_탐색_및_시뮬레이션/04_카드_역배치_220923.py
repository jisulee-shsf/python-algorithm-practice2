# 20개의 카드 숫자를 입력된 구간에 맞춰 역배치해 출력하기
# 카드 숫자는 오름차순이며, 입력 구간은 10개로 고정되어 있음
# e.g. 카드 숫자(1 2 3 4 5) → 입력 구간(2 4) → 역배치 출력(1 '4 3 2' 5)

# Input :
# 5 10
# 9 13
# 12
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

# Output :
# 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

n = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        n[s+i], n[e-i] = n[e-i], n[s+i]
n.pop(0)
for j in n:
    print(j, end=' ')