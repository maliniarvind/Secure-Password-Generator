# Project Statement: Secure Password Generator

## 1. Problem Definition
In the modern digital landscape, the security of user accounts heavily relies on the strength of passwords. However, human behavior often leads to the creation of weak, predictable passwords (e.g., "password123", names, or birthdates) that are vulnerable to brute-force and dictionary attacks. Users struggle to manually create and randomize complex character strings that meet high-security standards.

## 2. Proposed Solution
The **Secure Password Generator** is a Python-based software solution designed to eliminate the human error factor in credential creation. It automates the process of generating high-entropy strings, ensuring that every password created is mathematically random and difficult to crack.

## 3. Project Objectives
* **Automation:** To instantly generate passwords without manual effort.
* **Customization:** To allow users to tailor passwords based on specific requirements (Length, Uppercase, Digits, Symbols).
* **Reliability:** To ensure that if a specific character type is requested (e.g., symbols), it is guaranteed to appear in the final output.
* **Usability:** To provide a clear, error-free command-line interface that guides the user through the process.

## 4. Technical Scope
The project utilizes **Python 3** and adheres to modular software engineering principles:
* **Input Handling:** Robust validation loops to ensure user inputs are strictly 'Yes' or 'No', preventing runtime errors.
* **Algorithm:** distinct logic using the `random` and `string` libraries to handle character pool construction, random selection, and list shuffling.
* **Modularity:** The code is split into `main.py` (execution), `input_handler.py` (validation), and `password_logic.py` (generation) to demonstrate separation of concerns.

## 5. Intended Impact
This tool provides a lightweight, accessible utility for students, professionals, and general users to enhance their personal cybersecurity posture by generating cryptographically strong credentials on demand.
