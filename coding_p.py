print("Hello World")
print("let's start")

#coding practice

x = 5
y = 6

if x<y:
    print("Hello baddie")

#This is single line comment

""" Here comes the multiline comment, 
it is string literal but it is not assigned to any variable"""

string_input = str(3)
int_input = int(3)
float_output = float(3)

print(string_input,type(string_input))
print(int_input, type(int_input))
print(float_output, type(float_output))


""" Assign multiple values to multiple variables """

a,b,c = 1,2,3
print(a,b,c)

""" unpacking variables """
alphs = [4,5,6]
a,b,c = alphs

print(a,b,c)

a=b=c=0
print(a,b,c)

""" working with global and local variables """

scope_var = "Hello_buddy"

def scopefun():
    scope_var = "Hello_local"
    print("this is local ", scope_var)

scopefun()

print("this is global scope ",scope_var)

"""scope can be modified inside function with global keyword"""

def func_scope():
    global z
    z = "inside function" 
    print(z)
func_scope()
print("outside but",z)


print(""" Data types """)
data_types =""" 
    text : string \n
    numeric : int , float, complex \n
    sequence : list, tuple , range \n
    mapping : dict \n
    set : set \n
    boolean : bool \n
    binary : bytes, bytearray, memoryview \n
    Nonetype : nonetype
    """

print(data_types)

# setting up data type

w = "Hello"
print(w, type(w))

w = 5
print(w, type(w))

w = 5j
print(w, type(w))

w = 5.2
print(w, type(w))

w = [1,2,3]
print(w, type(w))

w = (1,2,3)
print(w, type(w))

w = range(3)
print(w, type(w))

w = {"hello":1,"world":2}
print(w, type(w))

w = frozenset({1,2,3})
print(w, type(w))

w = {1,2,3}
print(w, type(w))

w = b"hello"
print(w,type(w))

w = bytes(5)
print(w, type(w))

w=bytearray(5)
print(w, type(w))

w = memoryview(bytes(5))
print(w, type(w))
w = True
print(w, type(w))

w = None
print(w, type(w))

