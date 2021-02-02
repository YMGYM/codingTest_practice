array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return # 원소가 1개인 경우 종료한다.
    
    pivot = start # 첫 번째 원소를 피봇으로 함
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈리면 작은 데이터와 피벗을 교체한다
            array[right], array[pivot] = array[pivot], array[right]

        else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array) - 1)
# print(array)

def quick_sort_pythonic(array):
    # 리스트가 하나 이하의 원소를 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 첫 번째 원소를 피봇으로 정함
    tail = array[1:] # 피봇을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분ㅋㅋㅋㅋㅋㅋㅋ 아니무슨
    right_side = [x for x in tail if x >= pivot]

    # 피봇을 기준으로 퀵정렬 수행 후 반환
    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)

print(quick_sort_pythonic(array))
