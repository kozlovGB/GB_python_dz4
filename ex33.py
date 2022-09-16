import random
polinom="" 
k=int(input('задайте натуральную степень: '))
a=[random.randint(0,100) for _ in range(k)]#список значений множителей
b=[random.randint(0,1) for _ in range(k)]# определяем существует ли элемент x степени соответствующей его месту в списке или нет.
a[-1]=random.randint(1,100)
print("a=",a)
print('b=',b)
for i in range(k-1,-1,-1):
    if (a[i]!=0 and b[i]!=0):
        print('a=',a[i],"b=",b[i])
        if a[i]==1:
            if i==0:
                polinom+="x"+"+"
            else:
                polinom+="x"+"^"+str(i+1)+"+"
        else:
            if i==0:
                polinom+=str(a[i])+"*x"+"+"#так как значение коэффициентов многочлена по условию больше 0 ограничеваемся +
            else:
 
               polinom+=str(a[i])+"*x"+"^"+str(i+1)+"+"#так как значение коэффициентов многочлена по условию больше 0 ограничеваемся +
f=random.randint(0,1)#определяем будет ли у нас константа
if f!=0:
    print(polinom+str(random.randint(0,100)))
else:
    print(polinom[:-1])