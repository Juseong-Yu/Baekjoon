T = int(input())
for t in range(1, T + 1):
    word = list(input())
    N = len(word)
    for idx in range(N // 2):
        if word[idx] != word[N - 1 - idx]:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')