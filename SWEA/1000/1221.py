# 노가다 해결 코드, 카운트 정렬 비스무리한게 들어가 있음
T = int(input())
for t in range(1, T + 1):
    TC, N = input().split()
    N = int(N)
    words = list(input().split())
    num_arr = [0] * 10
    for word in words:
        if word == 'ZRO':
            num_arr[0] += 1
        elif word == 'ONE':
            num_arr[1] += 1
        elif word == 'TWO':
            num_arr[2] += 1
        elif word == 'THR':
            num_arr[3] += 1
        elif word == 'FOR':
            num_arr[4] += 1
        elif word == 'FIV':
            num_arr[5] += 1
        elif word == 'SIX':
            num_arr[6] += 1
        elif word == 'SVN':
            num_arr[7] += 1
        elif word == 'EGT':
            num_arr[8] += 1
        elif word == 'NIN':
            num_arr[9] += 1

    result = ['ZRO'] * num_arr[0] +  ['ONE'] * num_arr[1] +  ['TWO'] * num_arr[2] +  ['THR'] * num_arr[3] +  ['FOR'] * num_arr[4] +  ['FIV'] * num_arr[5] +  ['SIX'] * num_arr[6]  +  ['SVN'] * num_arr[7] +  ['EGT'] * num_arr[8] + ['NIN'] * num_arr[9]

    print(f'#{t}')
    print(' '.join(result))

# 딕셔너리를 활용한 간소화 코드
T = int(input())
for t in range(1, T + 1):
    TC, N = input().split()
    N = int(N)
    words = list(input().split())