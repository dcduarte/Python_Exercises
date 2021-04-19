import time
count = 10

while count >= 0:
    time.sleep(1)
    if count == 3:
        print("3 - Getting close to blast off...")
        count -= 1
    elif count == 0:
        print("0 - Blast off!")
        break
    else:       
        print(count)
        count -= 1



