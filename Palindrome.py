def chain (str1):
    n = str1[::-1]
    if list(n)== list(str1):
        print('Đây là chuỗi Palindrome!')
    else:
        print('Đây không phải là chuỗi Palindrome!')

str1 = (1,2,2,4,6,7,9,15)
chain (str1)

str1 = 'abcddcba'
chain (str1)