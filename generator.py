#generator 
# generator is very close to function which run an iterable set of items, one at the time, in a special way.
# it's using for memory performance 
# in case of function we use 'return ' but in generator we use 'yield' 

# in function we use keyword 'return' once but in genrator we may use two or many more 
# genrator can genrate many value (infinite). yielding each one in it turns ---> '__next__()' to get the required result 


# if a function used a lest one time yield so that fuction become a generator the diffrence is that return terminate the function entirly and 
# the yield pause the function and later continue from there in success call

#function store all the result in memory while genrator is storing only when it's calld 

def zarb(n):
    result = n*5 
    return result
    #after you run this file you can see that you don't see the following line because function won't accept anything after result
    print("I love to code but i will not be executed ")

z = zarb(4)

print(z)


# the next time i will change the return to yield --> here we go 


def zarb(m):
    result = m*10 
    result1 = m*1
    result2 = m*2
    result3 = m*3 
    
    yield result3
    yield result2 
    yield result1
    yield result


z1 = zarb(5)
# remember that you shold call __next__() in generator as follows
print(z1.__next__())
print(z1.__next__())
print(z1.__next__())

#the next way to show a generator is like this
print(next(z1))



def natural_no(n):
    list = []
    for i in range(0,n):
        list.append(i)
    return list


n = natural_no(10)
print(n)

#the above function is working but we consume a lot of memory right now 
# instead i have to use genrator like this:

def natural_N(m):
    for i in range(0,m):
        yield i 


n1 = natural_N(10)
#print(next(n1)) it was the way but if i wana show all of them so i have to use for loop



print("\n\n\n\n\nforloop for genrator")
for i in n1:
    print(i)


# let's see in time which one is fast 

import time 
import memory_profiler as mem_profile 

print(f"Memory Usage before work: {mem_profile.memory_usage()}MB")

def List_of_Natural(n):
    list = []
    for i in range(0, n):
        list.append(i)
    return list 


t1 = time.time() 
list = List_of_Natural(1000000)
t2 = time.time()


print(f"The time after: {mem_profile.memory_usage()}MB")
print(f"Thie time between start and end of runing project", (t2- t1)*1000)


# so let se in genrator 
print(f"\n\n\n Memory Before genrator: {mem_profile.memory_usage()}")

def Natural_gen(n):
    for i in range(0,n):
        yield i 


t1 = time.time()
print(f"Memory After genrator: {mem_profile.memory_usage()}")
print("Total amout of taken time is ", (t2- t1)*1000)


# as you can see that it's huge differance thata genrator won't consume data like function














