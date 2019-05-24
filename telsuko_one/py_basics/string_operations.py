# The following module is by default imported
import builtins

msg = "Hellow raviKiran\tgoru how are you "

#print(dir(msg))
print("Type: ", type(msg))
print("Len:", len(msg))
print("Default split by whitespace", msg.split())

print("Find:", msg.find('how'))
print("Upper:",msg.upper())
print("Capitalize:", msg.capitalize())
print("Lower:", msg.lower())
print("Format:", "Hi {}, will you marry {}".format("ravi","ravali"))

sep = "-"
print("Join:",sep.join(["ravi","kavi","navi"]))
print("Index of word:", msg.index('how',0,len(msg)))
print("Count of word:",msg.count("h",0,len(msg)))
print("Casefold", msg.casefold())
print("Center:",msg.center(50,"*"))

name = "Hellöwö Ravi!"
print("Unicode String by default :", name)
print("Encoded name:", name.encode())
print("Encoded name ascii:", name.encode("ascii","ignore"))
print("Encoded name ascii:", name.encode("ascii","replace"))

print("Endwith a word",msg.endswith("Ravi!"))
print("Expand tab spaces by int :",msg.expandtabs(50))
msg.expandtabs(8)
print("isalnum alpha numeric string:",msg.isalnum())
print("isalpha alphabetic:",msg.isalpha())
print("Is decimal Hi:","Hi".isdecimal())
print("Is decimal 3:","3".isdecimal())
print("Is decimal 3.8: ","3.8".isdecimal())
print("Is digit 3.5: ","3.5".isdigit())
print("Is digit 5: ","5".isdigit())
print(msg.isidentifier())
print("is lower  hi: ","hi".islower())
print("Is numeric 45.6:","45.6".isnumeric())
print("Is numeric 45:","45".isnumeric())
print("Is printable Hi Dude:", "Hi Dude".isprintable())
print("Is printable Hi:","Hi".isprintable())
print("id space :\t \t:","\t \t".isspace())
print("id space :\ta\t:","\ta\t".isspace())
print("is title Hi all","Hi all".istitle())
print("is title Hi All","Hi All".istitle())
print("Is upper","HA".isupper())
print("lJust","Hi All".ljust(10))
print("rJust","Hi All".rjust(10))
msg = " Hi "
print("**",msg.lstrip(),"**",sep="")
print("**",msg.rstrip(),"**",sep="")
msg = " Hi "


print("Swapcase :",msg.swapcase())
print("Strip :",msg.strip())
print("Reverse ",msg[::-1])

print(msg)
print(msg)
print(msg)
print(msg)


print("", msg[2:len(msg):2])
