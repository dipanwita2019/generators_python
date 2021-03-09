
#replacing the return with yield produces a generator
def infinite_seq():
    num=0
    while True:
        yield num
        num +=1


def finite_seq():
    nums = [1,2,3]
    for num in nums:
        yield num




#using [] means list and using () means a generator

num_squared_lc = [num**2 for num in range(1,5)]

num_squared_gc = (num**2 for num in range(1,5))