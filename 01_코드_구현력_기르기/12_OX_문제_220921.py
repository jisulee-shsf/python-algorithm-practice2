# 맞거나 또는 틀린 두 가지 답을 가진 문제를 아래의 규칙으로 채점할 때, 총 점수 출력하기
# - 연속적으로 답을 맞히는 경우에 가산점을 주기 위함
# - 연속적으로 답을 맞히는 경우, k번째 문제는 k점으로 계산
# - 틀린 문제는 0점으로 계산하며, 틀린 후 맞춘 첫 번째 문제는 1점으로 계산

# Input :
# 10
# 1 0 1 1 1 0 0 1 1 0

# Output :
# 10

n = int(input())
scores = map(int, input().split())

sum = 0
cnt = 0

for i in scores:
    if i == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)
