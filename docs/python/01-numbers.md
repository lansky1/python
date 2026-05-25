# Numbers

> **Batteries Included Philosophy**: [PEP 206](https://peps.python.org/pep-0206/)

## Division

- `/` always performs floating-point division.
- `//` performs integer (floor) division.

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

## Floating Point Arithmetic

Why doesn't `0.1 + 0.2 - 0.3` equal `0.0`? Because binary floating point cannot represent most decimal fractions exactly.

Reference: [Floating Point Arithmetic — Python tutorial](https://docs.python.org/3/tutorial/floatingpoint.html)

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 - 0.3)  # 5.551115123125783e-17
```

## Exponentiation & Bitwise Operations

- `**` is the exponentiation operator.
- `^` is bitwise XOR — e.g. `001 ^ 110 = 111`.

```python
print(6 ** 6)  # 46656
print(1 ^ 6)   # 7  (binary: 001 XOR 110 = 111)
```

`pow()` extends `**` with an optional modulus argument for fast modular exponentiation:

```python
pow(2, 5)     # 32
pow(2, 4, 5)  # 1     —  same as (2**4) % 5
```

## Bases

```python
hex(12)    # '0xc'
hex(512)   # '0x200'
bin(128)   # '0b10000000'
```

## Float Formatting

Format spec: `{value:width.precision f}`

```python
print("The answer is {:1.1f}".format(100/77))  # The answer is 1.3
```

## Banker's Rounding

Python uses **banker's rounding** (round half to even) to reduce bias over many operations.

```python
print(round(4.5))  # 4 — rounds to nearest even
print(round(5.5))  # 6 — rounds to nearest even

round(3.1)         # 3
round(3.14159, 2)  # 3.14
```

`abs()` returns the unsigned distance from zero:

```python
abs(-2)  # 2
```

## Integer Size

Unlike C++ or C#, Python has **no fixed size constraints** on integers:

- Integers grow arbitrarily large, limited only by available memory.
- Python automatically handles the underlying representation.
- No overflow errors.
