#we can't do changes  in str but we can do it in list

friends=["Apple","Orange",5,345.45,False,"Aakash","Rohan"]
print(friends[0])
friends[0]="Grapes"
print(friends[0])
print(friends[0:4])

friends.append("Banana")#adds Banana at the end
friends.insert(3,777)#adds 777 at index 3
print(friends)

friends.pop(2)#deletes the element of index 2
print(friends)


l1=[2,22,12,3,54,5] 
l1.reverse()
print(l1)
l1.sort()#asc order
print(l1)


  