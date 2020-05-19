import numpy as np
def dfs(nums, target, start_index, subset, result):
	if target == 0:
		print(subset[:])
		return result.append(subset[:])
	for i in range(start_index, len(nums)):
		if nums[i] > target:
			return
		if nums[i] == nums[i - 1] and i > start_index:
			continue
		subset.append(nums[i])
		dfs(nums, target - nums[i], i+1, subset, result)
		subset.pop()


candidates = [1, 11, 55, 165, 330, 462]
target = 496
nums = sorted(candidates)
result, subset = [], []
start_index = 0
dfs(nums, target, start_index, subset, result)
