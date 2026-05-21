# 🐍 Learn Python — Complete Revision Guide

> A chapter-wise Python reference guide with concise definitions and code examples for quick revision.

---

## 📑 Table of Contents <a id="Table-of-Contents"></a>

| # | Topic | Key Concepts |
|---|-------|--------------|
| 0 | [Introduction & Print](#chapter-0--introduction--print) | `print()`, string repetition |
| 1 | [Variables & User Input](#chapter-1--variables--user-input) | Variables, `input()`, f-strings |
| 2 | [Data Types, Operators & Type Casting](#chapter-2--data-types-operators--type-casting) | `int`, `float`, `str`, operators, implicit/explicit conversion |
| 3 | [Strings](#chapter-3--strings) | Indexing, slicing, string methods, escape sequences |
| 4 | [Conditionals, Lists & Tuples](#chapter-4--conditionals-lists--tuples) | `if/elif/else`, list methods, tuple immutability |
| 5 | [Dictionaries & Sets](#chapter-5--dictionaries--sets) | Key-value pairs, set uniqueness |
| 6 | [Loops](#chapter-6--loops) | `while`, `for`, `range()`, `break`, `pass`, patterns |
| 7 | [Functions](#chapter-7--functions) | `def`, parameters, default args, `return` |
| 8 | [File Handling](#chapter-8--file-handling) | `open()`, read/write modes, `with`, `os` module |
| 9 | [OOP — Classes & Objects](#chapter-9--oop--classes--objects) | Classes, objects, `__init__`, `self`, methods |
| — | [Projects](#-projects) | Expense Tracker, Chatbot, Clock, Text Editor, Slideshow |

---

## Chapter 0 — Introduction & Print | [Back to Menu🔝](#Table-of-Contents)

### What is `print()`?

`print()` is a built-in function that outputs text or values to the console.

```python
print("Hello World")
print("Harshit this side")
```

### String Repetition

You can repeat strings using the `*` operator.

```python
# Print name 10 times, each on a new line
print(("Harshit Singh" + "\n") * 10)
```

> **Key Takeaway:** `print()` is the first function you learn. The `*` operator on strings repeats them.

---

## Chapter 1 — Variables & User Input | [Back to Menu🔝](#Table-of-Contents)

### Variables

A **variable** is a named container that stores a value in memory. Python is dynamically typed — no need to declare the type.

```python
name = "Harshit Singh"
age1 = 25
age2 = 50

print(f"Actual value of age2 is : {age2}")  # 50
age2 = age1
print(f"Now value of age2 is : {age2}")     # 25
```

### User Input — `input()`

`input()` reads a line of text from the user. It **always returns a string**.

```python
name = input("Enter your good name: ")
print("Your good name is:", name)
```

### Type Casting with Input

Since `input()` returns a string, cast it to the required type.

```python
# Calculate area of circle from diameter
diameter = float(input("Enter the diameter of the circle: "))
radius = diameter / 2
area = 3.14 * radius ** 2
print(f"The area of the circle is: {area}")
```

> **Key Takeaway:** `input()` always returns `str`. Use `int()` or `float()` to convert.

---

## Chapter 2 — Data Types, Operators & Type Casting | [Back to Menu🔝](#Table-of-Contents)

### Data Types

Python has several built-in data types. Use `type()` to check.

| Type | Example | Description |
|------|---------|-------------|
| `int` | `26` | Whole numbers |
| `float` | `22.23` | Decimal numbers |
| `str` | `"Rohit"` | Text / sequence of characters |
| `bool` | `True` | Boolean values |

```python
age = 26
area = 22.23
name = "Rohit Sharma"

print(type(age))   # <class 'int'>
print(type(area))  # <class 'float'>
print(type(name))  # <class 'str'>
```

### Operators

#### Arithmetic Operators

```python
x, y = 10, 5
print(x + y)   # 15  (Addition)
print(x - y)   # 5   (Subtraction)
print(x * y)   # 50  (Multiplication)
print(x / y)   # 2.0 (Division)
print(x % y)   # 0   (Modulus)
print(x ** y)  # 100000 (Exponentiation)
```

#### Comparison Operators

```python
print(x == y)  # False
print(x < y)   # False
print(x > y)   # True
```

#### Logical Operators

```python
print(x > y and x < y)   # False
print(x > y or x < y)    # True
print(not(x > y))         # False
```

#### Assignment Operators

```python
a = 2
a += 6   # same as a = a + 6
a -= 1   # same as a = a - 1
a /= 10  # same as a = a / 10
a *= 10  # same as a = a * 10
```

#### Bitwise Operators

```python
a = 5  # binary: 0101
print(a << 1)  # 10 (left shift)
print(a << 2)  # 20

b = 20  # binary: 10100
print(b >> 1)  # 10 (right shift)
print(b >> 2)  # 5

# XOR swap (no temp variable!)
a, b = 5, 3
a = a ^ b  # a=6
b = a ^ b  # b=5
a = a ^ b  # a=3 → swapped!
```

### Type Casting

#### Implicit Conversion (Automatic)

Python automatically converts smaller types to larger types.

```python
x = 5      # int
y = 10.5   # float
z = x + y  # float (15.5) — int promoted to float
print(type(z))  # <class 'float'>
```

#### Explicit Conversion (Manual)

You manually convert using `int()`, `float()`, `str()`.

```python
num = input("Enter a value: ")          # always str
convertedValue = float(num)
print(type(num))             # <class 'str'>
print(type(convertedValue))  # <class 'float'>
```

> **Key Takeaway:** Python auto-promotes `int` → `float`. Use explicit casting for `input()` values.

---

## Chapter 3 — Strings | [Back to Menu🔝](#Table-of-Contents)

### String Basics

A **string** is an immutable sequence of characters. Defined with `' '`, `" "`, or `''' '''`.

```python
str1 = 'Hello'
str2 = "Harshit"
str3 = '''Python Course by Harshit Singh'''

# Concatenation
print(str1 + " " + str2)  # Hello Harshit

# Length
print(len(str1))  # 5
```

### Indexing

Each character has a position (index) starting from `0`. Negative indexing starts from `-1` (last char).

```python
str1 = "Harshit's name is very nice"
print(str1[0])  # H
print(str1[4])  # h
```

### Slicing

Extract a substring using `str[start:end]` (end is exclusive).

```python
str = "GulabJamun"
print(str[0:5])   # Gulab
print(str[:5])    # Gulab  (start defaults to 0)
print(str[5:10])  # Jamun
print(str[5:])    # Jamun  (end defaults to len)
print(str[-2:])   # un     (negative indexing)
```

### String Methods

Strings are **immutable** — methods return new strings.

| Method | Description |
|--------|-------------|
| `.upper()` | Converts to uppercase |
| `.lower()` | Converts to lowercase |
| `.title()` | Capitalizes first letter of each word |
| `.find("x")` | Returns index of first occurrence |
| `.replace(old, new)` | Replaces substring |
| `.count("x")` | Counts occurrences |

```python
s = "harshit singh"
print(s.upper())              # HARSHIT SINGH
print(s.title())              # Harshit Singh
print(s.find("gh"))           # index of "gh"
print(s.replace("singh", "Best"))  # harshit Best
print(s.count("h"))           # 2
```

### Escape Sequences

| Sequence | Output |
|----------|--------|
| `\n` | New line |
| `\t` | Tab space |

```python
print("Hello\nWorld")   # prints on two lines
print("Hello \t World") # prints with tab
```

> **Key Takeaway:** Strings are immutable. Use slicing `[start:end]` and built-in methods for manipulation.

---

## Chapter 4 — Conditionals, Lists & Tuples | [Back to Menu🔝](#Table-of-Contents)

### Conditional Statements (`if / elif / else`)

Execute different blocks of code based on conditions.

```python
marks = 95

if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
else:
    print("Try harder")

# Voting eligibility
age = 16
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

### Lists

A **list** is a mutable, ordered collection that can hold mixed data types. Defined with `[]`.

```python
food = ["chole bathure", "choco waffle", "gulab jamun", "apple", "mango", 7]
print(len(food))    # 6
print(food[0])      # chole bathure
```

### List Methods

| Method | Description |
|--------|-------------|
| `.append(x)` | Add item to end |
| `.insert(i, x)` | Insert at index `i` |
| `.pop(i)` | Remove item at index `i` |
| `.remove(x)` | Remove first occurrence of `x` |
| `.sort()` | Sort in place |
| `max() / min()` | Get max/min value |

```python
marks = [99, 100, 90, 95]
marks.append(92)       # [99, 100, 90, 95, 92]
marks.sort()           # [90, 92, 95, 99, 100]
marks.pop(1)           # removes index 1
marks.insert(1, 100)   # inserts 100 at index 1
print(max(marks))      # 100
```

### Tuples

A **tuple** is an immutable, ordered collection. Defined with `()`. Faster than lists.

```python
myTuple = (78, 90, 75)
studentTuple = ("Khushi", "Divya", "Ishaan", "Divya")

# Tuples are IMMUTABLE — this would error:
# studentTuple[1] = "Aanchal"

emptyTuple = ()
singleTuple = (1,)   # comma required for single element!

print(studentTuple.index("Divya"))  # 1 (first occurrence)
print(studentTuple.count("Divya"))  # 2
```

> **Key Takeaway:** Lists are mutable (`[]`), Tuples are immutable (`()`). Strings are also immutable.

---

## Chapter 5 — Dictionaries & Sets | [Back to Menu🔝](#Table-of-Contents)

### Dictionaries

A **dictionary** stores data as **key-value pairs**. Keys must be unique. Defined with `{}`.

```python
student = {
    "name": "Harshit Singh",
    "city": "Sultanpur",
    "age": 25,
    "rollNumber": 23,
}

print(student["name"])         # Harshit Singh
student["favSubject"] = "Maths"  # add new key
student.pop("favSubject")        # remove key

print(student.keys())    # dict_keys([...])
print(student.values())  # dict_values([...])
print(student.items())   # dict_items([...])
print(student.get("name"))  # Harshit Singh (safe access)
```

### Sets

A **set** is an unordered collection of **unique** elements. Duplicates are automatically removed. Defined with `{}`.

```python
food = {"paneer", "chole bathure", "sandwitch", "golgappe", "paneer"}
print(food)  # "paneer" appears only once!

food.add("Kunafa")
food.remove("chole bathure")

# Empty set (NOT {} — that creates a dict!)
emptySet = set()
print(type(emptySet))  # <class 'set'>
```

### Converting List → Set (Remove Duplicates)

```python
langs = ["Python", "Java", "C++", "Python", "Java", "C"]
uniqueLangs = set(langs)
print(len(uniqueLangs))  # 4 unique languages
```

> **Key Takeaway:** Dicts = key-value pairs. Sets = unique items, no duplicates. Empty set = `set()` not `{}`.

---

## Chapter 6 — Loops | [Back to Menu🔝](#Table-of-Contents)

### While Loop

Repeats a block **as long as** the condition is `True`.

```python
num = 1
while num <= 5:
    print("Harshit Singh")
    num += 1
```

### For Loop

Iterates over a sequence (list, tuple, string, dict, range).

```python
# Iterate over a list
foodList = ["cake", "mango", "pizza"]
for item in foodList:
    print(item)

# Iterate over a dictionary
carRated = {"BMW": 4.5, "Audi": 4.0, "Mercedes": 4.8}
for key in carRated:
    print(f"Car: {key}, Rating: {carRated[key]}")

# enumerate() — get index + value
items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)
```

### `range()` Function

Generates a sequence of numbers: `range(start, stop, step)`.

```python
for i in range(2, 21, 2):   # even numbers 2 to 20
    print(i)

for i in range(10, 0, -1):  # countdown 10 to 1
    print(i)
```

### `break` and `pass`

```python
# break — exit loop immediately
# (used in projects like menu-driven programs)

# pass — do nothing (placeholder)
for i in range(1, 7):
    pass  # empty loop body, no error
```

### Pattern Printing

```python
n = 1
while n <= 4:
    print("*" * n)
    n += 1
# Output:
# *
# **
# ***
# ****
```

### Sum of First N Natural Numbers

```python
n = int(input("Enter a number: "))
total = 0
while n >= 1:
    total += n
    n -= 1
print("Sum =", total)
```

> **Key Takeaway:** `while` = condition-based. `for` = sequence-based. `range(start, stop, step)` generates numbers.

---

## Chapter 7 — Functions | [Back to Menu🔝](#Table-of-Contents)

### What is a Function?

A **function** is a reusable block of code defined with `def`. It avoids repetition.

```python
def sumFunc():
    a, b = 4, 8
    print(a + b)

sumFunc()  # 12 — call it anytime
sumFunc()  # 12
```

### Parameters & Arguments

**Parameters** = variables in function definition. **Arguments** = values passed during call.

```python
def average(a=10, b=20):     # default parameters
    print((a + b) / 2)

average(5, 10)   # 7.5
average()        # 15.0 (uses defaults)
```

### Return Statement

`return` sends a value back to the caller. Without it, function returns `None`.

```python
def multiply(a=10, b=10):
    return a * b

result = multiply(5, 10)
print(result)  # 50
```

### Returning Multiple Values

```python
def countVowConso(userInput):
    vowels = "aeiouAEIOU"
    countV, countC = 0, 0
    for char in userInput:
        if char.isalpha():
            if char in vowels:
                countV += 1
            else:
                countC += 1
    return countV, countC

v, c = countVowConso("Harshit Singh")
print(f"Vowels: {v}, Consonants: {c}")
```

> **Key Takeaway:** `def` defines, `return` sends back values. Use default params for flexibility.

---

## Chapter 8 — File Handling | [Back to Menu🔝](#Table-of-Contents)

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). Error if file doesn't exist |
| `"w"` | Write. Creates file / overwrites existing |
| `"x"` | Exclusive create. Error if file exists |
| `"a"` | Append. Adds to end of file |

### Reading Files

```python
# Basic read
file = open("mast.txt", "r")
data = file.read()
print(data)
file.close()
```

### `with` Keyword (Recommended)

Automatically closes the file — no need for `file.close()`.

```python
with open("notes.txt", "r") as f:
    data = f.read()        # entire file as string
    # f.readline()         # one line at a time
    # f.readlines()        # list of all lines
```

| Method | Returns |
|--------|---------|
| `.read()` | Entire content as one string |
| `.readline()` | One line at a time |
| `.readlines()` | List of all lines |

### Writing Files

```python
# Write mode — creates or overwrites
file = open("report.txt", "w")
file.write("Hello World")

# Exclusive create — error if exists
file = open("new_report.txt", "x")
file.write("Brand new file")
```

### Searching in a File

```python
with open("certificate.txt", "r") as f:
    data = f.read().lower()
    if "live" in data:
        print("Word found!")
```

### Try-Except with Files

```python
try:
    with open("notes.txt", "r") as f:
        lines = f.readlines()
        print("Number of lines:", len(lines))
except:
    print("File does not exist")
```

### File Operations with `os` Module

```python
import os
# os.rename("old.txt", "new.txt")   # rename
# os.remove("file.txt")             # delete permanently
```

> **Key Takeaway:** Always use `with open()` for auto-closing. `"r"` read, `"w"` write, `"x"` create, `"a"` append.

---

## Chapter 9 — OOP — Classes & Objects | [Back to Menu🔝](#Table-of-Contents)

### What is a Class?

A **class** is a blueprint for creating objects. It bundles data (attributes) and behavior (methods).

```python
class Vehicle:
    color = "black"           # attribute
    petrolOrDiesel = "petrol"
    mileage = "10"

    def start():              # method
        print("Vehicle started")

# Creating objects
car = Vehicle()
car.color = "pink"
print(car.color)   # pink

bike = Vehicle()
print(bike.color)  # black (default)
```

### `__init__()` — Constructor

The `__init__` method is called **automatically** when an object is created. `self` refers to the current object.

```python
class Student:
    schoolName = "ABC School"

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Khushi", "Btech")
print(student1.name)    # Khushi
print(student1.course)  # Btech

student2 = Student("Ankit", "Bsc")
print(student2.name)    # Ankit
```

### Methods in Classes

```python
class Student:
    def __init__(self, name, listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        total = sum(self.listOfMarks)
        return total / len(self.listOfMarks)

s1 = Student("Harshit", [99, 95, 90])
print(s1.average())  # 94.67
```

> **Key Takeaway:** Class = blueprint, Object = instance. `__init__` is the constructor. `self` = current object.

---

## 🚀 Projects

### Project 1 — 💰 Expense Tracker

A menu-driven CLI app to add, view, and total expenses using **lists of dictionaries**.

**Concepts Used:** `while True`, `if/elif/else`, `list`, `dict`, `for` loop, `break`, `input()`, f-strings

```python
expensesList = []

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        date = input("Date: ")
        category = input("Category (Food/Travel/Books): ")
        description = input("Description: ")
        amount = float(input("Amount: "))
        expense = {"date": date, "category": category,
                   "description": description, "amount": amount}
        expensesList.append(expense)
        print("Expense added!")

    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses yet.")
        else:
            for i, e in enumerate(expensesList, 1):
                print(f"{i} -> {e['date']}, {e['category']}, "
                      f"{e['description']}, ₹{e['amount']}")

    elif choice == 3:
        total = sum(e["amount"] for e in expensesList)
        print("Total Expense =", total)

    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
```

---

### Project 2 — 🤖 Rule-Based AI Chatbot

A chatbot that greets based on time-of-day and responds using a keyword-matching dictionary.

**Concepts Used:** `datetime`, `dict`, `functions`, `while True`, `break`, `.lower()`, `for` loop

```python
import datetime

name = input("Enter your name: ")
hour = datetime.datetime.now().hour

if 5 <= hour <= 11:
    print("Good morning,", name)
elif 11 <= hour <= 17:
    print("Good afternoon,", name)
elif 17 <= hour <= 20:
    print("Good evening,", name)
else:
    print("Good night,", name)

responses = {
    "hello": "Hi! How can I help you?",
    "how are you": "I am fine, thank you!",
    "who are you": "I am a smart AI chatbot",
    "motivate me": "Every bug makes you a better developer!",
}

def getResponse(question):
    question = question.lower()
    for key in responses:
        if key in question:
            return responses[key]
    return "I don't know that yet."

while True:
    userInput = input("You: ")
    print("Bot:", getResponse(userInput))
    if "bye" in userInput.lower():
        break
```

---

### Project 3 — 🕐 Digital Clock (GUI)

A real-time digital clock built with **Tkinter**.

**Concepts Used:** `tkinter`, `time.strftime()`, `.after()` for recurring updates, `Label` widget

```python
import time
import tkinter as tk

root = tk.Tk()
root.title("Digital Clock")

def currentTime():
    string = time.strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, currentTime)  # update every 1 sec

label = tk.Label(root, font=('calibri', 60, 'bold'),
                 background='yellow', foreground='black')
label.pack(anchor='center')

currentTime()
root.mainloop()
```

---

### Project 4 — 📝 Simple Text Editor (GUI)

A Notepad-like text editor with New, Open, Save, and Exit using **Tkinter + filedialog**.

**Concepts Used:** `tkinter`, `filedialog`, `messagebox`, `Menu`, file handling (`open`, `read`, `write`)

```python
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 18))
text.pack(expand=True, fill=tk.BOTH)

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    path = filedialog.askopenfilename(defaultextension=".txt",
           filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "r") as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt",
           filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "w") as f:
            f.write(text.get(1.0, tk.END))
    messagebox.showinfo("Info", "File saved!")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
```

---

### Project 5 — 🖼️ Photo Slideshow Album (GUI)

An image slideshow player using **Tkinter + PIL (Pillow)**.

**Concepts Used:** `tkinter`, `PIL` (Pillow), `ImageTk`, `time.sleep()`, lists, `for` loop, `Button` widget

```python
import tkinter as tk
import time
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("500x500")

image_paths = ["img0.jpeg", "img1.JPG", "img2.JPG"]  # your image paths

images = []
for path in image_paths:
    img = Image.open(path).resize((700, 700))
    images.append(ImageTk.PhotoImage(img))

image_label = tk.Label(root)
image_label.pack(pady=30)

def start_slideshow():
    for photo in images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

play_btn = tk.Button(root, text="Play Slideshow",
                     font=("Arial", 17), command=start_slideshow)
play_btn.pack(pady=40)

root.mainloop()
```

---

## 📌 Quick Cheat Sheet

| Concept | Mutable? | Ordered? | Syntax | Duplicates? |
|---------|----------|----------|--------|-------------|
| **List** | ✅ Yes | ✅ Yes | `[]` | ✅ Yes |
| **Tuple** | ❌ No | ✅ Yes | `()` | ✅ Yes |
| **Dictionary** | ✅ Yes | ✅ Yes (3.7+) | `{}` | Keys: ❌ No |
| **Set** | ✅ Yes | ❌ No | `{}` / `set()` | ❌ No |
| **String** | ❌ No | ✅ Yes | `""` | ✅ Yes |

---

> 💡 **Tip:** Bookmark this file and come back anytime for a quick revision before interviews or exams!

---

*Built with ❤️ while learning Python*
