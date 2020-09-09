#match vs serach
#match is going to match only at the start of string but serach is anywher in string 

import  re

pattern = 'd'
sequence = 'abcdef'

k = re.match(pattern, sequence)
l = re.search(pattern, sequence)

print(l.group())
# as you can see here that it only display for search but not for match 
print(k.group())



#Greedy VS Non-Greedy function 
# greedy means that give you to the maximum and non-greedy meand give you to the minimum 


import re

pattern = "Do"
sequence = "Do what you love "

new_sequence = r'<h1>This is new header</h1>'

#at the first i gonna show you the Greedy one
a = re.match(r'<.*>', new_sequence).group()
print(a)

#this time let's see the none greedy one
b = re.match(r'<.*?>', new_sequence).group()
print(b)



#Modifiers or Flags

re.I --->is about case insenstive


import re

pattern = "do"

sequence = "Do what you love"

a = re.match(pattern, sequence,re.I)


if a:
    print("Match Found")
else:
    print("match not foun")



re.L  =

re.M = 
re.S=
re.U = 
re.X =  



import re

pattern = "Do \n what"
sequence = "Do \n what you love"

a =re.match(pattern, sequence, re.M)

if a:
    print("Match found")
else:
    print("match not found")



import re


passwords = [
        "shir@1234",
        "4543daishyar",
        "do 342309",
        "pytho343n",
        "3453rust",
        "!#@@!#$423",
        "########3",
        "jaldsfjalsf"
        ]


matching_squence = r'[0-9]'

for ps in passwords:
    r = re.search(matching_squence,ps)
    if r:
        print(ps +" is a valid password")
    else:
        print(ps + " is not a valid password")


