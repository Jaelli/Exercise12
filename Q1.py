# What is wrong with this;

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'

print(cheese)

# Without the square brackets on 'Oke' it will add as string data
# rather than an item to a list, so the letters will go on individually

# How should 'Oke' be added to the list?

cheese += ['Oke']
# or, as it's only one item
cheese.append('Oke')

print(cheese)

# How would you add two new cheeses with a single command?

cheese += ['Red Leicester', 'Gouda']
# or
cheese.extend(['Red Leicester', 'Gouda'])

print(cheese)
