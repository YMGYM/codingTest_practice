import sys
input = sys.stdin.readline # input을 더 빠르게 하는 함수

INF = int(1e9) # 무한을 의미하는 값으로 10억정도 지정

# n = 노드의 개수, m = 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 각 노드들이 연결되어 있는 정보를 담는 배열
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적
visited = [False] * (n+1)

# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b까지 가는 비용이 C
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n+1): # 전체를 순회하면서..
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]: # j에는 시작 노드에 대한 간선 정보들이 들어있음
        distance[j[0]] = j[1] # 시작 노드에서 각 노드들까지의 거리 설정(최초)

    # 시작 노드를 제외하고 전체 n-1 개 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: # j에는 시작 노드에 대한 간선 정보들이 들어있음
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 다른 노드를 이용하는게 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 알고리즘 수행
dijkstra(start)

# 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])

