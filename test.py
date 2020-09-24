import re

list1 = [[1,2,3],[4,5,6],[7,8,9]]
for line in list1:
    print(line)
col2 = [row[1] + 1 for row in list1]
print('\ncol 2:', col2,'\n')

for line in list1:
    print(line)
print('sum of each in a row:', list(map(sum,list1)))

list2 = list(range(4))
print('\nlist2:', list2)

D = {}
D['name'] = 'Alex'
print(D)
D['age'] = 32
print(D)
print(D['name'])

person = {'name':{'first': 'Alex', 'last': 'Green'},
            'job': ['dev', 'mgr'],
            'age': 32}
print(person)
print(person['name']['last'])
print(person['job'])
person['job'].append('lol')
print(person['job'])
print(sorted(person))
person = 0  # all mem freed, lol xD
print(person)

sq = [x ** 2 for x in range(6)]
print(sq)
