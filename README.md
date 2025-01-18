# Collatz-Conjecture-Project

## Overview

The Collatz Conjecture is a mathematical sequence defined as follows : Start with any positive integer \( n \). Then each term is obtained from the previous term as follows:

- If the previous term is *even*, the next term is one half of the previous term.
- If the previous term is *odd*, the next term is 3 times the previous term plus 1.

The conjecture states that no matter what value of \( n \) you start with, you will always eventually reach 1.

This project explores the Collatz Conjecture with :
- **`collatz_conjecture.py`** : Calculates the sequence for a given number.
- **`collatz_csv.py`** : Plots the sequence using Matplotlib and pandas.


## Why This Matters
This project is a fun way to dive into the Collatz Conjecture and visualize how numbers behave under its rules. Feel free to experiment with different starting numbers!

## Requirements
- Python 3+
- Matplotlib
- Pandas

```bash
  pip install matplotlib
```
  
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.