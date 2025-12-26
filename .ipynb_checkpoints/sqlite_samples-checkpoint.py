import sqlite3

def main():
    print("=== Connect to database (file-based) ===")
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    print("\n=== Create table ===")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)
    conn.commit()

    print("\n=== Insert single row ===")
    cur.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        ("Alice", 30)
    )
    conn.commit()

    print("\n=== Insert multiple rows ===")
    users = [
        ("Bob", 25),
        ("Charlie", 40),
    ]
    cur.executemany(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        users
    )
    conn.commit()

    print("\n=== Query all rows ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)

    print("\n=== Query single row ===")
    cur.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
    print(cur.fetchone())

    print("\n=== Query with column names (row_factory) ===")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")
    for row in cur.fetchall():
        print(row["id"], row["name"], row["age"])

    print("\n=== Update data ===")
    cur.execute(
        "UPDATE users SET age = ? WHERE name = ?",
        (31, "Alice")
    )
    conn.commit()

    cur.execute("SELECT name, age FROM users WHERE name = ?", ("Alice",))
    print(cur.fetchone())

    print("\n=== Delete data ===")
    cur.execute(
        "DELETE FROM users WHERE name = ?",
        ("Bob",)
    )
    conn.commit()

    cur.execute("SELECT name FROM users")
    print(cur.fetchall())

    print("\n=== Error handling example ===")
    try:
        cur.execute("SELECT * FROM non_existing_table")
    except sqlite3.Error as e:
        print("SQLite error:", e)

    conn.close()

    print("\n=== Context manager example ===")
    with sqlite3.connect("test.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        print("User count:", cur.fetchone()[0])

    print("\n=== In-memory database (for tests) ===")
    mem_conn = sqlite3.connect(":memory:")
    mem_cur = mem_conn.cursor()
    mem_cur.execute("CREATE TABLE t (x INTEGER)")
    mem_cur.execute("INSERT INTO t VALUES (1)")
    mem_cur.execute("SELECT * FROM t")
    print(mem_cur.fetchall())
    mem_conn.close()


if __name__ == "__main__":
    main()
