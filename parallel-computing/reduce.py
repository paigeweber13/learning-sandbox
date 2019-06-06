import multiprocessing
import threading

NUM_CPUS = multiprocessing.cpu_count()
SUM = 0

def sum_array(array_to_sum):
    sum = 0
    for x in array_to_sum:
        sum += x
    return sum

def sum_array_child_thread(array_to_sum, lock):
    local_sum = sum_array(array_to_sum)
    global SUM
    lock.aquire()
    SUM += local_sum
    lock.release()

def sum_array_static_parallel(array_to_sum, num_threads=NUM_CPUS):
    array_to_sum_len = len(array_to_sum)
    indices_per_thread = int(array_to_sum_len/num_threads) + 1
    completed_to_index = 0
    mylock = threading.Lock()
    for i in range(num_threads):
        next_completed_to_index = completed_to_index + indices_per_thread
        if next_completed_to_index > array_to_sum_len:
            next_completed_to_index = array_to_sum_len
        threading.Thread(
            target=sum_array_child_thread, 
            args=(array_to_sum[completed_to_index:next_completed_to_index],
                mylock)
            ).start()
        completed_to_index = next_completed_to_index
    pass
