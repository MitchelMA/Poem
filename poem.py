import time
poem = open('./poem.txt', 'r')

for i in poem:
    print(i, end='', flush=True)

    if i != '\n':
        time.sleep(4.4)
else:
    time.sleep(6)
