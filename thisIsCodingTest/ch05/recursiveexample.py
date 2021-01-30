def recursive_function(i):
    if i == 10:
        return
    
    print(f"{i} 번째 재귀 함수에서 {i+1} 번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(f"{i} 번째 재귀 함수 호출을 종료합니다.")

recursive_function(1)