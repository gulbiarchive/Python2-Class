def add_mul(choice, *args):
    if choice == "add": # 'add' 입력받았을 때
        result = 0
        for i in args:
            result = result + i # *args에 모든 값 더한다.
    elif choice == "mul": # 'mul' 입력받았을 때
        result = 1
        for i in args:
            result = result * i # *args에 입력받은 모든 값 곱한다.
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result) # 15

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result) # 120


