w = int(input())
a = w % 10
b = ((w % 100) - a)/10
c = ((w % 1000) - a - b * 10)/100
d = ((w % 10000) - a - b * 10 - c * 100)/1000
e = (w - a - b * 10 - c * 100 - d * 1000)/10000
s = ((b**a)*c)/(e-d)  
print (s)