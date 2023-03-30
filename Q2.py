# What is going on here? Can you explain the output?

tup = 'Hello'
print(len(tup))
# prints 5

tup = 'Hello',
print(len(tup))
# prints 1

# In the first section, as the data is just in quotation marks,
# it will default as string data
# so the output will be the number of characters in that string

# The data in the second section has a comma added outside the quotation marks
# which identifies the data as a tuple
# There is only the one item in this Tuple, which is the word 'Hello' as a whole
# so it will print 1
