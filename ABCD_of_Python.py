print('''Aye, aye, aye, aye (ooh)
Ooh, ooh, ooh, ooh-ooh (ooh)
Aye, aye
Ooh, ooh, ooh, ooh-ooh''')
d=5<4
print(d)

# truth table of 'or'
e=True or False
print("True or False is ",True or False)
print("True or True is ",True or True)
print(" False or True is ",False or True)
print("False or False is ",False or False)
# truth table of 'and'
print("True and False is ",True and False)
print("True and True is ",True and True)
print(" False and True is ",False and True)
print("False and False is ",False and False)
# truth table of 'not'
print(not(False))

#typecasting
a="ANam"
t=type(a)
print(t)#<class 'str'>

b="123"
c=float(b)
f=type(c)
print(f)#<class 'float'>


# taking input
x=input("Enter num 1 : ")
y=input("Enter num 2 : ")

print("Number x is: " ,x)
print("Number y is: " ,y)
print("Sum is: " ,x+y)#1+2=12


w=int(input("Enter num 1 : "))
z=int(input("Enter num 2 : "))

print("Number w is: " ,w)
print("Number z is: " ,z)
print("Sum is: " ,w+z)#1+2=3


print("the square of w is:",w**2)
