# IT Help Desk

A Django-based IT Help Desk system for managing support tickets and IT service requests.

## Overview

This project provides a web-based platform for managing IT support tickets, service requests, and IT resource management.

## Requirements

- Python 3.12 or higher
- Django 5.2.3 or higher
- uv 0.7.13

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd IT_Help_Desk
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
```
**Using uv package manager**
```bash
uv venv # Using uv package manager
```
**Linux**
```bash
source .venv/bin/activate
```
**Windows**
```bash
.venv\Scripts\activate
```

3. Install Dependencies
```bash
uv pip install
```

## Running the Application

```bash
cd app
python manage.py runserver
```