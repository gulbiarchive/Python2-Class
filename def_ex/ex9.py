def add(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값 더함
    return result

result = add(1, 2, 3) # 함수 호출
print(result) # 6 출력

result = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result) # 55 출력


