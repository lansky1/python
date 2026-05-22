# Systems Thinking

## Topics

- [ ] Understand how Python code interacts with the OS.
- [ ] Understand how Python code interacts with the file system.
- [ ] Understand how Python code interacts with the network.
- [ ] Understand how Python code interacts with memory.

## Main ideas

- Files, sockets, subprocesses, and locks are external resources. Clean them up explicitly, usually with `with`.
- Text and bytes are different. Always know the encoding boundary.
- The OS can fail any operation: files can disappear, permissions can be denied, networks can time out, and subprocesses can exit badly.
- A Python process has memory, open files, environment variables, signals, threads, and child processes. Good programs account for those boundaries.

## References

- [`os`](https://docs.python.org/3/library/os.html) — environment variables, process info, file descriptors, permissions, paths, OS-level behavior.
- [`pathlib`](https://docs.python.org/3/library/pathlib.html) — modern object-oriented path handling. Prefer this for most path code.
- [`io`](https://docs.python.org/3/library/io.html) — text I/O, binary I/O, buffering, encodings, file-like objects.
- [`tempfile`](https://docs.python.org/3/library/tempfile.html) — safe temporary files and directories.
- [`subprocess`](https://docs.python.org/3/library/subprocess.html) — running external programs and understanding process boundaries.
- [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html) — low-level networking concepts.
- [`socket`](https://docs.python.org/3/library/socket.html) — exact API for network sockets.
- [`mmap`](https://docs.python.org/3/library/mmap.html) — memory-mapped files. Read after normal file I/O is comfortable.
- [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html) — practical memory allocation tracing.
