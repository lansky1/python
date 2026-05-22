# Reliability & Concurrency

## Topics

- [ ] Design for failure.
- [ ] Handle exceptions meaningfully, not defensively.
- [ ] Think about concurrency correctly.
- [ ] Know the difference between I/O-bound and CPU-bound problems.
- [ ] Choose the appropriate solution for each kind of concurrency problem.

## Concurrency decision guide

- **I/O-bound, normal blocking libraries** — use threads or `ThreadPoolExecutor`.
- **I/O-bound, async-compatible libraries** — use `asyncio`.
- **CPU-bound, pure Python** — use `multiprocessing` or `ProcessPoolExecutor`.
- **CPU-bound, NumPy / C-extension work** — threads may help if the extension releases the GIL, but measure.
- **Shared mutable state** is where many concurrency bugs start. Prefer message passing, queues, immutable data, or isolated processes.
- Catch exceptions where you can add meaning or recover. Otherwise let them propagate.

## References

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — `try`, `except`, `else`, `finally`, exception chaining, cleanup, custom exceptions.
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) — the standard exception hierarchy so you catch the right errors.
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html) — use logging instead of hiding failures or relying on ad-hoc `print` statements.
- [Concurrent Execution overview](https://docs.python.org/3/library/concurrency.html) — official overview of Python concurrency modules.
- [`threading`](https://docs.python.org/3/library/threading.html) — I/O-bound work with blocking libraries; locks, events, race conditions.
- [`queue`](https://docs.python.org/3/library/queue.html) — thread-safe queues for coordinating worker threads.
- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) — process-based parallelism for CPU-bound work.
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — practical thread/process pool interface.
- [`asyncio`](https://docs.python.org/3/library/asyncio.html) — async I/O with coroutines, tasks, streams, queues, subprocess support.
- [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html) — cancellation, debugging, logging, common async mistakes.
