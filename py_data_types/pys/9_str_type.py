s = 'ravi'
print(s[0],s[1],s[2],s[3])
print(s[-1],s[-2],s[-3],s[-4])

#s[4] or s[-5] ---> IndexError: string index out od range

# ignore escape chars
s = r'ravi\t\n'
print(s, type(s))

# str can be enclosed within '' "" No character data type in python.
s = 'ravi'
s = "ravi"
s = 'r'

# multi line str can be enclosed by """ or '''
s = """ravi
        kiran
            goru"""
s = '''ravi
        kiran
            goru'''
print(s)

# Combination of single and double quotes
s1 = "Ravi's 'girl friend' is beautiful"
s2 = 'Who is "Ravi"?'
s3 = "Ravi's \"Girlfriend\" is beautiful"
s4 = """Ravi's "Girlfriend" is beautiful"""

print(s4)

# To define doc string

