# Library Management System

## Introduction

This Library Management System is a Python-based project designed to streamline library operations, such as borrowing and returning books, and maintaining an up-to-date inventory. It automates essential tasks, minimizes errors, and efficiently tracks borrower details, book availability, and overdue fees.

The system maintains records of:
- Borrowers and their transaction history.
- Book inventory, including stock updates upon borrowing or returning.
- Issuance and return notes with borrower details, date/time, and any applicable fees.

The system aims to simplify library management, making it accessible to users with minimal technical expertise.

---

## Features
1. **Book Inventory Management**: Displays available books and updates stock upon transactions.
2. **Borrowing Books**:
   - Records borrower's name and book details.
   - Automatically deducts stock and calculates borrowing costs.
3. **Returning Books**:
   - Updates inventory upon book returns.
   - Calculates overdue charges for late returns (loan period is 10 days).
4. **Transaction Records**:
   - Maintains a log of all borrow and return transactions.
5. **User-Friendly Interface**:
   - Simple menu-driven options for borrowing, returning, and viewing books.
   - Clear error handling and guidance for users.



## Goals and Objectives
- Develop a reliable and efficient Library Management System using Python.
- Enhance understanding of file handling, data structures, and modular programming.
- Automate invoice creation for borrowed and returned books.
- Ensure accurate tracking of stock and user transactions.



## Prerequisites
### Software and Tools:
1. **Python**: Programming language for the system.
2. **Sublime Text 3 / PyCharm**: Code editors used for development.
3. **Draw.io**: For designing flowcharts and diagrams.



## How to Run
1. Clone or download the project repository.
2. Ensure Python is installed on your system.
3. Place the `books.txt` file in the root directory of the project. This file should contain the initial book inventory in the format:
   ```
   BookName,Author,Quantity,Price
   ```
4. Run the main script:
   ```bash
   python main.py
   ```
5. Follow the on-screen instructions to:
   - Borrow books.
   - Return books.
   - Exit the system.

---

## File Structure
- **main.py**: Entry point for the program. Displays the main menu and routes to borrow/return functions.
- **borrow.py**: Handles the book borrowing process and updates inventory.
- **return.py**: Manages book returns, calculates overdue charges, and updates inventory.
- **read.py**: Displays the current inventory of books from `books.txt`.
- **books.txt**: Stores book inventory details.
- **Borrow_.txt**: Logs borrowing transactions.
- **Return.txt**: Logs return transactions.

---

## Sample Workflow
### Borrowing Books:
1. Choose the "Borrow Book" option from the menu.
2. Enter your name, book ID, and quantity.
3. The system:
   - Checks stock availability.
   - Updates inventory.
   - Generates a note with details such as book name, cost, and timestamp.

### Returning Books:
1. Choose the "Return Book" option.
2. Enter your name, book ID, and quantity.
3. The system:
   - Updates stock.
   - Calculates overdue charges if applicable.
   - Generates a return note with details.

---

## Algorithm Overview
1. Display the main menu with options:
   - Borrow Book.
   - Return Book.
   - Exit.
2. For borrowing:
   - Check stock availability.
   - Deduct quantity from inventory.
   - Log transaction details in `Borrow_.txt`.
3. For returning:
   - Update stock.
   - Calculate late fees if applicable.
   - Log return details in `Return.txt`.


## Pseudocode
### Main Function:
```python
Display menu options.
While the user does not exit:
    If the user selects 'Borrow Book':
        Call borrow() function.
    If the user selects 'Return Book':
        Call return() function.
    If the user selects 'Exit':
        Terminate the program.
```

---

## Future Enhancements
1. Implement a database for better scalability.
2. Add a graphical user interface (GUI) for improved usability.
3. Enable multi-user support with login credentials.
4. Introduce advanced reporting features for administrators.

---

## Author
**Gaurab Khadka**

This project was developed as part of the CS4051NI Fundamentals of Computing course.

Feel free to contribute to the project or provide feedback for improvement.
