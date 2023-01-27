count=int(input("Enter the number of terms:"))
a=0
b=1
if count<0:
          print("Enter a valid count")
elif count==0:
    print(a)
else:
    for i in range(0,count+1):
        print(a)
        c=a+b
        a=b
        b=c

    
    
