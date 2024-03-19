# 0x0F. Python - Object-relational mapping

## Description
This project focuses on linking two important worlds: Databases and Python. It involves using the `MySQLdb` module to connect to a MySQL database and execute SQL queries, as well as utilizing the `SQLAlchemy` module, which is an Object Relational Mapper (ORM). The key objective is to understand the abstraction of storage to usage facilitated by an ORM, thereby reducing the reliance on SQL queries and making Python code independent of storage type.

## Background Context
The project entails several tasks, each emphasizing different aspects of working with databases and Python:
- Connecting to a MySQL database from a Python script
- Executing SELECT and INSERT operations on MySQL tables using Python
- Understanding Object Relational Mapping (ORM) and its significance
- Mapping Python Classes to MySQL tables using SQLAlchemy
- Creating Python Virtual Environments for project dependencies management

## Requirements
- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- `pycodestyle` for code style enforcement
- Python Virtual Environment (venv) for dependency isolation

## Tasks
The project consists of several tasks, each focusing on specific objectives and skills development. Some of the key tasks include:
- Writing scripts to retrieve and manipulate data from MySQL databases
- Implementing SQL injection prevention techniques
- Defining SQLAlchemy models for database tables
- Performing CRUD (Create, Read, Update, Delete) operations using SQLAlchemy
- Handling database interactions securely and efficiently

## Learning Objectives
By the end of this project, the learner is expected to:
- Understand the fundamentals of connecting Python with MySQL databases
- Comprehend the role of Object Relational Mapping (ORM) in database interactions
- Gain proficiency in using SQLAlchemy for ORM in Python projects
- Acquire skills to perform CRUD operations on MySQL databases using Python
- Develop awareness of SQL injection vulnerabilities and prevention techniques

## Usage
To execute the scripts in this project, follow these steps:
1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd 0x0F-python-object_relational_mapping`
3. Run the desired Python script with appropriate arguments.
   Example: `./0-select_states.py root root hbtn_0e_0_usa`

## Credits
This project was developed by Guillaume at Holberton School as part of the Higher-Level Programming curriculum.

## Resources
- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/21/)
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/en/latest/index.html)
- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [10 Common Stumbling Blocks for SQLAlchemy Newbies](https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://overiq.com/sqlalchemy-101/)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

