# reading from file
# f = open('./Files.txt', 'r')
# file_data = f.read()
# f.close()
# print(file_data)
# writing to a new file
# f1 = open('./new_file.txt', 'w')
# f1.write("Hello there!\n")
# f1.close()

# files = []
# for i in range(10000):
#     files.close()
#     print(i)

with open("./Files.txt", "r") as f:
    file_data = f.read()
print(file_data)
