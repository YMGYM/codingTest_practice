import sys
input = sys.stdin.readline
INF = inf(1e9)

# n = 노드의 개수, m = 간선의 개수
n,m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어있는 노드
graph = [[] for i in range(n+1)] # 각 노드에 대응하는 리스트 생성

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 각 노드까지 가는 최단경로
distance = [INF] * (n+1)
 
# 모든 간선정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b까지 가는 비용이 c
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF

    index = 0 # 가장 최단거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = 1
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1] # 연결된 간선이 있는지 확인 후..

    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


