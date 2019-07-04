from time import time
def chap2mang(array1,array2):
    array3 = array1 + array2
    array3.sort(key = int, reverse = False)
    return(array3)

start = time()
for _ in range(100000):
    array1 = [1,3,5,7,9,11,15,18]
    array2 = [2,7,9,13,21,24,38]
    chap2mang(array1,array2)
delta = (time()-start)*1000000
print(f"{delta:6.0f} micro seconds")

from time import time


def gop2mang(array1, array2):
    array3 = array1 + array2
    n = sorted(array3)
    return(n)


start = time()
for _ in range(100000):
    array1 = [1, 3, 5, 7, 9, 11, 15, 18]
    array2 = [2, 7, 9, 13, 21, 24, 38]
    chap2mang(array1, array2)
delta = (time() - start) * 1000000
print(f"{delta:6.0f} micro seconds")