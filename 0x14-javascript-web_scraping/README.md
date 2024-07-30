# 0x14. JavaScript - Web Scraping

## Description
This project involves using JavaScript for web scraping, accessing JSON data, and manipulating it. You will learn how to make HTTP requests, handle JSON data, and use modern JavaScript features.

## Learning Objectives
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and `fetch` API
- How to read and write a file using `fs` module

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should be `semistandard` compliant
- All files must be executable
- You are not allowed to use `var`

## Installations
### Install Node 14
```bash
sudo apt-get update
sudo apt-get install -y nodejs
```

### Install semi-standard
```bash
Copy code
npm install -g semistandard
```
### Install request module
```bash
Copy code
npm install request
```
## Tasks

### Task 0: Readme
Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurs during the reading, print the error object

### Task 1: Write me
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8

### Task 2: Status code
Write a script that displays the status code of a GET request.

The first argument is the URL to request
The status code must be printed like this: code: <status code>

### Task 3: Star Wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
Use the Star Wars API: https://swapi-api.alx-tools.com/api/films/:id
### Task 4: Star Wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/
Use character ID 18 for filtering
### Task 5: Loripsum
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument is the file path to store the body response
The file must be UTF-8 encoded
### Task 6: How many completed?
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed tasks

## Author
Yazide Salhi - yadsashel
