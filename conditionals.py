a=int(input("Enter your age: "))
if(a>18):
    print("you are 18+.")
    print("good for you")
elif(a<0):
    print("you are entering neg age.")    
elif(a==0):
    print("You are entering 0 which is not valid")

else:
    print("You are not allowed , baby")    

print("End of program") 




#practice1
a1=int(input("Enter num1:"))
a2=int(input("Enter num2:"))
a3=int(input("Enter num3:"))
a4=int(input("Enter num4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("The greatest num is a1:",a1)
elif(a2>a3 and a2>a4 and a2>a1):
    print("Greatest number is a2:",a2)
elif(a3>a4 and a3>a2 and a3>a1):
    print("Greatest number is a3:",a3)
elif(a4>a3 and a4>a2 and a4>a1):
    print("Greatest number is a4:",a4)



# practice2
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

messege=input("Enter your comment:")
if((p1 in messege)or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("This comment is a spam")
else:
    print("this comment is not a spam")    

     
    
