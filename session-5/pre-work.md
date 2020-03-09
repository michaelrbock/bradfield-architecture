# Session 5: A Brief Tour of Logic Circuits (Pre-Work)

## Truth Tables

| x | NOT |
|---|-----|
| 0 | 1 |
| 1 | 0 |

| x | y | AND |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

| x | y | NAND |
|---|---|------|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

| x | y | OR |
|---|---|----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

| x | y | NOR |
|---|---|-----|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

| x | y | XOR |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Circuit Diagrams

TODO: photo here.

## Adders

Full adder = two half adders.

TODO: image here of half and full adders.

* Each adder has:
    * Input: A, B, Carry In (connected from previous adder)
    * Output: Sum, Carry Out (connected to subsequent adder)

* The [video](https://www.youtube.com/watch?v=VBDoT8o4q00) shows a simple design of a multi-bit adder using a sequence of full adders, where the carry bit of one becomes an input to the next. Does this seem slower than it needs to be? Can you come up with a design that would be faster?
    * 
