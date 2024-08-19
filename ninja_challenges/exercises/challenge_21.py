# Challenge 21 - Interval List Intersections
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].
#
# Example 1:
# Input: first_list = [[0,2],[5,10],[13,23],[24,25]],
#        second_list = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
# Example 2:
# Input: first_list = [[1,3],[5,9]],
#        second_list = []
# Output: []


def interval_intersection(
    first_list: list[list[int]], second_list: list[list[int]]
) -> list[list[int]]: ...