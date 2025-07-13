# Python Decorators for Database Operations - Detailed Explanations

This document provides in-depth explanations of each decorator implementation in the Python Decorators project, covering their purpose, implementation details, and usage patterns.

## Table of Contents
1. [Query Logging Decorator](#0-log_queriespy)
2. [Connection Management Decorator](#1-with_db_connectionpy)
3. [Transaction Management Decorator](#2-transactionalpy)
4. [Retry Mechanism Decorator](#3-retry_on_failurepy)
5. [Query Caching Decorator](#4-cache_querypy)

---

## 0-log_queries.py
### Query Logging Decorator

**Purpose**: 
Intercepts and logs all SQL queries before execution for debugging and monitoring purposes.

**Key Components**:
```python
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        if query:
            print(f"[{datetime.now()}] Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper
Implementation Details:

Uses functools.wraps to preserve the original function's metadata

Extracts the query from keyword arguments using kwargs.get('query')

Prints a timestamped log message before executing the query

Returns the original function's result unchanged

Behavior:

When applied to a database function, it will:

Print the query with execution timestamp

Execute the original function

Return the results transparently

Example Usage:

python
@log_queries
def fetch_data(query):
    # database operations
Best Practices:

Include timestamps for better debugging

Consider logging to a file in production

Can be extended to log execution time and results

1-with_db_connection.py
Connection Management Decorator
Purpose:
Automates database connection lifecycle management.

Key Components:

python
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper
Implementation Details:

Creates a new SQLite connection when called

Uses try-finally to ensure connection is always closed

Passes the connection as first argument to decorated function

Returns the original function's result

Behavior:

Automatically handles:

Connection establishment

Resource cleanup

Error propagation

Example Usage:

python
@with_db_connection
def db_operation(conn, params):
    # uses provided connection
Best Practices:

Always use context managers or try-finally for resources

Consider adding connection pooling in production

Can be extended to support different database backends

2-transactional.py
Transaction Management Decorator
Purpose:
Provides automatic transaction handling with commit/rollback.

Key Components:

python
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"Transaction failed: {e}")
            raise
    return wrapper
Implementation Details:

Wraps function execution in try-except block

Commits on successful execution

Rolls back on any exception

Re-raises exceptions after rollback

Designed to work with connection decorator

Behavior:

When combined with connection decorator:

Establishes connection

Begins transaction

Executes operation

Commits or rolls back

Closes connection

Example Usage:

python
@with_db_connection
@transactional
def update_data(conn, params):
    # transactional operation
Best Practices:

Always place below connection decorator

Handle specific exceptions when possible

Consider adding transaction isolation levels

3-retry_on_failure.py
Retry Mechanism Decorator
Purpose:
Automatically retries failed database operations.

Key Components:

python
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempts += 1
            raise Exception("Maximum retry attempts reached")
        return wrapper
    return decorator
Implementation Details:

Uses a decorator factory pattern (accepts configuration)

Implements retry loop with attempt counter

Sleeps between retries using configurable delay

Logs retry attempts

Raises final exception if all retries fail

Behavior:

Attempts operation up to N times

Waits between attempts

Returns first successful result

Raises exception if all attempts fail

Example Usage:

python
@retry_on_failure(retries=3, delay=2)
def unreliable_operation():
    # might fail temporarily
Best Practices:

Use exponential backoff for production systems

Consider circuit breakers for persistent failures

Log retry attempts for monitoring

4-cache_query.py
Query Caching Decorator
Purpose:
Caches query results to optimize performance.

Key Components:

python
query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query')
        if query in query_cache:
            print("Returning cached result")
            return query_cache[query]
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper
Implementation Details:

Uses global dictionary for cache storage

Uses query text as cache key

Checks cache before execution

Stores new results in cache

Logs cache hits

Behavior:

First execution: runs query and caches result

Subsequent executions: returns cached result

Transparent to calling code

Example Usage:

python
@cache_query
def expensive_query(query):
    # database operation
Best Practices:

Consider cache invalidation strategies

Add TTL (time-to-live) for cached items

Use more sophisticated caching libraries for production

Consider thread safety for cache access

Combined Usage Example
python
@with_db_connection
@transactional
@retry_on_failure(retries=3)
@log_queries
@cache_query
def robust_query_operation(conn, query):
    # Fully instrumented database operation
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
This combination provides:

Automatic connection handling

Transaction safety

Failure recovery

Query logging

Result caching

Execution Order:

cache_query (outermost)

log_queries

retry_on_failure

transactional

with_db_connection (innermost)