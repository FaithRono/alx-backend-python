# File: 4-stream_ages.py
# ===============================
from seed import connect_to_prodev

def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield float(age)
    cursor.close()
    connection.close()

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
# This script calculates the average age of users from a database.
# It connects to the database, retrieves ages, and computes the average.