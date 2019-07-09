x = 1   #int
y = 2.5    #float
name = "Ana"   #str
is_cool = True    #bool

#Multiple definicion
x,y,name,is_cool=(1,2.5,"Ana",True)

#matematicas basicas
a =x + y

print(x,y,name,is_cool,a)

#chechar el tipo de x
print(type(x))

#cast e.g x to string
x = str(x) #passing x
y = int(y) #passing y
z = float(y)

print(type(y),y)
print(type(z),z)
