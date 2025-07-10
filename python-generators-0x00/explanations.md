# 📘 Explanations for Python Generator MySQL Project

This file provides a **line-by-line explanation** of the implementation files used in the Python Generators and MySQL project.

---

## 📄 File: `seed.py`

```python
import mysql.connector
import csv
import uuid
```

* **Imports necessary modules**:

  * `mysql.connector`: Used to connect and interact with a MySQL database.
  * `csv`: Enables reading data from CSV files.
  * `uuid`: Generates unique user IDs.

```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword"
    )
```

* **connect\_db()**:

  * Connects to the MySQL server (no database specified).
  * Returns the connection object.

```python
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()
```

* **create\_database(connection)**:

  * Uses the connection to execute a SQL query.
  * Creates the database `ALX_prodev` if it doesn't exist.
  * Closes the cursor.

```python
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="ALX_prodev"
    )
```

* **connect\_to\_prodev()**:

  * Connects directly to the `ALX_prodev` database.

```python
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    )""")
    print("Table user_data created successfully")
    cursor.close()
```

* **create\_table(connection)**:

  * Creates a `user_data` table with UUID, name, email, and age.
  * Uses SQL triple quotes for multi-line query.

```python
def insert_data(connection, file_path):
    cursor = connection.cursor()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute("""
            INSERT IGNORE INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
```

* **insert\_data(connection, file\_path)**:

  * Reads each row in the CSV file.
  * Generates a new UUID per user.
  * Inserts the user data into the table.
  * Uses `INSERT IGNORE` to skip duplicates.
  * Commits and closes.

---

## 📄 File: `0-stream_users.py`

```python
from seed import connect_to_prodev

def stream_users():
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
    connection.close()
```

* **stream\_users()**:

  * Connects to the database.
  * Fetches all users.
  * Uses a **generator (`yield`)** to return one row at a time (memory efficient).

---

## 📄 File: `1-batch_processing.py`

```python
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

    cursor.close()
    connection.close()
```

* **stream\_users\_in\_batches(batch\_size)**:

  * Collects users into a list until `batch_size` is reached.
  * Yields each batch.
  * Final remaining batch (if any) is also yielded.

```python
def batch_processing(batch_size):
    processed_users = []
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
                processed_users.append(user)
    return processed_users
```

* **batch\_processing(batch\_size)**:

  * Calls `stream_users_in_batches`.
  * Filters and prints users over age 25.
  * Collects them in a list and returns it.

---

## 📄 File: `2-lazy_paginate.py`

```python
from seed import connect_to_prodev

def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows
```

* **paginate\_users(page\_size, offset)**:

  * Uses SQL LIMIT and OFFSET for pagination.
  * Fetches a page of users.

```python
def lazy_pagination(page_size):
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size
```

* **lazy\_pagination(page\_size)**:

  * Lazily fetches user data page-by-page.
  * Stops when no more data is returned.

---

## 📄 File: `4-stream_ages.py`

```python
from seed import connect_to_prodev

def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield float(age)
    cursor.close()
    connection.close()
```

* **stream\_user\_ages()**:

  * Queries only `age` column.
  * Yields each age as a float — one at a time.

```python
def average_age():
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    avg = total / count if count else 0
    print(f"Average age of users: {avg:.2f}")

if __name__ == "__main__":
    average_age()
```

* **average\_age()**:

  * Uses the generator to compute total and count.
  * Avoids loading all ages in memory.
  * Prints the average.

---

Let me know if you'd like a PDF version or diagrams included! ✅
