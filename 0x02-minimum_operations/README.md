# 0x02. Minimum Operations

## Project Description

This project, part of the curriculum at ALX, involves solving the "Minimum Operations" problem using Python. The task is to determine the fewest number of operations needed to achieve a specific number of 'H' characters in a text file, given that the only allowed operations are Copy All and Paste.

## Project Details

- **Author:** Carrie Ybay, Software Engineer at Holberton School
- **Weight:** 1
- **Start Date:** January 15, 2024, 4:00 AM
- **End Date:** January 19, 2024, 4:00 AM
- **Checker Release Date:** January 16, 2024, 4:00 AM
- **Auto Review:** Will be launched at the deadline

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Interpreter/Compiler:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings:** All files should end with a new line
- **First Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README:** A README.md file at the root of the project folder is mandatory
- **Documentation:** Code should be well-documented
- **Style Guide:** Code should follow the PEP 8 style (version 1.7.x)
- **Executable Files:** All files must be executable

## Tasks

### 0. Minimum Operations

- **Description:** In a text file, there is a single character 'H'. The text editor can execute only two operations: Copy All and Paste. Given a number `n`, the task is to write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

- **Prototype:** `def minOperations(n)`

- **Returns:** An integer. If `n` is impossible to achieve, return 0.

#### Example

```python
n = 9

# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
```

## Usage

To test the implementation, use the provided `0-main.py` script:

```bash
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Repository Information

- **GitHub Repository:** [alx-interview](https://github.com/username/alx-interview)
- **Directory:** 0x02-minimum_operations
- **File:** 0-minoperations.py

