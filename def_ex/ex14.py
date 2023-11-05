def myself(name, old, man = True):
    print('나의 이름은 %s입니다.' %name)
    print('나의 나이는 %d살입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
        
myself('Tom', 27)
# 나의 이름은 Tom입니다.
# 나의 나이는 27살입니다.
# 남자입니다.

myself('Tom', 27, True)




