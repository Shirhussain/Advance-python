#Decorator Method 1
#Decorator means adding some new functionality to an existing funtion withoud modifying that function 

def OuterFunction(func):
    def WrapperFunction():
        print("This is some new functionality")
        return func()
    return WrapperFunction


def favPlayer():
    print("Missi")


#don't use '()' when you pass function as argument because we gonna call inside function
favorite = OuterFunction(favPlayer)
favorite()




#Decorator Method 2
#this is the shurtcut one, with @FunctionNameYouwannaDecorate e.g

#@OuterFunction == favorite=OuterFunction(favPlayer)



def OuterFunction(func):
    def WrapperFunction():
        print("This is new add shortcut one")
        return func()
    return WrapperFunction


@OuterFunction
def FavPlayer():
    print("Ronaldo")

FavPlayer()

#*********************************************************************************************

#if you wanna use *args, **kwargs

def OuterFunction(func):
    def WrapperFunction(*args, **kwargs):
        print("The name of my favorite player is ")
        return func(*args, **kwargs)
    return WrapperFunction


@OuterFunction
def favorite(country):
    print(f"Missi and my favorite footbal team is {country}")
favorite("Spain")


#********************************************************************************************
#decorator is avoid code dublication this time i gonna prove 
import time 

def evenNo(num):
    start = time.time()
    evenList=[]

    for x in range(0,num):
        if x%2 == 0:
            evenList.append(x)
    end = time.time()
    total = (end-start)*1000
    print("Even num took about " + str(total))


def oddNo(num):
    start = time.time()
    oddList = []

    for x in range(0,num):
        if x%2 != 0:
            oddList.append(x)
    end = time.time()
    total = (end- start)*1000 
    print("Odd numbers took about "+ str(total))

odd = oddNo(100000)
even = evenNo(100000)

#As i told that we use decorator to prevent code dublocation, if you gonna write a lot of code like this you would get a pain in the ass 
# recoammand you to use deocrators



def time_it(func):
    def WrapperFunction(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        total = (end- start)*1000
        print(func.__name__+" Took about "+str(total)+" milli seconds")
        return result
    return WrapperFunction

@time_it
def evenNumber(num):
    even_list = []

    for i in range(0,num):
        if i%2 ==0:
            even_list.append(i)

    return even_list


@time_it
def oddNumber(num):
    odd_list = []

    for i in range(0,num):
        if i%2 ==0:
            odd_list.append(i)

    return odd_list



even = evenNumber(100000)
odd = oddNumber(100000)
