# DS to store a collection of related data.

tour_plan = ['chennai', 'madurai', 'palani', 'madurai', 'kanyakumari']
print(tour_plan)
tour_plan.append('rameswaram')
print(tour_plan)
tour_plan.append('dhanushkoti')
tour_plan.append('chennai')
print(tour_plan)

tour_plan.remove('chennai')
print(tour_plan)
del tour_plan[0]
print(tour_plan)

tour_plan.sort()
print('Sorted:', tour_plan)
tour_plan.reverse()
print('Reversed:', tour_plan)

print('All halts :', end=" ")
for i in tour_plan:
    print(i, end="->")

