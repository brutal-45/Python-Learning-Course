"""
Module: asyncio_basics.py
Topic: AsyncIO Basics
Level: Advanced

This file teaches you about:
- async/await syntax
- Coroutines
- Tasks and Futures
- Async context managers
- Async generators
"""

# =============================================================================
# SECTION 1: COROUTINES BASICS
# =============================================================================

print("=" * 60)
print("COROUTINES BASICS")
print("=" * 60)

import asyncio
import time


# Define a coroutine
async def hello():
    """A simple coroutine."""
    print("  Hello")
    await asyncio.sleep(0.5)  # Non-blocking sleep
    print("  World")


# Run the coroutine
print("Running hello():")
asyncio.run(hello())

# =============================================================================
# SECTION 2: MULTIPLE COROUTINES
# =============================================================================

print("\n" + "=" * 60)
print("MULTIPLE COROUTINES")
print("=" * 60)


async def fetch_data(name, delay):
    """Simulate fetching data."""
    print(f"  {name}: Starting fetch")
    await asyncio.sleep(delay)
    print(f"  {name}: Fetch complete")
    return f"{name} data"


async def main():
    """Run multiple coroutines concurrently."""
    print("Sequential:")
    start = time.time()
    result1 = await fetch_data("A", 0.3)
    result2 = await fetch_data("B", 0.3)
    print(f"  Results: {result1}, {result2}")
    print(f"  Time: {time.time() - start:.2f}s")

    print("\nConcurrent (gather):")
    start = time.time()
    results = await asyncio.gather(
        fetch_data("C", 0.3),
        fetch_data("D", 0.3),
        fetch_data("E", 0.3)
    )
    print(f"  Results: {results}")
    print(f"  Time: {time.time() - start:.2f}s")


asyncio.run(main())

# =============================================================================
# SECTION 3: TASKS
# =============================================================================

print("\n" + "=" * 60)
print("TASKS")
print("=" * 60)


async def background_task(name, duration):
    """A background task."""
    print(f"  {name}: Started")
    await asyncio.sleep(duration)
    print(f"  {name}: Completed")
    return f"{name} result"


async def tasks_demo():
    """Demonstrate tasks."""
    # Create tasks
    task1 = asyncio.create_task(background_task("Task-1", 0.5))
    task2 = asyncio.create_task(background_task("Task-2", 0.3))

    print("Tasks created, doing other work...")
    await asyncio.sleep(0.1)
    print("Other work done")

    # Wait for tasks
    result1 = await task1
    result2 = await task2
    print(f"  Results: {result1}, {result2}")


asyncio.run(tasks_demo())

# =============================================================================
# SECTION 4: ASYNC TIMEOUTS AND WAITING
# =============================================================================

print("\n" + "=" * 60)
print("TIMEOUTS AND WAITING")
print("=" * 60)


async def slow_operation():
    """A slow operation."""
    await asyncio.sleep(2)
    return "Done"


async def timeout_demo():
    """Demonstrate timeout."""
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.5)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Operation timed out!")


asyncio.run(timeout_demo())

# =============================================================================
# SECTION 5: ASYNC ITERATORS AND GENERATORS
# =============================================================================

print("\n" + "=" * 60)
print("ASYNC ITERATORS AND GENERATORS")
print("=" * 60)


async def async_count(n):
    """Async generator."""
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i


async def async_iterator_demo():
    """Demonstrate async iteration."""
    print("Async iteration:")
    async for num in async_count(5):
        print(f"  {num}")


asyncio.run(async_iterator_demo())

# =============================================================================
# SECTION 6: ASYNC CONTEXT MANAGERS
# =============================================================================

print("\n" + "=" * 60)
print("ASYNC CONTEXT MANAGERS")
print("=" * 60)


class AsyncResource:
    """An async context manager."""

    async def __aenter__(self):
        print("  Acquiring resource...")
        await asyncio.sleep(0.2)
        print("  Resource acquired")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("  Releasing resource...")
        await asyncio.sleep(0.1)
        print("  Resource released")


async def context_demo():
    """Demonstrate async context manager."""
    async with AsyncResource() as resource:
        print("  Using resource...")


asyncio.run(context_demo())

# =============================================================================
# SECTION 7: ASYNCIO VS THREADING
# =============================================================================

print("\n" + "=" * 60)
print("ASYNCIO VS THREADING")
print("=" * 60)

print("""
ASYNCIO:
- Single-threaded, cooperative multitasking
- Better for many I/O-bound tasks
- No thread synchronization issues
- Lower memory overhead

THREADING:
- Multi-threaded, preemptive multitasking
- Better for CPU-bound tasks (with multiprocessing)
- Need to handle synchronization
- Each thread has memory overhead

WHEN TO USE ASYNCIO:
- Web scraping
- API clients
- Database operations
- Network servers
- Many concurrent I/O operations

WHEN TO USE THREADING:
- Legacy code with blocking I/O
- CPU-bound tasks (actually use multiprocessing)
- Simple background tasks
""")

# =============================================================================
# SECTION 8: PRACTICAL EXAMPLE - WEB REQUESTS
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - SIMULATED WEB REQUESTS")
print("=" * 60)


async def fetch_url(url, delay=0.3):
    """Simulate fetching a URL."""
    print(f"  Fetching {url}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"  Got response from {url}")
    return f"Content from {url}"


async def fetch_all():
    """Fetch multiple URLs concurrently."""
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments",
    ]

    start = time.time()
    results = await asyncio.gather(*[fetch_url(url) for url in urls])
    elapsed = time.time() - start

    print(f"\n  All requests completed in {elapsed:.2f}s")
    print(f"  Sequential would take ~{0.3 * len(urls):.2f}s")


asyncio.run(fetch_all())

# =============================================================================
# MAIN EXECUTION 
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ You've learned about asyncio!")
    print("📚 Explore the projects for practical applications!")
    print("=" * 60)
