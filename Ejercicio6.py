matriz=[1,2,3,4,5,6,7,8,9];
i=0;
pares=0;
impares=0;
for i in range (0,9):
    if i % 2 is 0:
        pares= pares +1
        continue
    else:
        impares =( impares + 1)
    continue
print ('numeros pares: ' + str(pares))
print('numeros impares: ' + str(impares))

