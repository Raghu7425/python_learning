txt =""" string meThods """

print(txt)

#case and capitalization conversion

#capitalize
s = txt.capitalize()
print("capitalization: ", s)

#title
s=txt.title()
print("title(): ", s)

#lower
s=txt.lower()
print("lower: ",s)

#upper
s = txt.upper()
print("upper: ",s)

#casefold
s=txt.casefold()
print("casefold: ",s)

#swapcase

s=txt.swapcase()
print("swapcase: ",s)


#checks

txt = "Hello 123"

#charecter type checks
s=txt.isalnum()
print("isalnum: ",s)

s=txt.isalpha()
print("isalpha: ",s)

s = txt.isspace()
print("isspace: ",s)

s = txt.isascii()
print("isascii: ",s)

#numeric type checks

s=txt.isdigit()
print("isdigit: ", s)

s = txt.isdecimal()
print("isdecimal: ",s)

s=txt.isnumeric()
print("numeric: ",s)

#case checks

s= txt.islower()
print("islower: ",s)

s=txt.isupper()
print("isupper: ",s)

s=txt.isidentifier()
print("isidentifier: ",s)

s=txt.isprintable()
print("isprintable: ",s)