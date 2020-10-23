#List Comprehensions and Readability 

symbols = '$¢£¥€¤'
code = []

for symbol in symbols:
    code.append(ord(symbol))

code = [ord(syembol) for syembol in syembols]
    
print(code)

#Listcomps No Longer Leak Their Variables
a = 'my precious'

data = [a for a in 'KLM']
print(a)


m = "KLM"
dummy = [ord(m) for m in m]
print(m)
print(dummy)


#Listcomps Versus map and filter
#Listcomps do everything the map and filter functions do 
symbols = '$¢£¥€¤'

beyond_ascii = [ord(m) for m in symbols if ord(m)>130]
print(beyond_ascii)

beyond_ascii = list(filter(lambda z: z>90, map(ord,symbols)))

print(beyond_ascii)



----------------------------- tuple and list----------------
#Cartesian Products

colors = ['white', 'green','black','yellow']
sizes  = ['S', 'M','L']


tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

# or we can do like this as well 

for color in colors:
    for size in sizes:
        print((color, size), end=",")
        
tshirts2 = [(color, size) for size in sizes for color in colors]
print(tshirts2)

======================Generator Expressions ===========

#Generator Expressions

import array
symbols = '$¢£¥€¤' 

tuple_ = tuple(ord(symbol) for symbol in symbols)

print(tuple_)

arr_ = array.array("I", (ord(symbol) for symbol in symbols))

print(arr_)


# Cartesian product in a generator expression 
colors = ['black','white']
sizes = ['S','M','L']

for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
    print(tshirt)


====================Tuples Are Not Just Immutable Lists=====================
    #Tuples as Records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

#Tuple Unpacking



d=divmod(30,7)
print(d)

t = (20,7)
print(divmod(*t))


import os
_,fileName  = os.path.split('/usr/lib/python3.8/os.py')
print(fileName)


==============Using * to grab excess item===========

a,b,*rest  = range(10)

print(a,b,rest)

n,m,*digar = range(5)
print(m,n,digar)

a,*rest, b = range(10)
print(a,rest,b)

*rest, a,b = range(5)
print(rest,b,a)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.')) 

fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0: 
        print(fmt.format(name, latitude, longitude))
        
    
#the output will be 
                |   lat.    |   long.  
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
Sao Paulo       |  -23.5478 |  -46.6358


================================= Named Tuples====================
#The collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name

from collections import namedtuple

City = namedtuple('City','name country population coordinate')
jpan = City('tokyo','jp',36.933,(35.33433,139.4534534))
print(jpan)
print(jpan.population)
print(jpan.coordinate)
print(jpan[0])

print(City._fields)

LatLong = namedtuple('LatLong','lat long')
kabul_data = ('Kabul','af',6.3,LatLong(34.345345,180.324243))
kabul = City._make(kabul_data)
print(kabul)
print(kabul._asdict)

for key, value in kabul._asdict().items():
    print(key+' : ', value)   
    


======================== Slicing ====================================

le = [10,20,30,40,50,60,70,80,90]

print(le[:2])
print(le[2:])

st=("shirhussain_danishyar")

#this one jump 2 unite every time
print(st[::3])

#making reverse
print(st[::-1])

#reverse jump one unite
print(st[::-2])

#this is teh sequance 
#seq[start:stop:step]

invoice = """
... 0.....6.................................40........52...55........ 
... 1909  Pimoroni PiBrella                     $17.50    3    $52.50 
... 1489  6mm Tactile Switch x20                 $4.95    2     $9.90 
... 1510  Panavise Jr. - PV-201                 $28.00    1    $28.00 
... 1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95 
... """
 
product_id = slice(0, 6)
description = slice(6,40)
unite_price = slice(40,52)
qunatinty = slice(52,55)
total_price = slice(55,None)

#print(invoice.split("\n")[2:])

items = invoice.split("\n")[2:]

for item in items:
    print(item[unite_price], item[description])





#Multidimensional Slicing and Ellipsis

li = list(range(10))
print(li)

li[3:5] = 40,30
print(li)

del li[5:7]
print(li)

#li[1:3]=100   if i use like this i will get an error 

li[1:3] = [100]
print(li)

#Using + and * with Sequences
print(li*5) # repeating five time 


#Building Lists of Lists


board =  [['_'] * 3 for i in range(3)] 
print(board)
board[1][2] = "100"
print(board)

#also we can write as follows
board = []
for i in range(3):
    row = ['_']*3
    board.append(row)

board[1][2]="x"
print(board)


#but here is another example wiche look the same but arn't 
# and dosn't behave the same way 
#The same row is appended three times to board
# but in above examples each iteration builes a new row and append to teh lest

new_board = [['_']*3]*3
new_board[1][2]="200"
print(new_board)

#the last example look like this 
row = ['_']*3 
new_board = []
for i in range(3):
    new_board.append(row)
new_board[1][2]="y"
print(new_board)


=========================================Augmented Assignment with Sequence=====================
li = (2,5,[15,30])
li[2] += [40,50]
print(li)


#Note
"""
Putting mutable items in tuples is not a good idea
Augmented assignment is not an atomic operation—we just saw it throwing an exception after doing part of its job. 
Inspecting Python bytecode is not too difficult, and is often helpful to see what is going on under the hood
"""

==================================Managing Ordered Sequences with bisect ====================

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

row_fmt = '{0:2d} @ {1:2d}      {2}{0:2d}'

def sample(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position*'  |'
        print(row_fmt.format(needle, position, offset))


if __name__=="__main__":
    if sys.argv[-1] =="left":
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('Sample: ',bisect_fn.__name__)
print('hystack ->', ' '.join('%2d' % n for n in HAYSTACK))

sample(bisect_fn)

#Inserting with bisect.insort

import bisect
import random

SIZE = 10
my_list=[]

random.seed(2000)
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)


==============================When a List Is Not the Answer========================

from array import array
from random import random
floats = array('d',(random() for i in range(10**4)))
print(floats[-1])

fw = open('floats.bin','wb')
floats.tofile(fw)
fw.close()
floats2 = array('d')

fo = open('floats.bin','rb')
floats2.fromfile(fo,10**4)
fo.close()
print(floats2[-1])

floats2 ==floats

"""
As you can see, array.tofile and array.fromfile are easy to use.
 A quick experiment show that it takes about 0.1s for array.fromfile to load 10 million double-precision floats from a binary file created with array.tofile. That is nearly 60 times faster than reading the numbers from a text file, which also involves parsing each line with the float built-in. Saving with array.tofile is about 7 times faster than writing one float per line in a text file. 
 In addition, the size of the binary file with 10 million doubles is 80,000,000 bytes (8 bytes per double, zero overhead), while the text file has 181,515,739 bytes, for the same data.
 Another fast and more flexible way of saving numeric data is the pickle module for object serialization. 
"""

=====================================Memory Views========================================

import array
nums = array.array('h',[-2,-1,0,1,2])
memv = memoryview(nums)
print(len(memv))

mem_oct = memv.cast('B')
print(mem_oct.tolist())
print(mem_oct[5])
print(nums)


# end of chapter two 
