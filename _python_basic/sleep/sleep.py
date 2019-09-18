import time
import datetime
import random

i = 1

while True:
    print('\n' + str(i) + '回目')
    print(datetime.datetime.now().strftime("%Y%m%d:%H:%M:%S"))

    time.sleep(random.randrange(1,4))
    
    print(datetime.datetime.now().strftime("%Y%m%d:%H:%M:%S"))
    i = i + 1
    if i > 5: break

