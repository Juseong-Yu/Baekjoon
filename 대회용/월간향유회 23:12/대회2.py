N = int(input())
#a = 0인 경우
result1 = (N * 2 + 1) *(N * 2 + 1)

# a != 0인경우
result2 = 0
for i in range(-N, N+1):
  if i != 0:
    b_c = -i+1
    if b_c > 0:
      result2 += N + N + i
    elif b_c == 0:
      result2 += N * 2 + 1
    else:
      maxb = b_c + N
      result2 += maxb + N + 1
print(result1 + result2)