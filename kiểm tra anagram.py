def kiểm_tra(str1, str2):
    if sorted(str1)==sorted(str2):
        print('2 chuỗi này là anagram của nhau')
    else:
        print('2 chuỗi này không phải là anagram của nhau')


kiểm_tra('Hello', 'eHlol')
kiểm_tra('Mello', 'eHlol')
kiểm_tra('Hello', 'eHcol')
kiểm_tra('Hello', 'fHlol')
