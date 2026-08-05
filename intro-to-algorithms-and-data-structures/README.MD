# Introduction to Algorithms and Data Structures (IAED)

Course at Instituto Superior Técnico covering imperative programming in C, algorithm
efficiency analysis, and classic data structures.

Covers elementary and advanced sorting algorithms (insertion sort, selection sort,
bubble sort, quicksort, merge sort, heapsort), data structures (stacks, queues,
priority queues, heaps, trees) with both array and dynamic implementations, binary
search trees, balanced search trees, and hash tables (collision resolution via
chaining and open addressing).

## Project: Product Invoicing System

A command-line invoicing system written in C, supporting product registration,
shopping cart management, invoicing, and reporting.

### What it does
- Parses single-letter commands from standard input (`p`, `l`, `a`, `r`, `f`, `c`, `d`,
  `q`) to add/list products, manage a shopping cart, issue invoices, generate sales
  summaries, and delete products or invoices.
- Validates and computes EAN-8/EAN-13 barcode check digits.
- Applies configurable VAT rates (loaded from a file or defaulting to a fixed table)
  with symmetric rounding to the cent.
- Uses only dynamic memory allocation (no global variables, no fixed-size arrays for
  unbounded data) to support up to 10,000 products and an unlimited number of
  invoices/customers.
- Handles wildcard product lookups (`*` and `?`) and quoted customer names containing
  whitespace.

### Notes
Split into modules: `project.c` handles product registration, the shopping cart,
and command parsing; `invoice.h`/`invoice.c` implements the invoice list as a
self-contained linked-list module with its own create/add/find/remove/free
operations. Built with strict constraints: no `goto`, no `extern`, no built-in
`qsort`, and limited to `stdio.h`, `stdlib.h`, `ctype.h`, and `string.h`. Compiled
with `-O3 -Wall -Wextra -Werror`, and checked with valgrind for memory leaks.
