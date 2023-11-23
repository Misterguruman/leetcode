import itertools

def twoSum(self, nums: list[int], target: int) -> list[int]:
    combinations = itertools.combinations(nums, 2)

    for combination in combinations:
        if sum(combination) == target:
            x, y = combination

            if x == y:
                x_index = nums.index(x)
                return [x_index, nums.index(y, x_index + 1)]

            return [nums.index(x), nums.index(y)]
    