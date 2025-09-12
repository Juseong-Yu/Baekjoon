from pprint import pprint
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    max_result = -1
    # 맨 윗값 지정
    for y in range(N):
        for x in range(N):
            rd_ld_max = N - y - 1
            num = arr[y][x]
            
            # 가능한 값마다
            if rd_ld_max >= 2:
                # 오른쪽 아래, 왼쪽 아래의 횟수를 지정해준다. 올라오는것은 알아서 지정된다. 가능한 x 값도 조정한다.
                for rd_ld in range(2, rd_ld_max + 1):
                    for rd in range(1, rd_ld):
                        ld = rd_ld - rd
                        if 0 <= x + rd - ld - rd and x + rd < N:
                            # 구한 값으로 순회 하면서 중복되는 디저트가 없는지 확인한다.
                            num_set = list()
                            num_set.append(num)
                            #print(num_set)
                            tmp_y = y
                            tmp_x = x
                            flag = False
                            lu = rd
                            ru = ld
                            for _ in range(rd):
                                tmp_y += 1
                                tmp_x += 1
                                check = arr[tmp_y][tmp_x]
                                
                                if check in num_set:
                                    flag = True
                                    break
                                else:
                                    num_set.append(check)

                            if not flag:
                                for _ in range(ld):
                                    tmp_y += 1
                                    tmp_x -= 1
                                    check = arr[tmp_y][tmp_x]
                                    if check in num_set:
                                        flag = True
                                        break
                                    else:
                                        num_set.append(check)
                            
                            if not flag:
                                for _ in range(lu):
                                    tmp_y -= 1
                                    tmp_x -= 1
                                    check = arr[tmp_y][tmp_x]
                                    
                                    if check in num_set:
                                        flag = True
                                        break
                                    else:
                                        num_set.append(check)
                            
                            if not flag:
                                for _ in range(ru - 1):
                                    tmp_y -= 1
                                    tmp_x += 1
                                    check = arr[tmp_y][tmp_x]
                                    
                                    if check in num_set:
                                        flag = True
                                        break
                                    else:
                                        num_set.append(check)

                            if len(num_set) > max_result and flag == False:
                                max_result = len(num_set)

    print(f'#{t} {max_result}')