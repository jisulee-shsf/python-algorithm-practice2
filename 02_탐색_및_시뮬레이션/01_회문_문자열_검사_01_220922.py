# 입력된 n개의 문자열 중, 회문 문자열이 맞으면 YES / 아니면 NO 출력하기
# 대소문자는 구분하지 않음

# Input :
# 5
# level
# moon
# abcba
# soon
# gooG

# Output :
# #1 YES
# #2 NO
# #3 YES
# #4 NO
# #5 YES

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    for j in range(len(s)//2):
        if s[j] != s[-1-j]:
            print(f'#{i+1} NO')
            break
    else:
        print(f'#{i+1} YES')