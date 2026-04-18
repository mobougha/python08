# Python Data Engineering Essentials

This document covers three fundamental concepts essential for professional Python data engineering and development, matching the curriculum of Python Module 08.

## 1. Virtual Environments

### What is a Virtual Environment?
A virtual environment is purely an isolated workspace for a Python project. It creates a self-contained directory tree that contains a specific Python installation for a particular version of Python, plus a number of additional packages.

### Why use Virtual Environments?
Without virtual environments, Python installs all packages globally on your system. If Project A requires `pandas==1.5.0` and Project B requires `pandas==2.2.0`, you will encounter a version conflict. Virtual environments solve this by giving each project its own isolated "global" space.

### How to use `venv`
The built-in Python module for creating virtual environments is `venv`.
- **Creation**: Run `python3 -m venv .venv` (where `.venv` is the name of the folder created).
- **Activation**: Run `source .venv/bin/activate` on MacOS/Linux. Your prompt will change to show `(.venv)`.
- **Deactivation**: Run `deactivate`.
- **Checking Active Env**: Check if you're in a venv by reading the environment variable `VIRTUAL_ENV` or examining `sys.prefix` versus `sys.base_prefix` in a python script.

## 2. Package Management

### What is Package Management?
It's the process of defining, installing, and updating the libraries (packages) your project needs to function correctly. 

### `pip`
`pip` is the default package installer for Python. It is simple but powerful. 
- You list dependencies in a `requirements.txt` file (e.g., `requests==2.31.0`).
- You install them by running: `pip install -r requirements.txt`.
- It handles the downloading and installation of packages into the active environment.

### `poetry`
`poetry` is a more modern, comprehensive tool for dependency management and packaging in Python. 
- It uses a structured file called `pyproject.toml`.
- Unlike `pip`, `poetry` automatically manages virtual environments for you and resolves complex dependency trees (ensuring dependencies of dependencies do not conflict).
- It also locks identical versions to a `poetry.lock` file so that any developer on a team installs the exact same packages.

## 3. Environment Variables

### What are Environment Variables?
Environment variables are dynamic values outside of your application that can affect the way running processes behave on a computer. In web development and software engineering, they are primarily used to store configuration data and sensitive secrets.

### Security and Best Practices
1. **Never Hardcode Secrets**: API keys, database passwords, and tokens should **never** be written directly into your source code.
2. **The `.env` File**: It is standard practice to store these secrets in a local file named `.env`.
3. **The `.gitignore` File**: To avoid accidentally uploading realistic secrets to GitHub, **you must ensure `.env` is listed inside a `.gitignore` file**.
4. **The `.env.example` File**: You should commit a template file named `.env.example` that shows what keys are required by the app, but with dummy/empty values.

### Development vs Production Configuration
Environment variables allow a single codebase to act differently depending on where it's running:
- **Development**: Running on your local machine. Your `.env` will likely have `DEBUG=True` and a `DATABASE_URL` pointing to a local SQLite or local PostgreSQL instance. This `.env` file is generated strictly for your local machine testing.
- **Production**: Running on the live server. The `.env` file does not exist here; instead, environment variables are set explicitly in the cloud provider's dashboard (e.g., AWS, Heroku) where `DEBUG=False` and `DATABASE_URL` points to the live production database. This prevents production data from ever touching your local environment.

### Using `python-dotenv`
The library `python-dotenv` allows Python to seamlessly read a `.env` file and ingest its contents as native environment variables.
```python
from dotenv import load_dotenv
import os

load_dotenv() # Loads the contents of the .env file

secret = os.getenv("API_KEY") # Retrieves the stored secret
print(secret)
```
