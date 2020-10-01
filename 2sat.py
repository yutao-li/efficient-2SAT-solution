for i in range(1, 7):
    with open('2sat' + str(i) + '.txt') as f:
        n = int(f.readline())
        adj = [[] for _ in range(2 * n)]
        for line in f:
            a, b = map(int, line.split())
            if a > 0:
                if b > 0:
                    adj[2 * a - 2].append(2 * b - 1)
                    adj[2 * b - 2].append(2 * a - 1)
                else:
                    b = -b
                    adj[2 * a - 2].append(2 * b - 2)
                    adj[2 * b - 1].append(2 * a - 1)
            else:
                a = -a
                if b > 0:
                    adj[2 * a - 1].append(2 * b - 1)
                    adj[2 * b - 2].append(2 * a - 2)
                else:
                    b = -b
                    adj[2 * a - 1].append(2 * b - 2)
                    adj[2 * b - 1].append(2 * a - 2)
    disc = [0] * 2 * n
    scc = [0] * n
    c = 0
    stacked = [False] * 2 * n


    def dfs(timer, node):
        global c
        timer += 1
        cur = disc[node] = timer
        stack.append(node)
        stacked[node] = True
        for v in adj[node]:
            if not disc[v]:
                if not dfs(timer, v):
                    return False
                cur = min(disc[v], cur)
            elif stacked[v]:
                cur = min(disc[v], cur)
        if disc[node] == cur:
            c += 1
            t = -1
            while t != node:
                t = stack.pop()
                stacked[t] = False
                t1 = t // 2
                if not scc[t1]:
                    scc[t1] = c
                elif scc[t1] == c:
                    return False
        disc[node] = cur
        return True


    for i in range(2 * n):
        if not disc[i]:
            stack = []
            if not dfs(0, i):
                print(0)
                break
    else:
        print(1)
