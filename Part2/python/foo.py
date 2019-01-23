# Python 3.3.3 and 2.7.6
# python fo.py

from threading import Thread, Lock
mutex = Lock()
# Potentially useful thing:
#   In Python you "import" a global variable, instead of "export"ing it when you declare it
#   (This is probably an effort to make you feel bad about typing the word "global")
i = 0



def incrementingFunction():
    global i, mutex

    for j in range(1000000):
        #print("Hi from thread 1\n")

        mutex.acquire()
        try:
            i += 1
        finally:
            mutex.release()
# TODO: increment i 1_000_000 times

def decrementingFunction():
    global i, mutex

    for k in range(1000001):
        #print("Hi from thread 2\n")

        mutex.acquire()
        try:
            i -= 1
        finally:
            mutex.release()
    # TODO: decrement i 1_000_000 times



def main():
    global i, mutex

    incrementing = Thread(target = incrementingFunction, args = (),)
    decrementing = Thread(target = decrementingFunction, args = (),)

    # TODO: Start both threads
    incrementing.start()
    decrementing.start()

    incrementing.join()
    decrementing.join()

    print("The magic number is %d" % (i))


main()
