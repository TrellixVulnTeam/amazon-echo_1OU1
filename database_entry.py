import sqlite3


def convert_into_binary(file_path: str) -> str:
    """
    Takes a file with wav format
    converts to binary
    """
    try:
        with open(file_path, 'rb') as file:
            binary = file.read()
            return binary
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(e.message)


def sqlite_connect(db_name: str) -> str:
    """
    takes database name and attempts to connect
    """
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error:
        print(f"Error connecting to the database '{db_name}'")
    finally:
        return conn


def create_db_table(db_name: str) -> str:
    """
    db_name creates the database and schema in sqlite
    """
    connection = sqlite_connect(db_name)
    cursor = connection.cursor()
    sql_create_table_query = """
    CREATE TABLE audio
    (audio_name TEXT NOT NULL PRIMARY KEY, data BLOB,
    category TEXT NOT NULL,
    SHORT_DESC TEXT NOT NULL);
    """
    try:
        cursor.execute(sql_create_table_query)
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Failed to create the table", error)


def insert_file(file_name: str,
                db_name: str,
                table_name: str,
                category: str,
                SHORT_DESC: str):
    """
    inserts audio data into sqlite and stores it as a blob format.
    """
    try:
        # Establish a connection
        connection = sqlite_connect(db_name)
        print(f"Connected to the database `{db_name}`")
        cursor = connection.cursor()
        sqlite_insert_blob_query = f"""
        INSERT INTO {table_name} (audio_name, data,category,SHORT_DESC)
        VALUES (?,?,?,?)
        """
        binary_file = convert_into_binary(file_name)
        data_tuple = (file_name, binary_file, category, SHORT_DESC)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connection.commit()
        print('Audio file inserted succesfully')
        return True
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob into the table", error)
    finally:
        if connection:
            connection.close()
            print("Connection closed")


# insert_file('quiet-music.wav', 'sample.db', 'audio', "music" ,"quiet")
