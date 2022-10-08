# 입력된 n개의 자연수 nums 중, 뒤집어 소수인 수를 찾아 나란히 출력하기
# 910 > 19와 같이, 첫 자리 0은 무시 / def reverse(x) & def isPrime(x) 함수 작성 필요

# Input :
# 5
# 32 55 62 3700 250

# Output :
# 23 73

n = int(input())
nums = list(map(int, input().split()))

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1): 
        if x % i == 0:
            return False
    else:
        return True

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10 
        res = res * 10 + t 
        x = x // 10 
    return res

for x in nums:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
