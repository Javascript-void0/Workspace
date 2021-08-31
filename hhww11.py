# for i in range(30005):
#     for j in range(30005):
#         if i ** 2 + j ** 2 == 30005:
#             print(i, j)

nums = [1]

def list_add_up(nums):
    res = []
    res.append(1)
    for i in range(len(nums) - 1):
        res.append(nums[i] + nums[i+1])
    res.append(1)
    return res

for i in range(10):
    nums = list_add_up(nums)
    print(nums)