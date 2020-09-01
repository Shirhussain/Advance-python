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



