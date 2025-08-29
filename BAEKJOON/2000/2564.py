garo, sero = map(int, input().split())
n = int(input())
stores = []
for _ in range(n + 1):
    store = list(map(int, input().split()))
    if store[0] == 1:
        store = store[1]
    elif store[0] == 4:
        store = store[1] + garo
    elif store[0] == 2:
        store = garo + sero + garo - store[1]
    elif store[0] == 3:
        store = garo + sero + garo + sero - store[1]
    stores.append(store)
police = stores[-1]
stores = stores[:-1]
around = garo * 2 + sero * 2 

results = 0
for store in stores:
    if store > police:
        check1 = store - police
        check2 = police + (around - store)
    else:
        check1 = police - store
        check2 = store + (around - police)
    result = min(abs(check1), abs(check2))
    results += result
print(results)