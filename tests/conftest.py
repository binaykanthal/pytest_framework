import pytest
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def browser():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope='session')
def db_connection():
    conn =psycopg2.connect(
        dbname = "pytest_db",
        user = "pytest_user",
        password = "pytest_pass",
        host = "localhost",
        port = "5432"
    )
    yield conn
    conn.close()