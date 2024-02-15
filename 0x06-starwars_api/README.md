# 0x06. Star Wars API

## Overview
This project is part of the curriculum at Holberton School and is designed to familiarize students with interacting with external APIs using JavaScript. The task involves fetching and displaying information about Star Wars characters based on the movie ID provided as an argument.

## Project Details
- **Project Name:** Star Wars Characters
- **Weight:** 1
- **Start Date:** February 12, 2024, 4:00 AM
- **Deadline:** February 16, 2024, 4:00 AM
- **Checker Release Date:** February 13, 2024, 4:00 AM
- **Auto Review:** Will be launched at the deadline

## Project Description
The goal of this project is to interact with an external API, specifically the Star Wars API, to retrieve and display character information from a particular Star Wars movie. This requires knowledge of HTTP requests, API interaction, and asynchronous programming in JavaScript.

### Concepts Needed
1. **HTTP Requests in JavaScript:** Understanding how to make HTTP requests using modules like `request` or `fetch` in Node.js.
2. **Working with APIs:** Basic understanding of RESTful APIs, parsing JSON data, and interacting with APIs in JavaScript.
3. **Asynchronous Programming:** Managing asynchronous operations using callbacks, promises, and async/await syntax.
4. **Command Line Arguments in Node.js:** Parsing command-line arguments passed to a Node.js script using `process.argv`.
5. **Array Manipulation and Iteration:** Iterating over arrays and manipulating data structures to format and display character names.

By mastering these concepts, students will be able to effectively retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API.

## Requirements
- **Allowed Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- **File Endings:** All files should end with a new line
- **File Headers:** The first line of all files should be `#!/usr/bin/node`
- **README:** A `README.md` file at the root of the project folder is mandatory
- **Code Style:** Code should be semistandard compliant with semicolons and follow the AirBnB style guide
- **Executable Files:** All files must be executable
- **File Length:** The length of files will be tested using `wc`
- **No `var` Keyword:** `var` keyword is not allowed
- **Node.js Version:** Install Node 10.x
- **Semi-standard Installation:** Install semi-standard globally using `npm`
- **Request Module:** Install and use the `request` module for making HTTP requests

## Additional Resources
- Mock Technical Interview

## Tasks
### 0. Star Wars Characters
- **Description:** Write a script that prints all characters of a Star Wars movie.
- **Requirements:**
  - The first positional argument passed is the Movie ID (e.g., 3 for "Return of the Jedi").
  - Display one character name per line in the same order as the “characters” list in the `/films/` endpoint.
  - Utilize the Star Wars API and the `request` module.
- **Example:**
  ```
  $ ./0-starwars_characters.js 3
  Luke Skywalker
  C-3PO
  R2-D2
  Darth Vader
  Leia Organa
  Obi-Wan Kenobi
  Chewbacca
  Han Solo
  Jabba Desilijic Tiure
  Wedge Antilles
  Yoda
  Palpatine
  Boba Fett
  Lando Calrissian
  Ackbar
  Mon Mothma
  Arvel Crynyd
  Wicket Systri Warrick
  Nien Nunb
  Bib Fortuna
  ```

## Repository Details
- **GitHub Repository:** [alx-interview](https://github.com/moulineE/alx-interview)
- **Directory:** 0x06-starwars_api
- **File:** 0-starwars_characters.js
