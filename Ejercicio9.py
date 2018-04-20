
num=0;

num=int(input("Ingrese el numero para sacar su factorial"))
j=num
if num is not 0:
    for i in range (1,num):
         j=(num-i)*j
    print(j)
else:
    print('1')
