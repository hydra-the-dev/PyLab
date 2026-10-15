from math import exp,sin,cos,sqrt,log
a = float(input("Введите переменную a: "))
b = float(input("Введите переменную b: "))
c = float(input("Введите переменную c: "))
x = float(input("Введите переменную x: "))
chislitel = exp(x*log(a))+(log(abs(b))+3.4*exp(a*x))
znamenatel = (sin(c)/cos(c))*(sin(c)/cos(c))*sqrt(abs(b))
# y = exp(x*log(a))+(log(abs(b))+3.4*exp(a*x))/(sin(c)/cos(c)*(sin(c)/cos(c))*sqrt(abs(b)))
y = chislitel/znamenatel
print('y = ',y)