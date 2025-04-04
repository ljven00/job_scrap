"""
One-time Run file which connect to the database using
credentials from the .env file on the same directory,
then create the table to store the information about
each job we scrap
"""

import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError, Error

load_dotenv()


def get_connection():
    """Return a connection object that allows access to the database
    Or None in case an error occurred"""
    try:
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
        )
    except OperationalError as e:
        print("Could not connect to the database.")
        print("Error:", e)
        return None


def create_table():
    """Create jobs table on the database"""
    conn = get_connection()
    if not conn:
        print("Skipping table creation due to connection failure.")
        return

    try:
        # Using a context manager for automatic closure
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS jobs (
                        id SERIAL PRIMARY KEY,
                        title TEXT,
                        company TEXT,
                        location TEXT,
                        date_posted TEXT,
                        link TEXT
                    );
                """)
        print("Table 'jobs' has been created successfully.")
    except Error as e:
        print("Failed to create table.")
        print("Error:", e)
