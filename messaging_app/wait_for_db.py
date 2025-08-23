import time
import sys
import MySQLdb
import os

def wait_for_db():
    """Wait for database to be available"""
    max_retries = 30
    retry_count = 0
    
    print("Waiting for database connection...")
    
    while retry_count < max_retries:
        try:
            connection = MySQLdb.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('MYSQL_USER', 'messaging_user'),
                password=os.environ.get('MYSQL_PASSWORD', 'secure_password123'),
                database=os.environ.get('MYSQL_DB', 'messaging_app_db'),
                port=int(os.environ.get('DB_PORT', '3306'))
            )
            connection.close()
            print("✅ Database is ready!")
            return True
        except Exception as e:
            print(f"⏳ Database not ready, waiting... (attempt {retry_count + 1}/{max_retries})")
            retry_count += 1
            time.sleep(2)
    
    print("❌ Database connection failed after maximum retries")
    sys.exit(1)

if __name__ == "__main__":
    wait_for_db()