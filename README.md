# HIT137 – Assignment 2  
**Group: DAN-EXT-13**

---

## OVERVIEW

This repository contains the complete solution for **HIT137 – Assignment 2**, implemented in Python.  
The assignment is divided into three questions, each focusing on different core programming and problem-solving concepts such as file handling, modular design, data processing, and analysis.

The solutions emphasise:
- Correct implementation of assignment requirements  
- Modular and maintainable program structure  
- Clear documentation and commenting  
- Inclusion of example inputs and outputs  

---

## GROUP CONTRIBUTION STATEMENT

This assignment was completed as a **group project**.  
All group members contributed **equally** to the design, implementation, testing, and documentation of the solutions.

Decisions regarding program structure, logic, and presentation were made collaboratively, and all members participated in reviewing and refining the final submission.

---

## GROUP MEMBERS

| Name | GitHub Username |
|-----|----------------|
| *Abhiman Bhattarai (S399284)* | `S399284-Abhiman` |
| *Antim (S397254)* | `Antim10` |
| *Samuel Jacob Reid (S386533)* | `sjreading` |
| *Zachary Desmond Mullen (S366010)* | `ZMullen2004` |

> **Note:** GitHub usernames differ from real names and are listed separately for clarity.



---

## QUESTION 1 – FILE ENCRYPTION AND DECRYPTION

### Description
This program implements a file-based encryption and decryption system using ASCII character manipulation and the rules provided in the assignment.

### Key Features
- Encrypts plaintext from a file
- Attempts safe decryption even when cipher collisions occur
- Verifies decrypted output against the original input
- Modular design separating logic and file handling

### Main Files
- `encryption.py` – Encryption logic  
- `decryption.py` – Decryption logic with ambiguity handling  
- `file.py` – File input/output  
- `main.py` – Program entry point  

### Additional Documentation
- `cipher_collision_analysis.md` explains why cipher collisions occur and how they affect reversibility.

---

## QUESTION 2 – TEMPERATURE DATA ANALYSIS

### Description
This program analyses Australian temperature data collected from multiple weather stations over several years.

### Tasks Performed
- Calculation of **seasonal average temperatures**
- Identification of station(s) with the **largest temperature range**
- Identification of **most stable** and **most variable** stations using standard deviation

### Technical Highlights
- Combines multiple CSV files into a single dataset
- Handles missing or invalid data safely
- Outputs results to text files using UTF-8 encoding to preserve special characters (e.g. `°C`)

### Main Files
- `data_utils.py` – CSV loading and preprocessing  
- `analysis.py` – All temperature analysis calculations  
- `config.py` – Constants and configuration  
- `main.py` – Program controller  

---

## QUESTION 3 – ADDITIONAL PROGRAMMING TASK

### Description
This question focuses on implementing the required logic as specified in the assignment instructions.  
Sample output is included to clearly demonstrate the expected behaviour of the program.

### Files Included
- `Main.py` – Core program implementation  
- `Example Output.md` – Sample output produced by the program  
- `README.md` – Explanation of the solution approach and logic
