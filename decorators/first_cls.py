#A function can be stored in a variable 

def favFood(k):
    return k

 # if i use '()' it means that i'm calling that funtion but if i don't use it means that it just show the refrence in memory 
 
a = favFood

print(a("Pasta"))
#here you can see that it only prent the memory location funtion
print(favFood)

print(favFood("Meet"))



def favSport():
    return "Football"


def favPlayer():
    return "Messi"



#if i wanna pass a funtion as an argument to another function
def favorite(func):
    print(func())


favorite(favSport)
favorite(favPlayer)




#function can return another funtion 

def favSport(a):
    def favPlayer(b):
        return a+", "+b 
    return favPlayer

#at the first place i don't have access to the inner funtion --> 'favPlayer()' but after i pass the first funtion --> 'favSport' an argument
#then it will return the favPlayer so it's time to call that one
favorite = favSport("Footbal")
print(favorite("Missi"))


