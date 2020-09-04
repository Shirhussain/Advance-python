# Threading 
# Thread vs process 
# what is process ---> The program under excution is called process 
# process run independent and dosn't share any memory ---> if you open chrome browser 10 time it is 10 process 


#Thread is a process which executed inside a process 
# a process may contain single or many threads 

# for example in ms word if you have open one time word it is a on process but you may have ( auto save, spelling check ) 


import threading

t = threading.current_thread().getName()

print(t)


#if you wanna check if this is the main thread
if threading.current_thread() == threading.main_thread():
    print("This is main Thread")
else:
    print("This is not main Thread")


# here you can set the thread a name 
t2 = threading.current_thread().name="Danishyar Thread"

print(t2)


#here we go with function 

def naturalNum():
    # this is part of funtion thread
    #print(threading.current_thread().getName())
    for i in range(0,11):
        print(i)



# make sure that you are not targeting natural number with () 
t = threading.Thread(target=naturalNum)

t.start()
# just thrad inside the function is the function thread but outside the funtion is like here you see it's main thread
print(threading.current_thread().getName())



#if you wanna target multipal function with one thread so do as follows

def targeted_functions():
    f1()
    f2()


def f1():
    print(threading.current_thread().getName(),"F1")
    print("This is the function 1 ")

def f2():
    print(threading.current_thread().getName(),"F2")
    print("This is the function 2 ")



t = threading.Thread(target=targeted_functions)
t.start()



#threading inside and outside of a function

def Natural():
    for i in range(20):
        if i%2 ==0:
            print(i)
    t = threading.current_thread().name = "Natural thread"
    print(2)

t2 = threading.current_thread().getName()
t = threading.Thread(target=Natural)
t.start()


# how can we create a thread by extending a thread class 


from threading import Thread
import threading


class MyClass(Thread):

    # i wanna over write 'run ' method 
    def run(self):
        print(threading.current_thread().getName())
        list = []
        for i in range(10,20):
            list.append(i)

    print(list)

obj = MyClass()
# as you can see here that if i use run method it show that we are runing run inside the MyClass
obj.run()
# if i run start function it will show that it's class the main thread.
obj.start()




# create a thread without extending a thread class 
import  threading
from threading import Thread


class MyThread(Thread):

    def naturalNum(self):
        print(threading.current_thread().getName())
        list = []
        for i in range(20,30):
            list.append(i)
        print(list)



obj = MyThread()
# here is the way that we can target a function without extending the thread class 
t1 = Thread(target=obj.naturalNum)
t1.start()

#if you wanna work with main thread you can do like this 
obj.naturalNum()


# multi threading--> with this you can do multi task in paralal
import  threading


def Number():
    print(threading.current_thread().getName(),"hass been started")

    for i in range(30,40):
        print(i)

    print(threading.current_thread().getName(),"has ended")


t1 = threading.Thread(target=Number)
t2 = threading.Thread(target=Number)
t1.start()
t2.start()








#sleep in threading speacially in multi threading
import threading
from time import sleep


def Num():
    print(threading.current_thread().getName(),"Hass been started")

    sleep(2)

    for i in range(40,50):
        print(i)

    print(threading.current_thread().getName(),"hass endded")


n1 = threading.Thread(target=Num)
n2 = threading.Thread(target=Num)
n1.start()
n2.start()










