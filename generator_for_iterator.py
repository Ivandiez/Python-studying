# def my_range(x):
#     i = 0
#     while i < x:
#         yield i
#         i += 1


# for x in my_range(5):
#     print(x)


# my_generator
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
lessons1 = ["a", "b", "c"]

"""
This is my function that works with iterables like built-in function enumerate()
"""


def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for i in range(len(iterable)):
        yield start, iterable[i]
        start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

for i, lesson in enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

"""
The chunker with yield.
"""
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
