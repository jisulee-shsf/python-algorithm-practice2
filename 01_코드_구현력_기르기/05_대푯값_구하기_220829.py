# n명 학생의 수학 점수가 주어질 때, 점수 평균과 가장 가까운 학생의 점수와 몇 번째 학생인지 출력하기
# 평균과 가까운 점수가 중복될 경우, 높은 점수 우선 / 높은 점수가 중복될 경우, 빠른 순서 학생이 우선

# Input :
# 10
# 45 73 66 87 92 67 75 79 75 80

# Output :
# 75 7

n = int(input())
scores = list(map(int, input().split()))

ave = round(sum(scores) / n)
min_score = float('inf')

for idx, score in enumerate(scores):
    tmp = abs(score - ave)
    if tmp < min_score:
        min_score = tmp
        ret_score = score
        ret_index = idx + 1
    elif tmp == min_score:
        if ret_score < score:
            ret_score = score
            ret_index = idx + 1

print(ret_score, ret_index)
