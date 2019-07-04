def số_cửa(n:int):
    for x in range (1, n+1):
        list = [0, 1]
        for z in range (0, 1):
            if x < n:
                if x % 2 == 0:
                    z = 1
                    print('mở', end = ' ')
                else:
                    z = 0
                    print('đóng', end = ' ')
            else:
                if n%2==0:
                    print('đóng')
                if n %2 != 0:
                    print('mở')

số_cửa(7)
