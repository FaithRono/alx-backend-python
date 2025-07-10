# 📦 Python Generators: Stream SQL Data Efficiently

Welcome to the **Python Generators** project! This module demonstrates how to use Python generators to efficiently stream, paginate, and aggregate data from a MySQL database — one row or batch at a time.

---

## 📁 Project Structure

```
python-generators-0x00/
├── 0-main.py
├── 0-stream_users.py
├── 1-batch_processing.py
├── 1-main.py
├── 2-lazy_paginate.py
├── 2-main.py
├── 3-main.py
├── 4-stream_ages.py
├── seed.py
├── user_data.csv
└── README.md
```
---

## 📌 Objectives

1. ✅ **Set up MySQL database and populate it** using a CSV file.
2. ✅ **Stream users row-by-row** using a generator.
3. ✅ **Process user data in batches**.
4. ✅ **Paginate large datasets** lazily.
5. ✅ **Compute average age** without loading the whole dataset into memory.

---

## 🛠️ Setup Instructions

### 1. 🔧 Install Dependencies

Make sure you have Python and MySQL installed. Then install:

```bash
pip install mysql-connector-python
```
### 2. 📥 Create and Seed the Database

Update your MySQL credentials in seed.py, then run:
```
./0-main.py
```

This will:

*Connect to MySQL*

*Create the ALX_prodev database*

*Create the user_data table*

*Populate it with sample data from user_data.csv*

## 🚀 Features and Usage

### 1️⃣ Stream Users One by One

./1-main.py

File: 0-stream_users.py
```
def stream_users():
    ...
    yield row
```
Uses a generator to yield users one by one.

### 2️⃣ Batch Processing (Users > Age 25)

./2-main.py
File: 1-batch_processing.py

```
def stream_users_in_batches(batch_size)
def batch_processing(batch_size)
```
Processes users in chunks and filters based on age.

### 3️⃣ Lazy Pagination

python3 3-main.py
File: 2-lazy_paginate.py

```
def lazy_pagination(page_size)
```
Simulates paginated fetching using offset + LIMIT.

### 4️⃣ Memory-Efficient Aggregation

python3 4-stream_ages.py
File: 4-stream_ages.py

```
def stream_user_ages()
def average_age()
```
Calculates average user age using a streaming approach.

### 📄 Sample Output

- connection successful
-Table user_data created successfully
-Database ALX_prodev is present 
- [{'user_id': '...', 'name': 'John Doe', 'email': 'john@example.com', 'age': 32}, ...]
---Average age of users: 64.23
---💡 Technologies Used
--- Python 3.8+ ---

MySQL

Generators (yield)

CSV file handling

👤 Author
Faith Cherono

GitHub: FaithRono

LinkedIn: Faith Cherono

Email: faithrono132@gmail.com

🏁 License
This project is part of the ALX Backend Specialization and is open for educational use.
