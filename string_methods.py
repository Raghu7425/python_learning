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
print(txt)
print("isascii: ",s)

#numeric type checks

s=txt.isdigit()
print("isdigit: ", s)

s = txt.isdecimal()
print("isdecimal: ",s)

s=txt.isnumeric()
print("numeric: ",s)

#case/structure checks

s= txt.islower()
print("islower: ",s)

s=txt.isupper()
print("isupper: ",s)

s=txt.isidentifier()
print("isidentifier: ",s)

s=txt.isprintable()
print("isprintable: ",s)

#positional findings
new_txt="     Raghu, Hi iam Raghunandan vaddi     "

s=new_txt.find("Raghu")
print("find: ",s)

s=new_txt.index("Raghu")
print("index: ",s)

#positional reverse findings 

s = new_txt.rfind("Raghu")
print("rfind: ",s)

s=new_txt.rindex("Raghu")
print("rindex: ",s)

#boundary findings
s=new_txt.startswith("Raghu")
print("startswidth: ",s)

s=new_txt.endswith("vaddi")
print("endswith: ",s)

s=new_txt.count("Raghu")
print("count: ",s)

#trimming and cleaning
s=new_txt.strip()
print("strip: ",s)

s=new_txt.lstrip()
print("left strip: ",s)

s=new_txt.rstrip()
print("right strip: ",s)

#padding and alignment
new_txt = "banana"
s=new_txt.center(20)
print("centre: ",s)

s=new_txt.rjust(20)
print("rjustify: ",s)

s=new_txt.ljust(20)
print("left justify",s)

s=new_txt.zfill(10)
print("zfill: ",s)

s=new_txt.expandtabs(2)
print("expandtabs:",s)

#splitting and joining
s = new_txt.split()
print("split: ",s)

s=new_txt.rsplit()
print("rsplit: ",s)

s=new_txt.splitlines()
print("split lines: ",s)

mylist = ("a","b","c")
x="#".join(mylist)
print("join: ",x)


new_txt="     Raghu, Hi iam Raghunandan vaddi     "

x=new_txt.partition("hi")
print("partition: ",x)

x=new_txt.rpartition("Raghu")
print("rpartition: ",x)

#replacement and translation


