import time
poem = open('./poem.txt', 'r')

for i in poem.readlines():
    print(i, end = '')
    time.sleep(5)
poem.close()

while True:
    pass
