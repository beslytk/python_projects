#  process pool executor => allows easy switch btw threads and processes depending on problem 
import concurrent.futures
import time
from unittest import result

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds} second(s)'

if __name__ == '__main__':
    # 
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # submit fn schedules a method to be executed and returns a future object
        # future object allows us to check on scheduled task
        f1= executor.submit(do_something,1)
        print(f1.result())
        
        # alternative way=> get results of completed processes one by one
        results_list_comp = [executor.submit(do_something,0.5) for _ in range(10)]
        for f in concurrent.futures.as_completed(results_list_comp):
            print(f.result())
        
        # demonstration that results are retrieved in order of completion 
        secs = [5, 4, 3, 2, 1]
        results_list_comp_cnt_dw = [executor.submit(do_something,sec) for sec in secs]
        for f in concurrent.futures.as_completed(results_list_comp_cnt_dw):
            print(f.result())
        
        # to run fn over a list of values:
        # submit returned future objects
        # map returns results directly
        # return results in ordrer that they started! 
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
