# complex(-)
print('complex(10)', complex(10))
print('complex(0b111)', complex(0b111))
print('complex(0o231)', complex(0o231))
print('complex(0xbeef)', complex(0xbeef))
print('complex(1.5)', complex(1.5))
print('complex(True)', complex(True))
print('complex(False)', complex(False))
# str value should be int/float in decimal form
print("complex('10')", complex('10'))
print("complex('10.5')", complex('10.5'))


#  complex(-,-)
print('complex(10,20)', complex(10,20))
print('complex(0b111,20)', complex(0b111,20))
print('complex(0o231,30)', complex(0o231,30))
print('complex(0xbeef,40)', complex(0xbeef,40))
print('complex(0b111,0b111)', complex(0b111,0b111))
print('complex(0o231,0o231)', complex(0o231,0o231))
print('complex(0b111,0xbeef)', complex(0b111,0xbeef))
print('complex(1.5,1.6)', complex(1.5,1.6))
print('complex(True,False)', complex(True,False))
print('complex(False,True)', complex(False,True))
# str value should be int/float in decimal form
print("complex('10.5')", complex('10'))
print("complex('10.5')", complex('10.5'))

# if real part is string then img part should not be str: TypeError: complex() can't take second arg if first is a string
# if real part is string then img part is not allowed
print("complex('10', '20') TypeError",)
print("complex('10', 20) TypeError")

