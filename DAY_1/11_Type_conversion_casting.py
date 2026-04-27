# int - float
#float - int
#int - bool

#implicit type conversion
a =10
b =5
print(a/5)
print(type(a/5))

#explicit type conversion user ya phir developer 
ans = int(5+100)
print(type(ans))

ans1 = int(5+10.0)
ans2 = 5+10.0
print(ans1 ,type(ans1))
print(ans2,type(ans2))


val = int("123")
print(type(val))

val = bool(10)
print(val,type(val))