def myself(name, old, man = False):
    print('나의 이름은 %s입니다.' %name)
    print('나의 나이는 %d살입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
        
myself('Amy', 27)
# 나의 이름은 Amy입니다.
# 나의 나이는 27살입니다.
# 여자입니다.

myself('Amy', 27, False)




