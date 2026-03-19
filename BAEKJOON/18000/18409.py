N = int(input())
S = input()
cnt = 0
for ele in S:
    if ele in ['a', 'i', 'u', 'e', 'o']:
        cnt += 1

print(cnt)