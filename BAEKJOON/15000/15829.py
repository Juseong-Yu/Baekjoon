L = int(input())
letters = input()
result = 0
for i in range(L):
    result += ((ord(letters[i])-96)*(31**i))

result = result % 1234567891
print(result)