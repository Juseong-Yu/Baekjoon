N, M = map(int, input().split())

cnt = N
result = cnt
while True:
    Ms = cnt // M
    result += Ms
    if Ms >= M:
        cnt = Ms
    else:
        break

print(result)