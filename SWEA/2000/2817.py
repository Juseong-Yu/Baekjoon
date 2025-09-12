T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * (N)
    arr.sort()
    result = []

    def comb(cnt, tmp_arr, i):
        if cnt == K:
            result.append(tuple(tmp_arr))

        for idx in range(i + 1, N):
            if visited[idx] == False:
                visited[idx] = True
                next_arr = tmp_arr + [arr[idx]]
                comb(cnt + arr[idx], next_arr, idx)
                visited[idx] = False

    comb(0, [], -1)
    print(result)
    print(f'#{t} {len(result)}')