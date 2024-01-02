# 0x00. Pascal's Triangle

## Project Description

This project involves implementing a Python function to generate Pascal's Triangle and includes automated testing using a provided main file.

## Project Details

- **Author:** Alexa Orrico, Software Engineer at Holberton School
- **Project Start Date:** January 2, 2024, 4:00 AM
- **Project End Date:** January 5, 2024, 4:00 AM
- **Checker Release Date:** January 2, 2024, 10:00 PM
- **Auto Review Deadline:** January 5, 2024, 4:00 AM
- **Weight:** 1

## Project Tasks

### Task 0: Pascal's Triangle

**Description:**
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`.
- You can assume `n` will always be an integer.

### Example

```python
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

Output:
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```