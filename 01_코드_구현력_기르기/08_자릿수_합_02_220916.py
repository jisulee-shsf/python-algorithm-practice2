# 입력된 n개의 자연수 nums 중, 자릿수 합이 최대인 수 출력하기
# 자릿수의 합을 구하는 digit_sum 함수 작성 필요

# Input :
# 3
# 125 15232 97

# Output :
# 97

import sys

n = int(input())
nums = list(map(int, input().split()))

def digit_sum(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

max = -sys.maxsize
for num in nums:
    tot = digit_sum(num)
    if tot > max:
        max = tot
        res = num
print(res)
