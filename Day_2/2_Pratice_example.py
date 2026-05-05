age = int(input("enter age: "))
if(age<13):
    print("child")
elif(age>=13 and age<18):
    print("teenager")
else:
    print("adult")

username = input("enter username: ")
password = input("enter password")
if(username == "admin" and password == "pass"):
    print("Login Successfully")
elif(username!="admin"):
    print("wrong username")
else:
    print("wrong password")


n = int(input("enter num"))
if(n%5==0):
    print("multiple of 5")
else:
    print("not multiple of 5")