import random
a=random.random() #it will pick random element
print(a)
a=random.uniform(1,10) #it will pick random element in 1 to 10
print(a)
a=random.randint(1,10) #it will pick random integer element in 1 to 10(inclusive)
print(a)
a=random.randrange(1,10) #it will pick random element in range(1,10)
print(a)
a=random.normalvariate(0,1) #it will pick random element with mean=0,sd=1
print(a)


#LIST RANDOM OPERTAION

mylist=list("akansdjdhd")
a=random.choice(mylist) #it will pick random element in a list
print(a)
a=random.sample(mylist,k=4) #it will pick random  multiple element in a list
print(a)
a=random.choices(mylist,k=4) #it will pick random  multiple element in a list without duplicate
print(a)
random.shuffle(mylist) #it will pick suffle element in random order
print(mylist)
