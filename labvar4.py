from math import cos,sin,sqrt
x = float(input('Введите х: '))
a = 2.8
b = -0.3
c = 4
def xlessonetwo():
    result = a*x**2+b*x+c
    return result
def xeqonetwo():
    result2 = a/x+sqrt(x**2+1)
    return result2
def xgreatonetwo():
    result3 = (a+b*x)/(sqrt(x**2+1))
    return result3
if x < 1.2 :
    y = xlessonetwo()
    print('y= ',y)
elif x == 1.2:
    y = xeqonetwo()
    print('y= ',y)
else :
    y = xgreatonetwo()
    print("y = ", y)
z = 2*x*y-sin(x+3*y**2)
print("z = ",z)