from collections import deque


n, m = map(int, input().split())

graph = list()

for i in range(n):
    graph.append(list(map(int,input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y): # 154
    count = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        print(queue)
        x, y = queue.popleft() # while문 기준 1회차 : 0, 0 -> if문 진입 후 1, 0 -> x, y = 1, 0

        print('x,y 값', x, y)
        print(queue)
        input('debug')

        for i in range(4):
            nx = x + dx[i] # for문 기준 1회차 -1 -> 2회차
            ny = y + dy[i] # 0, 0 -> 0

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 이전 경로가 nx, ny 보다 낮을 경우 다음 분기
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                print(nx, ny) # 1, 0
                input('if문 진입')
                graph[nx][ny] = graph[x][y] + 1 # 1 -> 1 + 1
                queue.append((nx, ny)) # append(1, 0)

    return graph[n -1][m - 1]

print(bfs(0, 0))

print(graph)