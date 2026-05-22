# Advanced Language Features

## Topics

- [ ] Use generators correctly.
- [ ] Use decorators correctly.
- [ ] Use context managers correctly.
- [ ] Use metaclasses correctly.
- [ ] Use descriptors correctly.
- [ ] Know when **not** to use advanced features.
- [ ] Remember that restraint is a mark of expertise.

## Suggested learning order

1. Iterators and generators.
2. Context managers.
3. Decorators.
4. Descriptors.
5. Metaclasses.

Metaclasses should usually come last because most problems can be solved more clearly with normal classes, functions, decorators, descriptors, or `__init_subclass__`.

## References

- [Functional Programming HOWTO — iterators and generators](https://docs.python.org/3/howto/functional.html#generators) — iterators, generator expressions, and generator functions.
- [Yield expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions) — the precise language reference for `yield` and `yield from`.
- [Function definitions and decorators](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) — official syntax rules for decorators on functions.
- [PEP 318 — Decorators for Functions and Methods](https://peps.python.org/pep-0318/) — historical context for why decorator syntax exists.
- [`contextlib`](https://docs.python.org/3/library/contextlib.html) — practical tools for writing context managers with `with`.
- [The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) — exact execution rules for context managers.
- [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html) — best starting point for descriptors, properties, methods, `staticmethod`, and `classmethod`.
- [Customizing class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation) — metaclasses and class creation hooks.
- [PEP 20 — The Zen of Python](https://peps.python.org/pep-0020/) — restraint reminder. Advanced features should make code clearer or safer, not just clever.
