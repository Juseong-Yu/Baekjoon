N,M,B = map(int,input().split())

arr = []
for i in range(N):
  level = list(map(int,input().split()))
  arr.append(level)
new_arr = [0] * (256 + 1)
for i in range(N):
  for j in range(M):
    new_arr[arr[i][j]] += 1

result_time = float("inf")
result_level = 0
for try_level in range(0,257):
  block = B
  time = 0
  for p in range(len(new_arr)):
    if p > try_level:
      time += 2 * (new_arr[p] * (p - try_level))
      block += (new_arr[p] * (p - try_level))
    elif p < try_level:
      time += (new_arr[p] * (try_level - p))
      block -= (new_arr[p] * (try_level - p))
  if block >= 0 and time <= result_time:
    result_time = time
    result_level = try_level
print(result_time, result_level)