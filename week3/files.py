
# f = open('example.txt')

# # print(f.read())


# f2 = open('../README.md')

# print(f2.read())

f3 = open('nofile.txt', 'r+')


f3.write("Thank you for creating this file.")

f3.close()

f3 = open('nofile.txt', 'r+')

print(f3.read())

