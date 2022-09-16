#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N=int(input('Задайте натуральное число N: '))
simple_multiplier=[1]
for i in range(1,N):
    if (N/i)%1==0:
        schet=0
        for j in range(1,i):
            if i%j==0:
                schet+=1
        if schet==1:
            simple_multiplier.append(i)
print(simple_multiplier)