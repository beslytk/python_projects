#Generator Examples

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result    

print(square_numbers([1,2,3]))
########################################

print("generator output: ")
# use yield to make a generator
def square_numbers_gen(nums):
    for i in nums:
        yield (i*i)
print(square_numbers_gen([1,2,3]))
print(next(square_numbers_gen([1,2,3])))
print(next(square_numbers_gen([1,2,3])))
print(next(square_numbers_gen([1,2,3])))

########################################

def square_numbers_gen2(nums):
    for i in nums:
        yield (i*i)
my_nums = square_numbers_gen2([1,2,3,4,5])

for num in my_nums:
    print( num)
########################################

# my_nums = square_numbers([1,2,3,4,5])
my_numsList = [x*x for x in [1,2,3,4,5]]
print( my_numsList)
for num in my_numsList:
    print( num)

########################################


########################################
my_numsGenerator = (x*x for x in [1,2,3,4,5])
print( my_numsGenerator)
for num in my_numsGenerator:
    print( num)

print (list(my_numsGenerator)) # [1, 4, 9, 16, 25]
