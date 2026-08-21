# DecodeLabs Python Programming Internship

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-unittest-brightgreen)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)
![License](https://img.shields.io/badge/license-MIT-informational)

A collection of command-line Python applications built during a software engineering internship at DecodeLabs, focused on core language fundamentals: data structures, file I/O, error handling, and test-driven verification — with no external frameworks or dependencies.

Each project is intentionally small in scope but built to production-quality standards: typed function signatures, docstrings throughout, defensive error handling, and an accompanying `unittest` suite.

---

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Skills Demonstrated](#skills-demonstrated)
- [Working With This Repository via Claude](#working-with-this-repository-via-claude)
- [About](#about)

---

## Overview

This repository contains four standalone CLI applications, each targeting a distinct set of core Python concepts:

| # | Project | Core Concepts |
|---|---------|----------------|
| 1 | [To-Do List](#1-to-do-list) | Lists, dictionaries, JSON serialization, persistent storage |
| 2 | [Expense Tracker](#2-expense-tracker) | Input validation, accumulator patterns, exception handling |
| 3 | [Password Generator](#3-password-generator) | Cryptographic randomness, entropy calculation, security standards |
| 4 | [Quiz Engine](#4-quiz-engine) | Control flow, string sanitization, data-driven design |

The goal across all four was the same: solve a well-defined problem cleanly, in plain Python, with code that's easy for another engineer to read, test, and extend.

---

## Projects

### 1. To-Do List
**File:** [`todo_app.py`](todo_app.py)

A CLI task manager that persists tasks to a local `tasks.json` file, so your list survives between runs. Separates data logic (`TaskModel`) from presentation (`display_tasks`), a small nod to separation-of-concerns design even in a script-sized project.

### 2. Expense Tracker
**File:** [`expense_tracker.py`](expense_tracker.py) · **Tests:** [`test_tracker.py`](test_tracker.py)

Accepts a running stream of expense entries, validates each as a whole number, and reports a running and final total. Demonstrates a clean accumulator pattern and graceful handling of malformed input without crashing the session.

### 3. Password Generator
**File:** [`password_generator.py`](password_generator.py) · **Tests:** [`test_password_generator.py`](test_password_generator.py)

Generates passwords using Python's `secrets` module — the cryptographically secure alternative to `random` — and calculates the resulting Shannon entropy so the strength of each password is quantifiable rather than assumed. Enforces NIST 2024 length guidance (15–64 characters).

### 4. Quiz Engine
**File:** [`quiz_engine.py`](quiz_engine.py)

A short general-knowledge quiz driven by a simple, data-first design: questions and answers live in a list of tuples rather than being hardcoded into control flow, making it trivial to extend with new questions.

---

## Project Structure

```
decodelabs-python-programming-internship/
├── todo_app.py                # Project 1: persistent to-do list
├── expense_tracker.py         # Project 2: expense accumulator
├── test_tracker.py            # Unit tests for expense_tracker.py
├── password_generator.py      # Project 3: secure password generator
├── test_password_generator.py # Unit tests for password_generator.py
├── quiz_engine.py             # Project 4: knowledge quiz
├── requirements.txt           # Dependency manifest (none required)
├── .gitignore
└── README.md
```

---

## Installation

Requires **Python 3.9+**. No third-party packages are needed — everything runs on the standard library.

```bash
git clone https://github.com/muhammadabdurrehmanmaqsood/decodelabs-python-programming-internship.git
cd decodelabs-python-programming-internship
```

That's it. There's nothing to `pip install`.

---

## Usage

Run any project directly with Python:

```bash
python todo_app.py
python expense_tracker.py
python password_generator.py
python quiz_engine.py
```

Each script runs an interactive command-line loop and prompts you for input.

---

## Testing

Unit tests are written with the standard library's `unittest` framework and cover core logic — input parsing, boundary conditions, and mathematical correctness (e.g. the entropy formula in the password generator).

```bash
python -m unittest discover -v
```

Or run an individual test file:

```bash
python -m unittest test_password_generator.py -v
python -m unittest test_tracker.py -v
```

---

## Skills Demonstrated

- **Language fundamentals** — lists, dictionaries, tuples, control flow, string manipulation
- **File I/O & serialization** — reading/writing JSON for persistent state
- **Error handling** — validating untrusted input and failing gracefully with `try`/`except`
- **Security awareness** — using `secrets` over `random` for cryptographic use cases; applying NIST password-length guidance
- **Testing discipline** — `unittest`-based coverage of edge cases, not just the happy path
- **Code quality** — PEP 8 formatting, type hints, and docstrings on every module, class, and function

---

## Working With This Repository via Claude

This repository's content is accessible through the **GitHub MCP (Model Context Protocol)** server, which means [Claude](https://www.anthropic.com/claude) can read, explain, and modify any file here directly.

If you're reviewing this project with Claude connected to GitHub MCP, you can ask it to:

- Walk through how a specific script works, function by function
- Explain the design decisions behind the `TaskModel` class or the entropy calculation
- Run or reason through the test suite
- Propose or make further changes to the codebase

This README itself — along with the PEP 8 cleanup, docstrings, and type hints across the codebase — was produced using Claude with GitHub MCP access to this repository.

---

## About

Built by **Muhammad Abdur Rehman Maqsood** as part of a Python programming internship at **DecodeLabs**, focused on writing clean, well-tested, dependency-free Python for real-world CLI tools.

- GitHub: [@muhammadabdurrehmanmaqsood](https://github.com/muhammadabdurrehmanmaqsood)
