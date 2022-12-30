d = {
    'name': 'Pratyakhs Suri',
    'Roll': '2002276',
    'Branch': 'Mrchanical (CS)'
}
# print(d)
# print(type(d))
# print(d['name'])

# for i in d:
#     print(d[i])


# get() ->  used to get the value of the respective key 
# print(d.get('name'))

# keys() -> returns the keys of the dictionary

for i in d.keys():
    print(d[i])

# to get keys from the values using list comprehension
# val  = {i for i in d if d[i]=='2002276'}
# print(val)

# we can create dictionry by using dict() keyword
dictionary = dict(firstname='pratyaksh', lastname='suri')
print(dictionary)

# update() -> used to update the the value in the dictionary
dictionary.update({'firstname': "mummy"})
print(dictionary)
