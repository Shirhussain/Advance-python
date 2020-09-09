import re

sentance = "Success is when your business rurn itself thosands miles away"
x = re.compile(sentance)

y = x.match("Success is when your business rurn itself thosands miles away")

if y:
    print("matuch found")
else:
    print("Match not found")


#compile is good when you have a lot of sequence of string, but there is another way you can use as follows 



import re

sentance = "Success is when your business rurn itself thosands miles away"


a = re.match(sentance,"Success is when your business rurn itself thosands miles away")

if a:
    print("match found")
else:
    print("match not found")


import re

#if you wanna splite the words you can do buy '\W+' or "(\W+)"
z = re.split('\W+','Do what you love')
print(z)



import re

#find something in documment

a = re.findall(r'Do what','Do what you love')

print(a)



import re

#find iterable object in memory
a = re.finditer(r'always','There is always a way for success')
print(a)



import re

a = re.sub(r'love','like','Do what you love',count=0)

print(a)



import re

#subn is also like sub function but the diffranc is that it will return tuple
#when i put count=1 it means that only change one of them
a = re.subn(r'love','like','Do what you love love',count=1)

print(a)



import re
import string

#escape is going to scape everything execpt ascii_char and digits

pattern = string.ascii_letters

a = re.escape(pattern)
print(a)

pattern = string.digits
b = re.escape(pattern)

print(b)


pattern = "~!@#$%^&*-+"

c = re.escape(pattern)
print(c)

# as you can see that it will escape like this \~!@\#\$%\^\&\*\-\+


import re


# the line bellow i didn't close by default if i gonna find the error it's very hard 
# but with 're.error' function i could easly find the error
pattern = r'(\W+ i love you so much'

x = re.match(pattern,'love')

if x:
    print("This is awsome")
else:
    re.error("this is not Awsome")


