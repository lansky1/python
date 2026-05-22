# Numbers & Arithmetic

## Division

- `/` always performs floating-point division
- `//` performs integer (floor) division

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

## Floating Point Arithmetic

Why doesn't `0.1 + 0.2 - 0.3` equal `0.0`?

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 - 0.3)  # 5.551115123125783e-17
```

Reference: [Floating Point Arithmetic — Python docs](https://docs.python.org/3/tutorial/floatingpoint.html).

## Exponentiation & Bitwise

- `**` — exponentiation
- `^` — bitwise XOR

```python
print(6 ** 6)  # 46656
print(1 ^ 6)   # 7  (binary: 001 XOR 110 = 111)
```

## Float Formatting

Format spec: `{value:width.precision f}`

```python
print("The answer is {:1.1f}".format(100/77))
```

## Banker's Rounding

Python uses **banker's rounding** (round half to even) to reduce bias over many operations.

```python
print(round(4.5))  # 4 — rounds to nearest even
print(round(5.5))  # 6 — rounds to nearest even
```

## The `math` module

| Function | Description |
|---|---|
| `math.floor(x)` | Round down |
| `math.ceil(x)` | Round up |
| `round(x)` | Banker's rounding |
| `math.pi` | π constant |
| `math.e` | Euler's number |
| `math.inf` | Positive infinity |
| `math.nan` | Not a Number |
| `math.log(math.e)` | Natural log → 1.0 |
| `math.sin(x)` | Sine (x in radians) |
| `math.degrees(x)` / `math.radians(x)` | Convert between degrees and radians |

## The `random` module

References: [Pseudorandom number generator](https://en.wikipedia.org/wiki/Pseudorandom_number_generator), [Random seed](https://en.wikipedia.org/wiki/Random_seed).

| Function | Description |
|---|---|
| `random.seed(42)` | Set seed for reproducibility |
| `random.randint(a, b)` | Random integer in `[a, b]` |
| `random.choice(seq)` | Pick one random element |
| `random.choices(population, k=n)` | Pick n elements **with** replacement |
| `random.sample(population, k=n)` | Pick n elements **without** replacement |
| `random.shuffle(list)` | Shuffle in place |
| `random.uniform(a, b)` | Random float in `[a, b]` |
| `random.gauss(mu, sigma)` | Normal distribution sample |

## Useful built-ins for numbers

- `abs()` — positive distance from zero
- `round()` — banker's rounding
- `divmod(a, b)` — `(quotient, remainder)` together
- `pow(base, exp[, mod])` — exponentiation; three-arg form does modular exponentiation
- `chr(n)` / `ord(c)` — convert between Unicode code point and character
