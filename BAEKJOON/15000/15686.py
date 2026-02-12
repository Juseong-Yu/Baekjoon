N, M = map(int, input().split())
homes = []
chickens = []
dists = []
for i in range(N):
    line = list(map(int, input().split()))
    for j, ele in enumerate(line):
        if ele == 1:
            homes.append((i, j))
        elif ele == 2:
            chickens.append((i, j))

for home in homes:
    hi, hj = home
    dist = []
    for chicken in chickens:
        ci, cj = chicken
        dist.append(abs(ci-hi) + abs(cj-hj))
    dists.append(dist)

combinations = []
ch_l = len(chickens)
h_l = len(home)
h_ll = len(homes)
arr = [i for i in range(ch_l)]

def comb(start, path):
    if len(path) == M:
        append_path = path.copy()
        combinations.append(append_path)
    for i in range(start, ch_l):
        path.append(arr[i])
        comb(i + 1, path)
        path.pop()

comb(0, [])
result = 1000000000
for combination in combinations:
    min_result = 0
    for home_idx in range(h_ll):
        min_home = 1000000
        for chicken_idx in combination:
            if dists[home_idx][chicken_idx] < min_home:
                min_home = dists[home_idx][chicken_idx]
        min_result += min_home
    if min_result < result:
        result = min_result

print(result)