# Learnings

- No need to manually return true or false when the condition already produces a boolean result. Return the boolean result directly.
- Slicing works on strings and arrays/lists using `value[start:stop:step]`.
  - `value[:]` means the complete value.
  - `value[start:]` means start from `start` and continue to the end.
  - `value[:stop]` means start from the beginning and stop before `stop`.
  - `value[start:stop]` means take the part from `start` up to, but not including, `stop`.
  - `value[::step]` means take items by skipping according to `step`.
  - `value[::-1]` means traverse in reverse.
  - Negative indexes count from the end, so they are useful for last items or slicing from the back.
  - Slicing is safe when the value is shorter than expected, so separate length checks are often unnecessary.
