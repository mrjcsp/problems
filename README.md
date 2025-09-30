# AP CSP Problems 2025

This repository contains all of the **CS50 check files** for problems used in my AP Computer Science Principles class.  
Each folder is organized by problem and can be checked using the CS50 `check50` tool.  

---

## Running Checks

The format for running checks is: 

check50 mrjcsp/problems/2025/challenge

---

## Purpose

This repo is meant to keep all AP CSP problems in one place, using the `problems/2025` structure. It helps organize and run automated tests for each student submission during the course.

---

## Adding a New Problem

1. Create a new folder inside `2025/` with the name of the problem.  
   Example:  
---
2. Inside that folder, create a `.cs50.yaml` file.  
This file defines how check50 finds your checks.
A typical example looks like:
yaml
check50:
  files: [tests/leapyear.py]
---
3. Add your check files inside a tests/ directory within the problem folder.
Example:
problems/2025/leapyear/tests/leap_year.py
---
4. Run check50 using the format above to test the new problem.
