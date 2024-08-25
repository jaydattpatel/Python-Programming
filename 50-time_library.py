'''
author : Jaydatt Patel
time library
'''
import time
from timeit import default_timer

# for x in range(2, 6):
#     print('Sleep {} seconds..'.format(x))
#     time.sleep(x) # "Sleep" for x seconds
# print('Done!')


# check how much function take time
def sum(x,y):
    time.sleep(5) # "Sleep" for x seconds
    return (x+y)

start = default_timer()
sum(3,2)
end = default_timer()
print(end - start)


