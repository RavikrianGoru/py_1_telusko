# Dictionary associate keys (name) with values (details).
# Note that you can use only immutable objects (like strings) for the keys of a dictionary but
# you can use either immutable or mutable objects for the values of the dictionary.

# address book ab
ab ={'ravi':'ravi@gmail.com', 'kiran':'kiran@gmail.com','goru':'goru@gmail.com'}
print('dictionary of ab:', ab)
print(f"ab['ravi'] is ravi's address : {ab['ravi']}")

# remove ravi's contact
del ab['ravi']
print('dictionary of ab removed ravi\'s address :', ab)

print('Dictionary items as dict_items type: ', ab.items())
print('\nThere are {} contacts in the address-book'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# adding new contact
ab['guntur'] ='guntur@gmail.com'
print('dictionary of ab:', ab)

if 'kiran' in ab:
    print(f"kiran contact is available: {ab['kiran']}")
