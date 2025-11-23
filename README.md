# Secure Password Generator
## ⚪  Project Description
This is a Python-based command-line application designed to generate strong, secure passwords. The application allows users to customize the password generation process by selecting specific criteria such as length and character types (uppercase, lowercase, numbers, and symbols).

The project is structured using a **modular approach** to ensure code readability, maintainability, and separation of concerns.

---

## ⚪  Project Structure
The codebase is divided into three distinct modules:

1.  **`main.py`** The entry point of the application. It orchestrates the flow between getting user input and generating the password.

2.  **`input_handler.py`** Handles all user interactions regarding validation. It ensures that users provide valid "Yes/No" (Y/N) inputs, preventing the program from accepting invalid keystrokes.

3.  **`password_logic.py`** Contains the core algorithms for password generation. It handles the random selection of characters and ensures that all selected criteria are met (e.g., guaranteeing at least one symbol if symbols are requested).

### ⚪ Directories
* **`screenshots/`**: Contains images of the application running.
* **`recordings/`**: Contains screen recordings of the project execution.

---

## ⚪ How to Run the Project

### ⚪ Prerequisites
* Python 3.13 installed on your system.

### ⚪ Execution Steps
1.  Clone this repository or download the source code.
2.  Open your terminal (Command Prompt/PowerShell/Bash).
3.  Navigate to the project directory.
4.  Run the main script using the following command:
## Screenshots
<img width="368" height="269" alt="Screenshot 2025-11-23 174058" src="https://github.com/user-attachments/assets/fd31c50d-efa0-4b58-a508-abd985d86773" />
<img width="395" height="373" alt="Screenshot 2025-11-23 183105" src="https://github.com/user-attachments/assets/179e8bb0-ffc2-46da-a5ea-28c92bd8fce4" />
<img width="547" height="217" alt="Screenshot 2025-11-23 183731" src="https://github.com/user-attachments/assets/c728dfb1-f9b9-4ba8-8687-4575ef1c32c5" />




```bash
python main.py
