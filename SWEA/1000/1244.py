T = int(input())
for t in range(1, T + 1):
    arr, N = input().split()
    N = int(N)
    arr = list(map(str, arr))
    loc = [i for i in range(N)]
    arr_length = len(arr)
    loc2 = [i for i in range(arr_length)]
    pick2 = []
    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            pick2.append([i, j])
    pick2_len = len(pick2)
    loc2 = [i for i in range(pick2_len)]
    paths = []
    max_money = 0
    visited = set()

    def perm(cnt, result):
        global max_money
        if (cnt, tuple(result)) in visited:
            return
        visited.add((cnt, tuple(result)))
        if cnt == N:
            money = ''.join(result)
            money = int(money)
            if money > max_money:
                max_money = money
            return

        for ele in loc2:
            next = pick2[ele]
            paths.append(pick2[ele])
            tmp_result = result.copy()
            tmp_result[next[0]], tmp_result[next[1]] = tmp_result[next[1]], tmp_result[next[0]]
            perm(cnt + 1, tmp_result)
            paths.pop()

    perm(0, arr)
    print(f'#{t} {max_money}')