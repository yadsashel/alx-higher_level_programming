# 0x11. Python - Network #1

## Project Overview

This project focuses on using Python to interact with network resources. The primary goal is to understand how to fetch internet resources, handle different types of HTTP requests, and manage response data using both the `urllib` and `requests` packages.

## Learning Objectives

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests`
- How to make HTTP GET requests
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation
- Use `get` to access dictionary values by key to avoid exceptions if the key doesn't exist
- Code should not be executed when imported (use `if __name__ == "__main__":`)

## Tasks

### Task 0: What's my status? #0

**Objective:**  
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib`.

### Task 1: Response header value #0

**Objective:**  
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.

### Task 2: POST an email #0

**Objective:**  
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`).

### Task 3: Error code #0

**Objective:**  
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in `utf-8`). Manage `urllib.error.HTTPError` exceptions and print `Error code:` followed by the HTTP status code.

### Task 4: What's my status? #1

**Objective:**  
Write a Python script that fetches `https://alx-intranet.hbtn.io/status` using `requests`.

### Task 5: Response header value #1

**Objective:**  
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable `X-Request-Id` in the response header using `requests`.

### Task 6: POST an email #1

**Objective:**  
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response using `requests`.

### Task 7: Error code #1

**Objective:**  
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, print `Error code:` followed by the value of the HTTP status code using `requests`.
