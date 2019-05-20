# Tuples are usually used in cases where a statement or a user-defined function can safely
# assume that the collection of values (i.e. the tuple of values used) will not change.

# I would recommend always using parentheses to indicate start and end of tuple even though parentheses are optional.

# Explicit is better than implicit.

# A list within a list does not lose its identity.
# a tuple within a tuple, or a tuple within a list, or a list within a tuple, etc.

t = 1,56,67,1,54,8 # () optional but recommended to use
print('tuple without () ', type(t), t)
t = ()
print('empty tuple :',t)

t = (1)# this us not tuple
t = (1,)
print(t)

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))
