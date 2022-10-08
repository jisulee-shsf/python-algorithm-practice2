# 입력된 문자열 중, 숫자만 추출하여 그 자연수의 숫자대로 약수의 개수 출력하기
# 첫 자리 0은 고려하지 않음

# Input :
# g0en2Ts8eSoft

# Output :
# 28
# 6

s = input()

res = 0
for i in s:
    if i.isdigit():
        res = res * 10 + int(i)
print(res)
cnt = 0
for j in range(1, res + 1):
    if res % j == 0:
        cnt += 1
print(cnt)