T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]
    nodes = [None] * (V + 1)
    for _ in range(E):
        node1, node2 = map(int, input().split())
        edges[node1].append(node2)
        edges[node2].append(node1)
    flag = False
    try:
        while True:
            num = nodes.index(None)
            stack = [num]
            nodes[num] = True
            while stack:
                now = stack.pop()
                for next in edges[now]:
                    if nodes[next] == None:
                        nodes[next] = 1 - nodes[now]
                        stack.append(next)
                    else:
                        if nodes[next] != 1 - nodes[now]:
                            flag = True
                            break
                if flag == True:
                    break
    except:
        pass
    
    
    if flag == True:
        print('NO')
    else:
        print('YES')