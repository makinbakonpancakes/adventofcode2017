nums = [int(x) for x in open('input.txt').readlines()]
index = 0
count = 0
while index >= 0 and index < len(nums):
    count += 1
    jump = nums[index]
    nums[index] += 1
    index += jump
print(count)

nums = [int(x) for x in open('input.txt').readlines()]
index = 0
count = 0
while index >= 0 and index < len(nums):
    count += 1
    jump = nums[index]
    if jump >= 3:
        nums[index] -= 1
    else:
        nums[index] += 1
    index += jump
print(count)
