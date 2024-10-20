variable=(1,2,3)

address=("London Road",10,"LN93 EU2",2,543)

print(address)
#unpacking
streetname,roadnumber,postcode,housenumber,distance= address

print(streetname,roadnumber,postcode,housenumber,distance)
      
mytuple = "Soham", "Dubey", 16

print(type(mytuple))
print(mytuple[0][4])

listtuple= ([7,8,9],'HI',(True,False,True))

print(listtuple[1:])

print(listtuple[:2])

print(listtuple[:])

list= [1,'HELLO',True]
print(list)

#Difference between tuple and list, Lists are mutable whereas tuples are immutable

list[1]='World'
print(list)
listtuple[1]='Welcome'


alien.pos = (800,800)
