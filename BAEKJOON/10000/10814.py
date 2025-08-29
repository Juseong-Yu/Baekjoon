N = int(input())
book = []

for i in range(N):
    age, name = input().split()
    book.append([int(age),name])

result = sorted(book,key = lambda books: books[0])


for i in range(N):
    print(result[i][0],result[i][1])