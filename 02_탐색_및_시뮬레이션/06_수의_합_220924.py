# n개의 수로 된 수열 a에서, 연속적인 부분 수열의 합이 m이 되는 경우의 수 출력하기

n, m = map(int, input().split())
a = list(map(int, input().split()))

tot = a[0]
lt = 0
rt = 1
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)