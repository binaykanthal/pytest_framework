from unittest.mock import MagicMock

def get_user_from_db(db_conn, user_id):
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def test_mock_db_query():
    # Mock connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Set expected return
    mock_cursor.fetchone.return_value = ("Charlie",)

    # Call function
    result = get_user_from_db(mock_conn, 1)

    # Assertions
    mock_cursor.execute.assert_called_once_with(
        "SELECT name FROM users WHERE id=?", (1,)
    )
    assert result == "Charlie"