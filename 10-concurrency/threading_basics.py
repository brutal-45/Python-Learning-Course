"""
Module: threading_basics.py
Topic: Threading Basics
Level: Advanced

This file teaches you about:
- Creating threads
- Thread synchronization
- Lock, RLock, Semaphore
- Thread pools
- Thread-safe operations
"""

# =============================================================================
# SECTION 1: CREATING THREADS
# =============================================================================

print("=" * 60)
print("CREATING THREADS")
print("=" * 60)

import threading
import time


def worker(name, delay):
    """A simple worker function."""
    print(f"  {name} starting")
    time.sleep(delay)
    print(f"  {name} finished")


# Method 1: Using Thread class directly
print("Method 1: Thread class")
thread = threading.Thread(target=worker, args=("Thread-1", 0.5))
thread.start()
thread.join()  # Wait for thread to finish

# Method 2: Creating a Thread subclass
print("\nMethod 2: Thread subclass")


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"  {self.name} starting")
        time.sleep(self.delay)
        print(f"  {self.name} finished")


t = MyThread("CustomThread", 0.3)
t.start()
t.join()

# =============================================================================
# SECTION 2: MULTIPLE THREADS
# =============================================================================

print("\n" + "=" * 60)
print("MULTIPLE THREADS")
print("=" * 60)


def task(name, duration):
    """Simulate a task."""
    print(f"  {name} started")
    time.sleep(duration)
    print(f"  {name} completed after {duration}s")


threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread-{i}", 0.3))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

print("All threads completed!")

# =============================================================================
# SECTION 3: THREAD SYNCHRONIZATION - LOCK
# =============================================================================

print("\n" + "=" * 60)
print("THREAD SYNCHRONIZATION - LOCK")
print("=" * 60)

# Shared resource problem
counter = 0
lock = threading.Lock()


def increment_unsafe():
    """Unsafe increment (race condition)."""
    global counter
    temp = counter
    time.sleep(0.0001)  # Simulate some work
    counter = temp + 1


def increment_safe():
    """Safe increment with lock."""
    global counter
    with lock:
        temp = counter
        time.sleep(0.0001)
        counter = temp + 1


# Unsafe version
counter = 0
threads = [threading.Thread(target=increment_unsafe) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Unsafe counter: {counter} (expected 100)")

# Safe version
counter = 0
threads = [threading.Thread(target=increment_safe) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Safe counter: {counter} (expected 100)")

# =============================================================================
# SECTION 4: RLOCK AND SEMAPHORE
# =============================================================================

print("\n" + "=" * 60)
print("RLock AND SEMAPHORE")
print("=" * 60)

# RLock (Reentrant Lock) - can be acquired multiple times by same thread
rlock = threading.RLock()


def nested_lock():
    """Demonstrate RLock with nested locking."""
    with rlock:
        print("  First lock acquired")
        with rlock:  # Same thread can acquire again
            print("  Second lock acquired (nested)")
    print("  Both locks released")


nested_lock()

# Semaphore - limit concurrent access
semaphore = threading.Semaphore(2)  # Max 2 threads at a time


def limited_access(name):
    """Access limited resource."""
    with semaphore:
        print(f"  {name} acquired semaphore")
        time.sleep(0.3)
        print(f"  {name} releasing semaphore")


threads = [threading.Thread(target=limited_access, args=(f"Thread-{i}",))
           for i in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# =============================================================================
# SECTION 5: THREAD POOL
# =============================================================================

print("\n" + "=" * 60)
print("THREAD POOL (concurrent.futures)")
print("=" * 60)

from concurrent.futures import ThreadPoolExecutor


def square(n):
    """Calculate square."""
    time.sleep(0.1)
    return n * n


# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit individual tasks
    future = executor.submit(square, 5)
    print(f"  Result of square(5): {future.result()}")

    # Submit multiple tasks
    numbers = [1, 2, 3, 4, 5]
    results = list(executor.map(square, numbers))
    print(f"  Results: {results}")

# =============================================================================
# SECTION 6: THREAD-LOCAL STORAGE
# =============================================================================

print("\n" + "=" * 60)
print("THREAD-LOCAL STORAGE")
print("=" * 60)

local_data = threading.local()


def process_data(name):
    """Each thread has its own local data."""
    local_data.value = name
    time.sleep(0.1)
    print(f"  {threading.current_thread().name}: local_data.value = {local_data.value}")


threads = [threading.Thread(target=process_data, args=(f"Data-{i}",))
           for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# =============================================================================
# SECTION 7: TIMERS AND EVENTS
# =============================================================================

print("\n" + "=" * 60)
print("TIMERS AND EVENTS")
print("=" * 60)

# Timer
def delayed_message():
    print("  Timer executed!")


timer = threading.Timer(0.5, delayed_message)
timer.start()
print("Timer started...")
timer.join()

# Event
event = threading.Event()


def waiter():
    print("  Waiting for event...")
    event.wait()  # Block until event is set
    print("  Event received!")


def setter():
    time.sleep(0.3)
    print("  Setting event...")
    event.set()


t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)
t1.start()
t2.start()
t1.join()
t2.join()

# =============================================================================
# SECTION 8: WHEN TO USE THREADS
# =============================================================================

print("\n" + "=" * 60)
print("WHEN TO USE THREADS")
print("=" * 60)

print("""
THREADING IS GOOD FOR:
- I/O-bound operations (network, file, database)
- GUI applications (keep UI responsive)
- Background tasks

THREADING IS NOT GOOD FOR:
- CPU-bound tasks (use multiprocessing instead)
- Tasks requiring true parallelism

PYTHON'S GIL (Global Interpreter Lock):
- Only one thread executes Python bytecode at a time
- This is why threading doesn't help CPU-bound tasks
- I/O operations release the GIL, so threads work well for I/O
""")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about threading!")
    print("📚 Next: Learn about asyncio in asyncio_basics.py")
    print("=" * 60)
