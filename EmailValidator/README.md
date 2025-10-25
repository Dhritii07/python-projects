# 📧 Email Validation Script  

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

A simple yet enhanced **Email Validation Tool** built with Python 🐍.  
It validates email addresses, extracts username & domain parts, and warns users about uncommon or invalid domains.

---

## ✨ Features  

✅ Validates email format using **regular expressions (regex)**  
✅ Extracts **username** and **domain** from valid emails  
✅ Detects **uncommon domains** and **invalid TLDs**  
✅ Provides user-friendly warnings and clear output  
✅ Lightweight — **no external libraries required**

---

## 🧠 How It Works  

1. The program takes an email as input.  
2. It checks if the email format matches a valid **regex pattern**.  
3. It verifies the **domain** against common email providers.  
4. It checks if the **TLD** (like `.com`, `.org`, `.io`) is valid.  
5. If valid, it splits and displays the **username** and **domain** parts.

---

## 💻 Example Usage  

```bash
$ python EmailValidation.py
Enter your email id - user@example.comm
Warning: The domain 'example.comm' is uncommon. Please verify if correct.
Warning: The TLD '.comm' might not be valid. Please verify.
Username -  user
Domain -  example.comm
````

✅ **Valid Email Example**

```
Enter your email id - johndoe@gmail.com
Username -  johndoe
Domain -  gmail.com
```

❌ **Invalid Email Example**

```
Enter your email id - johndoe@@gmail
Invalid Email!
```

---

## ⚙️ Requirements

* 🐍 **Python 3.6+**
* No external dependencies — uses only Python’s built-in `re` module.

---

## 🚀 Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/Dhritii07/EmailValidation.git
   cd EmailValidation
   ```
2. Run the script:

   ```bash
   python EmailValidation.py
   ```
3. Enter your email when prompted.

---

## 🔮 Future Enhancements

💡 Validate if the email domain actually exists using **DNS lookup**
💡 Add a **GUI** or **web interface** for user-friendly testing
💡 Integrate into **registration forms** for live validation

---

## 🧑‍💻 Author

**Your Name**
💻 GitHub: [@Dhritii07](https://github.com/Dhritii07)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it with attribution.

---

> ⭐ **If you like this project, consider giving it a star on GitHub!**


