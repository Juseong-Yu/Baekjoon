T = int(input())

def check(player):
    player.sort()
    triplet_check = 1
    run_check = 1
    triplet_before = -1
    run_before = -1
    for card in player:
        if triplet_before == card:
            triplet_check += 1
        else:
            triplet_check = 1
            if run_before + 1 == card:
                run_check += 1
            else:
                run_check = 1
            run_before = card
        triplet_before = card
        

        if triplet_check == 3 or run_check == 3:
            # print(player)
            return True

    return False

for t in range (1, T + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for idx, card in enumerate(cards):
        if idx % 2 == 0:
            player1.append(card)
        elif idx % 2 == 1:
            player2.append(card)
    
    for i in range(2, 6):
        player1_result = check(player1[:i + 1])
        player2_result = check(player2[:i + 1])

        if player1_result == True:
            print(f'#{t} 1')
            break
        elif player2_result == True:
            print(f'#{t} 2')
            break

    else:
        print(f'#{t} 0')