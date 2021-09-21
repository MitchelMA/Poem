import time
poem = open('./poem.txt', 'r')

for i in poem.readlines():
    print(i, end = '')
    
    if i != '\n':
        time.sleep(2)
poem.close()

while True:
    pass
