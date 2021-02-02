array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 2번부터 시작
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: # 원소를 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else: # 자기보다 작은 원소 앞에서 멈춤
            break


    
