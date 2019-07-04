import random
for x in range(1):
    n = random.randint(1, 101)
while n < 101:
#print("Please enter a number between 1 and 100: ")
    y = int(input("Hãy điền số từ 1 tới 100 đi em: "))
    if n > y:
        print("Số bé quá em ơi!")
    elif n < y:
        print ("Sao em điền số lớn thế!")
    else:
        #print("Your guess is correct!")
        break
if y == n:
    print ("Em đoán quá chuẩn!")
