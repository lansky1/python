# Python Mastery Checklist

These are advanced Python topics I want to understand one day as I keep learning.

Use the references like a roadmap:

- Start with the official Python docs links.
- Use the deep dives only after the core idea makes sense.
- For every topic, learn what problem it solves, what it costs, and when not to use it.
- Most Python documentation links use `/3/`, which points to the current Python 3 docs. If you are studying a specific Python version, use the version selector on the docs site.
- When studying performance, measure first. Do not optimize by guessing.

## Python Internals

- [ ] Understand the execution model: how Python runs code.
- [ ] Understand the GIL.
- [ ] Understand memory management.
- [ ] Understand reference counting.

References:

- [Python execution model](https://docs.python.org/3/reference/executionmodel.html): start here for code blocks, frames, scope, name resolution, exceptions, processes, threads, and the Python runtime model.
- [Python data model](https://docs.python.org/3/reference/datamodel.html): learn how objects, attributes, special methods, classes, and protocols fit together.
- [dis - Python bytecode disassembler](https://docs.python.org/3/library/dis.html): use this when you want to see the bytecode Python compiles from your source code.
- [CPython internals guide](https://devguide.python.org/internals/): a map of deeper CPython implementation resources.
- [Memory Management - Python/C API](https://docs.python.org/3/c-api/memory.html): explains Python's private heap and memory allocators. This is lower-level, but useful for understanding what Python manages for you.
- [gc - Garbage Collector interface](https://docs.python.org/3/library/gc.html): learn how Python exposes the cyclic garbage collector.
- [sys.getrefcount](https://docs.python.org/3/library/sys.html#sys.getrefcount): useful for experiments with reference counts. Treat results carefully because calling the function itself temporarily adds a reference.
- [Global Interpreter Lock glossary entry](https://docs.python.org/3/glossary.html#term-global-interpreter-lock): short official definition of the GIL.
- [Thread states and the global interpreter lock](https://docs.python.org/3/c-api/threads.html#thread-state-and-the-global-interpreter-lock): deeper explanation of why CPython needs the GIL around Python objects.
- [PEP 703 - Making the GIL Optional](https://peps.python.org/pep-0703/): read later for modern context around free-threaded Python and why removing the GIL is hard.

## Advanced Language Features

- [ ] Use generators correctly.
- [ ] Use decorators correctly.
- [ ] Use context managers correctly.
- [ ] Use metaclasses correctly.
- [ ] Use descriptors correctly.
- [ ] Know when not to use advanced features.
- [ ] Remember that restraint is a mark of expertise.

References:

- [Functional Programming HOWTO - Iterators and generators](https://docs.python.org/3/howto/functional.html#generators): start here for iterators, generator expressions, and generator functions.
- [Yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions): the precise language reference for `yield` and `yield from`.
- [Function definitions and decorators](https://docs.python.org/3/reference/compound_stmts.html#function-definitions): official syntax rules for decorators on functions.
- [PEP 318 - Decorators for Functions and Methods](https://peps.python.org/pep-0318/): historical context for why decorator syntax exists.
- [contextlib](https://docs.python.org/3/library/contextlib.html): practical tools for writing context managers with `with`.
- [The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement): exact execution rules for context managers.
- [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html): the best starting point for descriptors, properties, methods, `staticmethod`, and `classmethod`.
- [Customizing class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation): start here for metaclasses and class creation hooks.
- [PEP 20 - The Zen of Python](https://peps.python.org/pep-0020/): use this as a restraint reminder. Advanced features should make code clearer or safer, not just clever.

Good order to learn these:

1. Iterators and generators.
2. Context managers.
3. Decorators.
4. Descriptors.
5. Metaclasses.

Metaclasses should usually come last because most problems can be solved more clearly with normal classes, functions, decorators, descriptors, or `__init_subclass__`.

## Performance

- [ ] Know where Python is slow and why.
- [ ] Understand dynamic typing overhead.
- [ ] Understand why pure-Python loops can be slow.
- [ ] Understand how the GIL affects performance.
- [ ] Reach for the right tools when needed: NumPy, Cython, multiprocessing, and async I/O.
- [ ] Understand the trade-offs of performance tools instead of cargo-culting them.
- [ ] Profile and optimize instead of guessing.

References:

- [timeit](https://docs.python.org/3/library/timeit.html): use for small, isolated timing experiments.
- [cProfile and profile](https://docs.python.org/3/library/profile.html): use for finding where real programs spend time.
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html): use for tracking memory allocations.
- [dis](https://docs.python.org/3/library/dis.html): useful for seeing how much bytecode a piece of Python creates.
- [What is NumPy?](https://numpy.org/doc/stable/user/whatisnumpy.html): explains why NumPy can be much faster than pure-Python numeric loops.
- [NumPy ufunc basics](https://numpy.org/doc/stable/user/basics.ufuncs.html): learn vectorized operations.
- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html): learn how NumPy applies operations across arrays without manual loops.
- [Cython basic tutorial](https://cython.readthedocs.io/en/stable/src/tutorial/cython_tutorial.html): start here if pure Python is too slow and NumPy is not enough.
- [Cython with NumPy](https://cython.readthedocs.io/en/stable/src/tutorial/numpy.html): useful when speeding up array-heavy code that cannot be expressed cleanly with NumPy operations alone.
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html): use when CPU-bound pure-Python work needs multiple cores.
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html): higher-level API for thread pools and process pools.
- [asyncio](https://docs.python.org/3/library/asyncio.html): use for high-concurrency I/O when the libraries you depend on are async-friendly.

Performance decision guide:

- If code is slow, profile first with `cProfile` or measure a small hypothesis with `timeit`.
- If the hot path is numeric loops over arrays, try NumPy vectorization first.
- If the hot path is still CPU-bound and cannot be vectorized, consider Cython or another compiled extension path.
- If pure-Python CPU-bound work needs multiple cores, use `multiprocessing` or `ProcessPoolExecutor`.
- If work spends most of its time waiting on files, network, APIs, or databases, consider threads or `asyncio`.
- If memory is the problem, use generators, streaming I/O, and `tracemalloc` before changing architecture.

## Systems Thinking

- [ ] Understand how Python code interacts with the OS.
- [ ] Understand how Python code interacts with the file system.
- [ ] Understand how Python code interacts with the network.
- [ ] Understand how Python code interacts with memory.

References:

- [os](https://docs.python.org/3/library/os.html): environment variables, process information, file descriptors, permissions, paths, and OS-level behavior.
- [pathlib](https://docs.python.org/3/library/pathlib.html): modern object-oriented path handling. Prefer this for most path code.
- [io](https://docs.python.org/3/library/io.html): understand text I/O, binary I/O, buffering, encodings, and file-like objects.
- [tempfile](https://docs.python.org/3/library/tempfile.html): safe temporary files and directories.
- [subprocess](https://docs.python.org/3/library/subprocess.html): running external programs and understanding process boundaries.
- [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html): start here for low-level networking concepts.
- [socket](https://docs.python.org/3/library/socket.html): exact API for network sockets.
- [mmap](https://docs.python.org/3/library/mmap.html): memory-mapped files. Read after normal file I/O is comfortable.
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html): practical memory allocation tracing.

Main ideas to learn:

- Files, sockets, subprocesses, and locks are external resources. Clean them up explicitly, usually with `with`.
- Text and bytes are different. Always know the encoding boundary.
- The OS can fail any operation: files can disappear, permissions can be denied, networks can time out, and subprocesses can exit badly.
- A Python process has memory, open files, environment variables, signals, threads, and child processes. Good programs account for those boundaries.

## Reliability And Concurrency

- [ ] Design for failure.
- [ ] Handle exceptions meaningfully, not defensively.
- [ ] Think about concurrency correctly.
- [ ] Know the difference between I/O-bound and CPU-bound problems.
- [ ] Choose the appropriate solution for each kind of concurrency problem.

References:

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html): start here for `try`, `except`, `else`, `finally`, exception chaining, cleanup, and custom exceptions.
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html): learn the standard exception hierarchy so you catch the right errors.
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html): use logging instead of hiding failures or relying on ad hoc print statements.
- [Concurrent Execution overview](https://docs.python.org/3/library/concurrency.html): official overview of Python concurrency modules.
- [threading](https://docs.python.org/3/library/threading.html): useful for I/O-bound work with blocking libraries and for understanding locks, events, and race conditions.
- [queue](https://docs.python.org/3/library/queue.html): thread-safe queues for coordinating worker threads.
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html): process-based parallelism for CPU-bound work.
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html): practical thread/process pool interface.
- [asyncio](https://docs.python.org/3/library/asyncio.html): async I/O with coroutines, tasks, streams, queues, and subprocess support.
- [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html): important follow-up for cancellation, debugging, logging, and common async mistakes.

Concurrency decision guide:

- I/O-bound with normal blocking libraries: use threads or `ThreadPoolExecutor`.
- I/O-bound with async-compatible libraries: use `asyncio`.
- CPU-bound pure Python: use `multiprocessing` or `ProcessPoolExecutor`.
- CPU-bound NumPy/C-extension work: threads may help if the extension releases the GIL, but measure.
- Shared mutable state is where many concurrency bugs start. Prefer message passing, queues, immutable data, or isolated processes.
- Catch exceptions where you can add meaning or recover. Otherwise let them propagate.
