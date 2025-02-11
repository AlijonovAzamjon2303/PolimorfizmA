import time

start = time.time()

for i in range(int(1e4)):
    print(i / 100)

end = time.time()

print(end - start)