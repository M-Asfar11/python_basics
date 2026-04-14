# slicing 

a = "hello world!"
print(a) # full string print 

print(a[0]) # we can call it by there index 
print(a[1])

# because string are array and we can also loop through there characters
for x in "banana":
    print(x)

# string length 
print(len(a))

# how to check certain elepment is present in the string annd it returns u with TRUE or FALSE 
txt = "we are venom!!"
print("venom" in txt)

print("hello " in txt) # returns false 

print("hello " not in txt) # returns true 

if "hello" not in txt:
    print("No, 'hello' is not present")

# Returns the range of characters 
b = "Hello, Everyone"
print(b[2:5]) # in this index 5 is excluded 

# slice from start 
print(b[:5])

# slice to the end 
print(b[2: ])

# negative indexing 
print(b[-5:-2])

# upper and lower
x = "Hello, worlD"
print(x.upper())
print(x.lower())

# replace string
string = "Muhammad Asfar"
print(string.replace("Muhammad", "M"))

# split string 
string2 = "Hello, asfar"
splitString = string2.split(",")
print(splitString)

age = 21
txt2 = f"My name is asfar, i am {age}"
print(txt2)