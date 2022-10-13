from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums = list(set(nums))

    return len(nums)