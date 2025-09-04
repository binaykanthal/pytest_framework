
def remove_test_insert_and_select(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users(name) VALUES('John Doe') RETURNING id;")
    user_id = cursor.fetchone()[0]
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE id = %s;", (user_id, ))
    result = cursor.fetchone()[0]
    assert result == "John Doe"