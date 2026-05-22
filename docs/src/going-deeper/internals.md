# Python Internals

A roadmap for understanding what CPython is actually doing under the hood. Use these references as a study path, not a single read.

## Topics

- [ ] Understand the execution model: how Python runs code.
- [ ] Understand the GIL.
- [ ] Understand memory management.
- [ ] Understand reference counting.

## References

- [Python execution model](https://docs.python.org/3/reference/executionmodel.html) — code blocks, frames, scope, name resolution, exceptions, processes, threads, the runtime model.
- [Python data model](https://docs.python.org/3/reference/datamodel.html) — how objects, attributes, special methods, classes, and protocols fit together.
- [`dis` — Python bytecode disassembler](https://docs.python.org/3/library/dis.html) — see the bytecode Python compiles from your source.
- [CPython internals guide](https://devguide.python.org/internals/) — a map of deeper CPython implementation resources.
- [Memory Management — Python/C API](https://docs.python.org/3/c-api/memory.html) — Python's private heap and memory allocators.
- [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html) — the cyclic garbage collector API.
- [`sys.getrefcount`](https://docs.python.org/3/library/sys.html#sys.getrefcount) — useful for experiments. Treat results carefully — calling the function itself temporarily adds a reference.
- [GIL glossary entry](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) — short official definition.
- [Thread states and the global interpreter lock](https://docs.python.org/3/c-api/threads.html#thread-state-and-the-global-interpreter-lock) — deeper explanation of why CPython needs the GIL around Python objects.
- [PEP 703 — Making the GIL Optional](https://peps.python.org/pep-0703/) — modern context around free-threaded Python and why removing the GIL is hard.
