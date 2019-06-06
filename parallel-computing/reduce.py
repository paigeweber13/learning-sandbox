import multiprocessing
import threading

NUM_CPUS = multiprocessing.cpu_count()

def sum_array(array_to_sum):
    sum = 0
    for x in array_to_sum:
        sum += x
    return sum

def sum_array_static_parallel(array_to_sum):
    pass
