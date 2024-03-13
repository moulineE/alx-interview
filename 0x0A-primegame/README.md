# Prime Game

## Overview
This project involves solving a competitive game scenario where players strategically remove prime numbers and their multiples from a set of consecutive integers. The goal is to determine the winner of the game based on optimal play.

**Project Name:** 0x0A. Prime Game  
**By:** Carrie Ybay, Software Engineer at Holberton School  
**Weight:** 1  
**Start Date:** Mar 11, 2024 3:00 AM  
**End Date:** Mar 15, 2024 3:00 AM  
**Checker Release Date:** Mar 12, 2024 3:00 AM  
**Auto Review Launch:** An auto review will be launched at the deadline  

## Objective
The primary objective of this project is to leverage knowledge in prime numbers, game theory, and algorithm optimization to determine the winner of the game. Players take turns choosing prime numbers from a set and removing them along with their multiples. The player unable to make a move loses the game.

## Concepts Needed
1. **Prime Numbers:**
   - Understanding prime numbers.
   - Efficient algorithms for identifying prime numbers within a range.
2. **Sieve of Eratosthenes:**
   - An efficient algorithm for finding all prime numbers up to any given limit.
3. **Game Theory:**
   - Basic principles of competitive games.
   - Optimal play strategies and win conditions.
4. **Dynamic Programming/Memoization:**
   - Using previous results to speed up future calculations.
5. **Python Programming:**
   - Implementing game logic and algorithms using loops, conditional statements, arrays, and lists.

## Resources
- **Prime Numbers and Sieve of Eratosthenes:**
  - [Khan Academy: Prime Numbers](https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/what-are-prime-numbers)
  - [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/)
- **Game Theory Basics:**
  - [Game Theory Introduction](https://www.investopedia.com/terms/g/game-theory.asp)
- **Dynamic Programming:**
  - [What Is Dynamic Programming With Python Examples](https://realpython.com/python-thinking-recursively/)
- **Python Official Documentation:**
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

## Instructions
1. **General:**
   - Allowed editors: vi, vim, emacs.
   - Files interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.4.3).
   - All files should end with a new line.
   - The first line of all files should be exactly `#!/usr/bin/python3`.
   - A `README.md` file at the root of the project folder is mandatory.
   - Code should use the PEP 8 style (version 1.7.x).
   - All files must be executable.
2. **Tasks:**
   - **Task 0: Prime Game**
     - Prototype: `def isWinner(x, nums)`
     - Return: name of the player that won the most rounds
     - If the winner cannot be determined, return None
     - Constraints: `n` and `x` will not exceed 10000
     - No importing packages allowed
     - Refer to project specification for detailed task description.

## Additional Resources
- Mock Technical Interview

## Repository Information
- **GitHub Repository:** [alx-interview](https://github.com/moulineE/alx-interview)
- **Directory:** 0x0A-primegame
- **File:** 0-prime_game.py
