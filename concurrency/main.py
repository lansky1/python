# Standard Implementation
# Threads
# Individual Joins
# Post iteration Join
# Daemon

import time
import threading


def calculate_sum_square(n):
    print(sum([i**2 for i in range(n)]))


# CPU sits idle
def sleep(seconds):
    time.sleep(seconds)


def main():
    square_start_time = time.time()

    current_threads = []
    for i in range(5):
        # args param requires a tuple
        t = threading.Thread(target=calculate_sum_square, args=((i + 1) * 100000,))
        # main thread creates a child thread and hands off the work, will not wait for completion.
        t.start()
        # t.join()  # Here it ensures the current thread only executes, making it sequential again
        current_threads.append(t)
        # calculate_sum_square((i + 1) * 100000)

    # All threads — including the main thread — compete equally for CPU time.
    # GIL ensures only one runs at a time

    # This blocks the calling thread (main thread) until the thread whose `join()` method is called is terminated.
    # main wont run unless the thread on whom the join method is called is completed

    for t in current_threads:
        t.join()

    print(
        "Time taken to compute squares: ",
        round(time.time() - square_start_time, 2),
        "seconds",
    )

    sleep_start_time = time.time()

    for seconds in range(1, 2):
        sleep(seconds)

    print("Time taken to sleep: ", round(time.time() - sleep_start_time, 2), "seconds")


if __name__ == "__main__":
    main()
