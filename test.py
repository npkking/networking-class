import threading
import time

# global x
x = 0

def increment(by):
    """ function to increment global variable x """
    global x
    local = x
    local += by
    time.sleep(1e-10)  # to increase contention
    x = local

def increment_task(by):
    """ thread task to call increment 10 times. """
    for _ in range(10):
        increment(by)

def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=increment_task, args=(5,))
    t2 = threading.Thread(target=increment_task, args=(10,))

    # start threads
    t1.start()
    t2.start()

    # wait for threads to complete
    t1.join()
    t2.join()

    print(f"Final value of x: {x}")

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print(f"Interation {i}: x = {x}")

    