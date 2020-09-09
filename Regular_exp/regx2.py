import re 

#match function 

patterns =r"Do" 

sequence = "Do what you love "


if re.match(patterns,sequence):
    print("match found")
else:
    print("match not found")




import re

sequence = "Do what you love "

x = re.match(r"Do what",sequence)

if x:
    print(x.group())
    print(x.group(0))
    #if i wanna add another one (1) it will not work
    #print(x.group(1)) for this porpose i will do as follows




import re
sequence = "Do what you love the most"
y = re.match(r'(Do) (what) (you love)', sequence)

if y:
    print(y.group())
    print(y.group(0))
    print(y.group(1))
    print(y.group(2))
    print(y.group(3))
    print(y.group(1,2,3))


import re

sequence = 'shir@gmail.com'

a = re.match(r'(shir)(@)(gmail.com)', sequence)

if a:
    print(a.group())
    print(a.group(1))
    print(a.group(2))
    print(a.group(3))
    print(a.group(1,2,3))


Specific characters:
    . = match every single character except new line character 
    \w = match any single character, digits or underscore 
    \W = match any character which is not lower case 
    \s = match single white sapce like 'space, tap and etc'
    \S = match match allthe thing wich is not included in \s
    \t = match thee tap 
    \n = match new line 
    \r = match return 
    \d = match dicimal digit from (0-9) 
    ^  = match the start of string 
    $  = match the end of string 
    [abc]= match 'a,b or c' 
    [a-zA-Z0-9] = match evrythig characters and digits 
    (0-9) = match digit from 0 to 9 
    \A = match only at start of the string, it work on more than one line a too
    \b = match only the start and the end of the word 
    \  = it is use for scaping 
    +  = overloaded --> it means that chick one more thing 
    *  = anything 
    ?  = check only for 0 or 1 specified character in sequence
    *?, +?,?? = *? match as match as posible from the start to end
    +* = as few character as posible will be matched 
    ?? = if we have 'abc' we it only match 'a' instead of 'abc'
    {x} = copy of previous regular expretion should be matched 
    {x,y} = atempting to match as many reptation as possible
    {x,y}? = attempting to match as few reptation as possible
    [] =  a set of character in a set--> it can listed indivitually
    '|' = it means 'OR' 
    (...) = this going to match what ever regular expretion is inside this prantses and it indicate the start and end of the group as well 
    (?...) = ? the first question mark determines what the meaning and for the syntax of the constract is job going to be very the same as previous 
    (?iLmsux) = this text are modifier of flags and are going to cover all of these regular expression
    (?:...) = it match is what ever regular expretion inside the parantesis but substring matched by the group can not be retrive after performing a match are refrenced later in the pattern 
    (?<=...) = it match if the current position string proceeded --> it is use for search funtion rather than match funtion 

    e.g:
        import re 
        a = re.search('(?<=abc)xyz','abcxyz')
        print(a.group(0))


        #it's recommanded to use search instead of match because it's not goging to work for match 
        b = re.match(r'(?<=abc)xyz','abcxyz')
        print(b.group(0))

    \number = match the contant of the group with the same number 
    (?P <name>...)
    (?P=name)
    (?#...)
    (?=...)
    (?!...) 





