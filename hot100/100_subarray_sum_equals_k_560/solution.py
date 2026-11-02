"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -1000 <= nums[i] <= 1000
    - -10^7 <= k <= 10^7
"""

from typing import List
from collections import defaultdict


class Solution:

    '''
    这里为什么不需要用 dfs 呢，像之前那道 tree sum 的题目就是 需要dfs

    因为数组本身只有一条固定的线性路径：
    nums[0] -> nums[1] -> nums[2] -> ...
    使用 for 循环从左到右遍历，就已经完成了 DFS 在树中负责的“访问节点”工作，不需要递归。
    数组中：
    for num in nums:
        cur_sum += num
    所有之前出现的前缀和，都对应当前位置左侧的合法起点，所以 prefix_sum 不需要回溯删除。
    树则存在分叉：
        root
        /  \
    left  right
    必须使用 DFS：
    1. 进入左子树。
    2. 维护根到左侧当前节点的前缀和。
    3. 左子树完成后回溯删除其前缀和。
    4. 再进入右子树。
    左子树中的节点不是右子树节点的祖先，所以左侧前缀和不能用于计算右侧路径。
    核心区别：
    数组：只有一个遍历方向，所有旧前缀都在当前位置之前
    树：存在多个分支，只有当前祖先链上的前缀和有效
    因此：
    - 数组用普通循环 + 前缀和。
    - 树用 DFS + 前缀和 + 回溯。
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        ans = 0
        cur_sum = 0
        for num in nums:
            # 计算有多少组以 'num'为结尾，sum 为k 的 sub-array,
            cur_sum += num
            ans += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] += 1

        return ans
