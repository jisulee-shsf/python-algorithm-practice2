# 테스트 수(times)에 맞춰, n개의 숫자 중 s번째부터 e번째까지 수를 오름차순으로 정렬했을 때 k번째 숫자 출력하기
# Output은 '#(테스트 수) (k번째 수)' 형식으로 출력

# Input :
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

# Output :
# #1 7
# #2 6

times = int(input())
for t in range(times):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_sorted = sorted(nums[s - 1 : e])
    print(f'#{t + 1} {nums_sorted[k - 1]}')
