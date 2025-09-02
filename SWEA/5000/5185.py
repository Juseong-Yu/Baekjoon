# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, num = input().split()
    result = ""
    for ele in num:
        val = int(ele, 16)
        for i in range(3, -1, -1):
            bit = (val >> i) & 1
            result += str(bit)
    print(f'#{t} {result}')