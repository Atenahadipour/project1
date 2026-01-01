x = float(input("Number1 :"))
y = float(input("Number2 :"))
z = float(input("operator :"))

if z=="+" :
    print(x+y)
elif z=="-" :
    print(x-y)
elif z=="%" :
    print(x/y)
elif z=="*" :
    print(x*y)
    if y!=0 :
      print(x/y)
    else:
        print("/0 is not exist")
else :
    print("operator is not exist")
