nums= [2, 7, 11, 15]
target = 9
def SumOfTwo(array, target):
    l = len(array)
    for i in range(l):
        for j in range(l):
            if i == j : continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

output = SumOfTwo(nums,target)
print("Output:", output)