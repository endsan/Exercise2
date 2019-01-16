# Mutex and Channel basics

### What is an atomic operation?
> In concurrent programming, it is program operations that run completely independent of any other process.

### What is a semaphore?
> A variable or abstract data type, to control access to a common resource by multiple processes (in a concurrent system)

### What is a mutex?
> A mutially exclusive flag. It allowes one thread in and black the access to all the other threads. 

### What is the difference between a mutex and a binary semaphore?
> A mutex semaphore is "owned" by the task that takes it. If task B attempts to semGive a mutex currently held by task A, task B will fail and return an error. For binary semphores, task B is penden waiting for something to happen. Then task B should run and take appropriate actions for the sensor trip, and then go back to waiting. 

### What is a critical section?
> The part of the program that accesses shared resources. To disrupt other processes, the process must be in its critical section.

### What is the difference between race conditions and data races?
 > A race condition is a flaw that occurs when the timing or ordering of events effect the program's correctness. To produce a race condition you need for instance context switches, OS-signals, memory operations on a multiprocessor and hardware interrupts. A data race happens if there are two memory accesses in a program where both tarhet the same location, are performed concurrently by two threads, are not reads and are not synchronization operations.

### List some advantages of using message passing over lock-based synchronization primitives.
> Can use concurency. Safety and convenience, and easier to reason about. Avoid deadlocks, control of memory access for each process.

### List some advantages of using lock-based synchronization primitives over message passing.
> Easier, you can write straight forward. Don't have to think about detail about memory allocation. Message passing can lead to complex error messages and errors. Order is "random", so you don't have to think about when processes are executed.
