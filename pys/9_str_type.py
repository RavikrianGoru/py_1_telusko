
# ignore escape chars
s = r'ravi\t\n'
print(s)

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

print(s1)
print(s2)
print(s3)
print(s4)

# To define doc string

print(type(s))