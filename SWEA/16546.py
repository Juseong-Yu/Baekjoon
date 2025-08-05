T = int(input())

def runner(arr):
    if arr[0]+1 == arr[1] and arr[1] + 1 == arr[2]:
        return True
    else:
        return False

def triplet(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
    else:
        return False


for t in range(1, T + 1):
    arr = list(map(int, list(input().strip())))
    flag = 'false'
    
    for x in range(6):
        for y in range(x + 1, 6):
            for z in range(y + 1, 6):
                tmp_arr = {0, 1, 2, 3, 4, 5}
                tmp_arr = tmp_arr - {x, y, z}
                tmp_arr = list(tmp_arr)
                arr1 = [arr[x], arr[y], arr[z]]
                arr1.sort()
                tmp_arr.sort()
                if runner(arr1) or triplet(arr1):
                    arr2 = [arr[tmp_arr[0]], arr[tmp_arr[1]], arr[tmp_arr[2]]]
                    arr2.sort()
                    if runner(arr2) or triplet(arr2):
                        flag = 'true'
                        break
            if flag == 'true':
                break
        if flag == 'true':
            break

    print(f'#{t} {flag}')
    
                        
                    
#1 true
#2 false
#3 true
#4 true
#5 true
#6 true
#7 false
#8 true
#9 true
#10 false