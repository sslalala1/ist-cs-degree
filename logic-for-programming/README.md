# Logic for Programming (Lógica para Programação)

Course at Instituto Superior Técnico covering formal logic and logic
programming, using Prolog.

Covers propositions and arguments, propositional logic (deductive system and
semantics), first-order logic (deductive system and semantics), soundness and
completeness, resolution, and logic programming.

## Project: Star Battle Solver

Prolog program that solves "Star Battle" puzzles: an NxN grid divided into regions,
where the goal is to place exactly two stars in every row, column, and region, with
no two stars adjacent (including diagonally).

### What it does
- Represents the board as a list of lists (unbound variables for empty cells) and
  a separate, read-only region structure.
- Implements insertion/query predicates to place stars and points and inspect the
  board (e.g. `insereObjecto`, `objectosEmCoordenadas`, `coordObjectos`).
- Implements two solving strategies:
  - **Closing lines** — fills in the rest of a row/column/region once it already
    has its two stars, or narrows down the last remaining star(s) when only one
    or two free spaces are left.
  - **Pattern matching** — finds sequences of empty cells within a line and
    applies known patterns (the "I" pattern for 3-cell sequences, the "T" pattern
    for 4-cell sequences) to deduce star placement.
- Combines both strategies in `resolve/2`, applying them repeatedly until the
  board stops changing — solving many (though not all) puzzles completely without
  brute-force search.

### Notes
Written in SWI-Prolog, using logic programming and unification rather than
imperative state changes.
