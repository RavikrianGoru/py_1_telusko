# Pickle is python module.
# which you can use to store any plain Python object in a file and then get it back later.
# This is called storing the object persistently.

import pickle

employee_names = ['Ravi', 'Kiran', 'Chinna', 'Devi']
emp_data_file = 'employees.data'

print("Before  pickle.dump(--):", employee_names)
f = open(emp_data_file, 'wb')
# dump object in to file pickling lly serialization
pickle.dump(employee_names, f)
f.close()

del employee_names # destroy object

# Read back object from file unpickling lly de-serialization
f = open(emp_data_file, 'rb')
employee_names = pickle.load(f)
print("After pickle.load(-)", employee_names)
f.close()




