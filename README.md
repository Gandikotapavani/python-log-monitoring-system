# Python Log Monitoring and Alert Management System

## Overview
A Python-based system to monitor server logs, detect errors,
warnings and failed login attempts, and generate alerts.

## Features
- Log parsing using Python
- ERROR and WARNING detection
- Failed login detection
- Alert generation
- SQLite database storage
- Flask web dashboard
- Duplicate log prevention
- Pytest unit testing

## Technologies
Python, Flask, SQLite, Pytest, HTML, CSS, Linux, Git, GitHub.

## Run Instructions

1. Create virtual environment:
   python3 -m venv venv

2. Activate:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Monitor logs:
   python3 alert_manager.py

5. Start dashboard:
   python3 app.py

6. Run tests:
   python3 -m pytest -v

## Author
Pavani Gandikota
