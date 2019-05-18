# int(-)
print('int(5)', int(5))
print('int(0b111)', int(0b111))
print('int(0o152)', int(0o152))
print('int(0xBEE4)', int(0xBEE4))
print('int(123.45)', int(123.45))
print("int('125')", int('125'))
print('int(True)', int(True))

print('int(10+20j) TypeError')
print("int('0b111') ValueError")
print("int('True') ValueError")
print("int('125.5') ValueError")

