#!/bin/python3

import math
import os
import random
import re
import sys

def mostBalancedPartition(parent, files_size):
    n = len(parent)
    graph = [[] for _ in range(n)]
    for i, p in enumerate(parent):
        if p != -1:
            graph[p].append(i)

    # Helper function for DFS to compute the size of each subtree
    def dfs(node):
        size = files_size[node]
        for child in graph[node]:
            size += dfs(child)
        return size

    # Initialize the total size of the entire structure and minimum difference
    total_size = dfs(0)
    min_partition_diff = float('inf')

    # Calculate the minimum absolute difference between the partition sizes
    for i in range(1, n):
        partition1_size = dfs(i)
        partition2_size = total_size - partition1_size
        diff = abs(partition1_size - partition2_size)
        min_partition_diff = min(min_partition_diff, diff)

    return min_partition_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())
    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())
    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')
    fptr.close()
