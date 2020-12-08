# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test
# Description:  
# Author:       Allen
# Time:         2020/9/14 19:21
# -------------------------------------------------------------------------------
# Definition for a binary tree node.
import collections
import math
from typing import List

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if len(preorder) == len(inorder) and len(preorder) > 1:
#             root_value = preorder[0]
#             root_index = inorder.index(root_value)
#             left_node_range = inorder[:root_index]
#             right_node_range = inorder[root_index + 1:]
#
#             if root_index > 0:
#                 left_value = inorder[root_index - 1]
#             else:
#                 left_value = None
#
#             node = TreeNode(root_value)
#             left_node = TreeNode(left_value)
#
#             node.left = left_node
#             if left_value:
#                 preorder = preorder[preorder.index(left_value) + 1:]
#             else:
#                 preorder = preorder[preorder.index(root_value) + 1:]
#
#             inorder = inorder[inorder.index(root_value) + 1:]
#             node.right = self.buildTree(preorder, inorder)
#         elif len(preorder) == 1:
#             node = TreeNode(preorder[0])
#         else:
#             return None
#         return node


# if __name__ == '__main__':
#     class Solution2:
#         def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#             v = [gas[i] - cost[i] for i in range(len(gas))]
#             if sum(v) >= 0:
#                 for start_index in range(len(v)):
#                     start_gas = gas[start_index]
#                     last_cost = cost[start_index]
#                     run_index = start_index
#                     _gas = start_gas
#                     while run_index - start_index - len(v) != 0:
#                         run_index += 1
#                         if run_index >= len(v):
#                             _gas = _gas + v[run_index - len(v)]
#                         else:
#                             _gas = _gas + v[run_index]
#                         if not _gas >= 0:
#                             break
#                         if run_index - start_index - len(v) == 0:
#                             left_gas = _gas - last_cost
#                             if left_gas >= 0:
#                                 return run_index if run_index < len(v) else run_index - len(v)
#                             else:
#                                 break
#             else:
#                 return -1
#
#
#     class Solution:
#         def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#             v = [gas[i] - cost[i] for i in range(len(gas))]
#             if sum(v) >= 0:
#                 for start_index in range(len(v)):
#                     index = start_index
#                     next_index = index + 1 if index + 1 < len(v) else 0
#                     left_gas = v[index]
#                     if left_gas < 0:
#                         continue
#                     while next_index != start_index and left_gas >= 0:
#                         left_gas += v[next_index]
#                         next_index = next_index + 1 if next_index + 1 < len(v) else 0
#                     if left_gas >= 0:
#                         return start_index
#             else:
#                 return -1
#
#
#     s = Solution()
#     gas = [5, 1, 2, 3, 4]
#     cost = [4, 4, 1, 5, 1]
#     res = s.canCompleteCircuit(gas, cost)
#     print(res)


if __name__ == '__main__':
    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            if len(nums) >= 2:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        n = i + 1
                        while True:
                            if n == len(nums):
                                return
                            if nums[n] != 0:
                                nums[i], nums[n] = nums[n], nums[i]
                                break
                            n += 1


    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print(nums)


    def function(n, max_numb):
        if n == 0:
            return max(max_numb) + 1
        else:
            return n


    nums = sorted(nums, key=function(lambda x: x, max(nums)), reverse=True)
    print(nums)


    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None


    # class Solution:
    #     def insertionSortList(self, head: ListNode) -> ListNode:
    #         if not head:
    #             return
    #         if not head.next:
    #             return head
    #         else:
    #             _h = head
    #             _l = [head.val]
    #             while head.next:
    #                 _l.append(head.next.val)
    #                 head = head.next
    #             _l.sort()
    #             i = 0
    #             head = _h
    #             while _h:
    #                 _h.val = _l[i]
    #                 i += 1
    #                 _h = _h.next
    #             return head

    # class Solution:
    #     def insertionSortList(self, head: ListNode) -> ListNode:
    #         if not head or not head.next:
    #             return head
    #         else:
    #             dummy_head = ListNode(0)
    #             dummy_head.next = head
    #             last = head
    #             cur = head.next
    #             while cur:
    #                 if last.val <= cur.val:
    #                     last = last.next
    #                 else:
    #                     prev = dummy_head
    #                     while prev.next.val <= cur.val:
    #                         prev = prev.next
    #                     last.next = cur.next
    #                     prev.next = cur
    #                     cur.next = prev.next
    #                 cur = last.next
    #             return dummy_head.next
    #
    #
    # class Solution:
    #     def insertionSortList(self, head: ListNode) -> ListNode:
    #         if not head:
    #             return head
    #
    #         dummyHead = ListNode(0)
    #         dummyHead.next = head
    #         lastSorted = head
    #         curr = head.next
    #
    #         while curr:
    #             if lastSorted.val <= curr.val:
    #                 lastSorted = lastSorted.next
    #             else:
    #                 prev = dummyHead
    #                 while prev.next.val <= curr.val:
    #                     prev = prev.next
    #                 lastSorted.next = curr.next
    #                 curr.next = prev.next
    #                 prev.next = curr
    #             curr = lastSorted.next
    #
    #         return dummyHead.next

    # class Solution:
    #     def translateNum(self, num: int) -> int:
    #         if num is None:
    #             return 0
    #         elif num < 10:
    #             return 1
    #         else:
    #             num = str(num)
    #             p = self.translateNum(int(num[1:]))
    #             if int(num[:2]) <= 25 and num[0] not in [0, '0']:
    #                 if num[2:]:
    #                     l = self.translateNum(int(num[2:]))
    #                 else:
    #                     l = 1
    #             else:
    #                 l = 0
    #             return p + l
    #
    #
    # s = Solution()
    # res = s.translateNum(220)
    # print(res)

    # class Solution:
    #     def sortString(self, s: str) -> str:
    #         if not s:
    #             return None
    #         else:
    #             res = ''
    #             num = [0] * 26
    #             for ch in s:
    #                 num[ord(ch) - ord('a')] += 1
    #
    #             while len(res) < len(s):
    #                 for i in range(len(num)):
    #                     if num[i] > 0:
    #                         num[i] -= 1
    #                         res = '{}{}'.format(res, chr(i + ord('a')))
    #                 for i in range(25, -1, -1):
    #                     if num[i] > 0:
    #                         num[i] -= 1
    #                         res = '{}{}'.format(res, chr(i + ord('a')))
    #             return res