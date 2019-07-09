#simple loop

people = ['juana','jana','karina','laura']

print('****simple loop****')
for person in people:
	print('Current Person: {0}'.format(person))

#break 
print('****Break loop****')
for person in people:
	if person == 'benito':
	   break
	print('Current person: {0}'.format(person))
