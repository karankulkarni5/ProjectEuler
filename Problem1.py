a = 3
b = 5
c = 15
sum1 = 0
sum2 = 0
sum3 = 0
limit = 1000

while a<limit:
    if a>limit:
        break
    sum1=sum1+a
    a=a+3

while b<limit:
    if b>limit:
        break
    sum2=sum2+b
    b=b+5

while c<limit:
    if c>limit:
        break
    sum3=sum3+c
    c=c+15

print(sum1+sum2-sum3)
