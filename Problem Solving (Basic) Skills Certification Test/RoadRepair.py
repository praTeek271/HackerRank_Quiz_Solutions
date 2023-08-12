#!/bin/python3

import math
import os
import random
import re
import sys

def getMinCost(crew_id, job_id):
    # Write your code here
    n = len(crew_id)
    
    # Sort the crews and jobs to pair them optimally
    crew_id.sort()
    job_id.sort()
    
    # Calculate the total travel distance
    total_distance = 0
    for i in range(n):
        total_distance += abs(crew_id[i] - job_id[i])
    
    return total_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
