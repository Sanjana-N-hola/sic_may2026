people = [(1,'Theia', 1, 'Berlin', 29),(2, 'Proto', 0, 'Denver', 30), (3, 'Jupiter', 0, 'Oslo',50), (4, 'Mars', 0, 'Rio De Janeiro', 27), (5, 'Venus', 0, 'Cairo', 35)]

print('%-2s %-15s %-7s %-15s %-10s' %('ID','NAME','GENDER', 'LOCATION', 'AGE'))
print('-'*50)
gender = ''
for person in people:
    if person[2] == 0:
        gender = 'f'
    else:
        gender = 'm'
    print('%-2d %-15s %-7s %-15s %-10d' %(person[0],person[1], gender, person[3], person[4]))
print('-'*50)
    
    