# N개에서 절반 뽑는 조합을 한후, 나머지와 비교한다.


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    foods = [i for i in range(N)]
    visited = [False] * N
    path = []
    min_diff = float('inf')
    def perm(idx, last):
        global min_diff
        if idx == N // 2:
            not_path = list(set(foods) - set(path))
            groupA = 0
            groupB = 0
            for i in range(idx):
                for j in range(i + 1, idx):
                    groupA += S[path[i]][path[j]] + S[path[j]][path[i]]
                    groupB += S[not_path[i]][not_path[j]] + S[not_path[j]][not_path[i]]

            diff = abs(groupA - groupB)
            if min_diff > diff:
                min_diff = diff
            return
        
        for food in foods[last + 1:]:
            if visited[food] == False:
                visited[food] = True
                path.append(food)
                perm(idx + 1, food)
                path.pop()
                visited[food] = False

    perm(0, -1)
    print(f'#{t} {min_diff}')