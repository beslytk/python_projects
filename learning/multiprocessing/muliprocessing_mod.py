import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print(f'Sleeping 1 second(s)...')
    time.sleep(1)
    return f'Done Sleeping...1 seconds'

def do_something_args(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    # in order to pass args to a multiprocessing process, the args must be able to be serialized using pickle
    # converting python objects into a format, that can be deconstructed and constructed back in another python script 
    processes2 = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something_args, args=[1.5])
        p.start()
        processes2.append(p)

    for process in processes2:
        process.join()
    finish = time.perf_counter()
    print(f'finished in {round(finish-start, 2)} seconds(s)')
