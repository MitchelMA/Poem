poem = open('./poem.txt', 'r')
print(dir(poem))

for i in poem.readlines():
    print(i, end = '')