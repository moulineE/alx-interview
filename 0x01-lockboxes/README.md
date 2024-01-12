# 0x01. Lockboxes
## Overview

This project focuses on solving a problem related to lockboxes. The goal is to implement a method that determines if all the boxes can be opened by exploring the relationships between boxes and their corresponding keys. The task involves working with a list of lists representing locked boxes and their associated keys.
## Project Details

    Author: Carrie Ybay, Software Engineer at Holberton School
    Weight: 1
    Start Date: Jan 8, 2024, 4:00 AM
    End Date: Jan 12, 2024, 4:00 AM
    Checker Released: Jan 9, 2024, 4:00 AM
    Auto Review: Will be launched at the deadline

## Requirements
### General

    Allowed Editors: vi, vim, emacs
    Interpreter/Compiler: Ubuntu 20.04 LTS using Python 3.4.3
    File Endings: All files should end with a new line.
    First Line: The first line of all files should be exactly #!/usr/bin/python3.
    README.md: A README.md file, at the root of the project folder, is mandatory.
    Documentation: Your code should be documented.
    PEP 8 Style: Your code should use the PEP 8 style (version 1.7.x).
    Executable Files: All your files must be executable.

## Tasks:
### Task 0: Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists.
    A key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.
    Return True if all boxes can be opened, else return False.
Example:
    
        carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
        #!/usr/bin/python3
        
        canUnlockAll = __import__('0-lockboxes').canUnlockAll
        
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # Output: True
        
        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        print(canUnlockAll(boxes))  # Output: True
        
        boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        print(canUnlockAll(boxes))  # Output: False
