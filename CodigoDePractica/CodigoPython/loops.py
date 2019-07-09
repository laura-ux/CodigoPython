#simple loop

people = ['juana','jana','karina','laura']

print('****simple loop****')
for person in people:
	print('Current Person: {0}'.format(person))

#break 
print('****Break loop****')
for person in people:
	if person == 'karina':
	   break
	print('Current person: {0}'.format(person))

#continue 
print('*****continue loop******')
for person in people:
	if person == 'jana':
	   continue 
	print('current person: {0}'.format(person))
	print('en orden')
#ranger
print('****Renger loop*****')
for i in range(len(people)):
	print(people[i])

for i in range(0,len(people)):
	print('number: {0}'.format(i))

#while 
count=0
while count <= 10:
	print('Count:{0}'.format(count))
	count+=1
