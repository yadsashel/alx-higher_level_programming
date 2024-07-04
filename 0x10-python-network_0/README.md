Certainly! Here’s a properly formatted and decorated `README.md` for your project:

---

# 0x10. Python - Network #0

**Author:** <Yazide Salhi>

---

## Project Overview

This project focuses on using cURL to interact with web servers and understanding HTTP methods. Additionally, it includes a Python task to find a peak in a list of unsorted integers.

---

## Objectives

- Understand the HTTP request/response cycle.
- Use cURL to send HTTP requests.
- Differentiate between various HTTP methods.
- Implement a simple algorithm to find a peak in a list of unsorted integers.

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3
- cURL

---

## Tasks

### Task 0: cURL body size

**Objective:**
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

**Instructions:**
1. Create a script named `0-body_size.sh`.
2. The script should:
   - Take in a URL.
   - Send a request to the URL.
   - Display the size of the body of the response.

### Task 1: cURL to the end

**Objective:**
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.

**Instructions:**
1. Create a script named `1-body.sh`.
2. The script should:
   - Take in a URL.
   - Send a GET request to the URL.
   - Display the body of the response.

### Task 2: cURL Method

**Objective:**
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

**Instructions:**
1. Create a script named `2-delete.sh`.
2. The script should:
   - Send a DELETE request to the URL passed as the first argument.
   - Display the body of the response.

### Task 3: cURL only methods

**Objective:**
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

**Instructions:**
1. Create a script named `3-methods.sh`.
2. The script should:
   - Take in a URL.
   - Display all HTTP methods the server will accept.

### Task 4: cURL headers

**Objective:**
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`.

**Instructions:**
1. Create a script named `4-header.sh`.
2. The script should:
   - Take in a URL as an argument.
   - Send a GET request to the URL.
   - Display the body of the response.
   - Include a header variable `X-HolbertonSchool-User-Id` with the value `98`.

### Task 5: cURL POST parameters

**Objective:**
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.

**Instructions:**
1. Create a script named `5-post_params.sh`.
2. The script should:
   - Take in a URL.
   - Send a POST request to the URL.
   - Display the body of the response.
   - Include the POST parameters:
     - `email=test@gmail.com`
     - `subject=I will always be here for PLD`

### Task 6: Find a peak

**Objective:**
Write a function that finds a peak in a list of unsorted integers.

**Instructions:**
1. Create a file named `6-peak.py`.
2. The function should:
   - Be named `find_peak`.
   - Take a list of integers as an argument.
   - Return a peak element in the list.

---

## Usage

To run the Bash scripts, use the following command:

```bash
./<script_name>.sh <URL>
```

To test the Python function, you can use the following command:

```python
python3 -m doctest <script_name>.py
```

---
