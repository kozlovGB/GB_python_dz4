#Вычислить число c заданной точностью d
#при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
a=float(input('Введите число с большим колличеством знаков после точки: '))
d=float(input("Задайте точность: "))
len_d=len(str(d).split(".")[-1])
len_a=len(str(a).split(".")[-1])
if a%1==0:
    a=str(a)
    print('a=',a+(len_d-1)*'0')
    exit()
if len_a<len_d:
    a=str(round(a,len_d))
    print('a=',a+(len_d-len_a)*'0')
else:
    print("a=",round(a,len_d))

