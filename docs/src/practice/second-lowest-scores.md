# Second Lowest Scores

Given a list of `[name, score]` records, find every name whose score is the **second lowest**, then print them alphabetically.

```python
records = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39],
]

records.sort(key=lambda x: x[1])
records = list(filter(lambda x: x[1] != records[0][1], records))   # drop the lowest
records = list(filter(lambda x: x[1] == records[0][1], records))   # keep only the new lowest
records.sort(key=lambda x: x[0])                                   # alphabetical
print(records)
```

Walkthrough:

1. Sort by score (ascending).
2. Drop everyone tied with the absolute minimum — what remains starts at the second-lowest score.
3. Keep only those tied with the new minimum.
4. Sort alphabetically and print.
