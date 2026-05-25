# Miscellaneous Concepts

Stray notes that didn't fit anywhere larger but were worth keeping.

## Complex Numbers

Python has a built-in `complex` type and a `cmath` module for complex-number math:

```python
import cmath

input_text = '-2-5j'
complex_num = complex(input_text)
# complex_num.real, complex_num.imag

print(abs(complex_num))         # 5.385164807134504
print(cmath.phase(complex_num)) # -1.9513027039072615
```

- `abs(z)` returns the modulus (distance from origin).
- `cmath.phase(z)` returns the argument (angle in radians).
- The imaginary unit literal in Python is `j` (or `J`), not `i`.
