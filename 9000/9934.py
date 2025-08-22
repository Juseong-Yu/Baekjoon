K = int(input())
arr = list(map(int, input().split()))
N = len(arr)
tree = [0] * (N + 1)
cnt = 0
def inorder(i):
    global cnt
    if i > N:
        return
    
    inorder(i * 2)
    tree[i] = arr[cnt]
    cnt += 1
    inorder(i * 2 + 1)
inorder(1)
counts = 1
tree = tree[1:]
while True:
    if len(tree) <= counts:
        result = ' '.join(list(map(str, tree)))
        print(result)
        break
    else:
        result = tree[:counts]
        result = ' '.join(list(map(str, result)))
        tree = tree[counts:]
        counts *= 2
        print(result)