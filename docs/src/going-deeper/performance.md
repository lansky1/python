# Performance

## Topics

- [ ] Know where Python is slow and why.
- [ ] Understand dynamic typing overhead.
- [ ] Understand why pure-Python loops can be slow.
- [ ] Understand how the GIL affects performance.
- [ ] Reach for the right tools when needed: NumPy, Cython, multiprocessing, async I/O.
- [ ] Understand the trade-offs of performance tools instead of cargo-culting them.
- [ ] Profile and optimize instead of guessing.

## Decision guide

- If code is slow, profile first with `cProfile` or measure a small hypothesis with `timeit`.
- If the hot path is numeric loops over arrays, try NumPy vectorization first.
- If the hot path is still CPU-bound and cannot be vectorized, consider Cython or another compiled extension path.
- If pure-Python CPU-bound work needs multiple cores, use `multiprocessing` or `ProcessPoolExecutor`.
- If work spends most of its time waiting on files, network, APIs, or databases, consider threads or `asyncio`.
- If memory is the problem, use generators, streaming I/O, and `tracemalloc` before changing architecture.

## References

- [`timeit`](https://docs.python.org/3/library/timeit.html) — small, isolated timing experiments.
- [`cProfile` and `profile`](https://docs.python.org/3/library/profile.html) — finding where real programs spend time.
- [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html) — tracking memory allocations.
- [`dis`](https://docs.python.org/3/library/dis.html) — seeing how much bytecode a piece of Python creates.
- [What is NumPy?](https://numpy.org/doc/stable/user/whatisnumpy.html) — why NumPy can be much faster than pure-Python numeric loops.
- [NumPy ufunc basics](https://numpy.org/doc/stable/user/basics.ufuncs.html) — vectorized operations.
- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — applying operations across arrays without manual loops.
- [Cython basic tutorial](https://cython.readthedocs.io/en/stable/src/tutorial/cython_tutorial.html) — start here if pure Python is too slow and NumPy is not enough.
- [Cython with NumPy](https://cython.readthedocs.io/en/stable/src/tutorial/numpy.html) — speeding up array-heavy code that can't be expressed cleanly with NumPy alone.
- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) — CPU-bound pure-Python work that needs multiple cores.
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — higher-level thread/process pool API.
- [`asyncio`](https://docs.python.org/3/library/asyncio.html) — high-concurrency I/O when dependencies are async-friendly.
