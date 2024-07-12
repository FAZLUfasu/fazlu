import pymysql

# Connection parameters
host = 'localhost'
user = 'root'
password = 'fazlu'
database_to_check = 'investors'  # Replace with the database name you want to check

try:
    # Connect to MySQL
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    # Check if the database exists
    cursor = conn.cursor()
    cursor.execute(f"SHOW DATABASES LIKE '{database_to_check}'")
    result = cursor.fetchone()

    if result:
        print(f"Database '{database_to_check}' exists.")
    else:
        print(f"Database '{database_to_check}' does not exist.")

    cursor.close()
    conn.close()

except pymysql.Error as e:
    print(f"Error connecting to MySQL: {e}")
