letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
for letter, num in zip(letters, numbers):
    print("{}: {}".format(letter, num))

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters, nums)
