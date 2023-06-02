import psycopg2
import os


print(os.getenv('EASTVANTAGE_DB_HOST'))

conn = psycopg2.connect(
    host=os.getenv('EASTVANTAGE_DB_HOST'),
    database=os.getenv('EASTVANTAGE_DEFAULT_DB'),
    user=os.getenv('EASTVANTAGE_DB_USER'),
    password=os.getenv('EASTVANTAGE_DB_PWD'),
    port=os.getenv('EASTVANTAGE_DB_PORT')
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

conn.autocommit = True

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a new database if it doesn't already exist
cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (os.getenv('EASTVANTAGE_DB_NAME'),))
db_exists = cur.fetchone()

if not db_exists:
    cur.execute("CREATE DATABASE " + os.getenv('EASTVANTAGE_DB_NAME'))
    print("Database created successfully.")
else:
    print("Database already exists.")
    cur.execute("DROP DATABASE " + os.getenv('EASTVANTAGE_DB_NAME'))
    cur.execute("CREATE DATABASE " + os.getenv('EASTVANTAGE_DB_NAME'))

# Close the cursor and the default database connection
cur.close()
conn.close()

# Establish a connection to the newly created database
conn = psycopg2.connect(
    host=os.getenv('EASTVANTAGE_DB_HOST'),
    database=os.getenv('EASTVANTAGE_DB_NAME'),
    user=os.getenv('EASTVANTAGE_DB_USER'),
    password=os.getenv('EASTVANTAGE_DB_PWD'),
    port=os.getenv('EASTVANTAGE_DB_PORT')

)
# Create a new cursor
cur = conn.cursor()

# SQL query to create the "user" table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS "users" (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(255),
        mail_id VARCHAR(255),
        phone_number VARCHAR(20),
        user_address VARCHAR(255),
        latitude FLOAT,
        longitude FLOAT,
        details JSONB,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
    )
'''

# Execute the create table query
cur.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cur.close()
conn.close()