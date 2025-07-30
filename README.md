# 🔐 Python Password Strength Checker
A python command-line tool that checks the strength of a password and classfies it as Weak, Moderate or Strong, developed as part of my cybersecurity studies. 

## 🎯 Project Overview
This tool demonstrates an understanding of:
- String handling and character analysis
- Conditional logic and loops
- Input validation techniques

## ✨ Features
- ✅ Accepts user input securely via CLI
- ✅ Evaluates password strength based on length, character types, and complexity
- ✅ Real-time feedback with helpful rating messages
- ✅ Custom scoring logic for password classification

## 🚀 Usage
### Run the program:
```bash
python main.py
```
### Example session:
```bash
Enter your password: Sunshine1!
Password strength score: 5
Strong
```
## 📋 Password Evaluation Logic
The program checks:
- ✅ Password length
- ✅ Use of uppercase and lowercase letters
- ✅ Presence of numbers
- ✅ Special characters
- ❌ No leading/trailing spaces
- ❌ No accented or non-ASCII characters

## 🧠 Program Logic
Password Strength Checker Flow:
1. Accept password input
2. Validate the format
3. Score based on character types
4. Display a rating: Weak / Moderate / Strong

## 📸 Screenshots
<img width="969" height="173" alt="image" src="https://github.com/user-attachments/assets/c4dcb851-c25b-48b8-839a-1a41ecc46e8d" />

## 🔮 Future Enhancements
- Add real-time GUI version with Tkinter
- Show score breakdown (e.g., “+1 for uppercase, +1 for numbers”)
- Integrate password hashing for secure storage examples
- Export password ratings to a log file
- Add password generation functionality
- Implement dictionary word checks for weak password detection

## 🙏 Acknowledgments
Developed as part of my Python learning journey.
Inspired by real-world password security concerns and the importance of strong credential practices.

##  📝 License
This project is open for learning and personal portfolio use.
Developed by Kelly Lindsay – Cybersecurity Student
