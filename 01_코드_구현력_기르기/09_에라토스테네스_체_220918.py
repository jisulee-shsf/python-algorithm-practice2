# 입력된 자연수 n의 1부터 n까지 소수 개수 출력하기
# 20의 경우, '2, 3, 5, 7, 11, 13, 17, 19' 소수 총 8개 확인

# Input :
# 20

# Output :
# 8

n = int(input())
cnt_list = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if cnt_list[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            cnt_list[j] = 1

print(cnt)
