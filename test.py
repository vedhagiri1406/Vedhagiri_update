import time

def timer(func):
    def wrapper():
        start = time.time()          # start time
        func()                       # run the function
        end = time.time()            # end time
        print(f"Execution time: {end - start:.5f} seconds")
    return wrapper

@timer
def big_task():
    total = 0
    for i in range(1000000):
        total += i
    print("Task finished")

big_task()
