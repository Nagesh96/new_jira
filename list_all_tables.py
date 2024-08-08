from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def connect_to_mssql(server, database, username, password):
    try:
        connection_string = (
            "mssql+pyodbc://{username}:{password}@{server}/{database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        ).format(username=username, password=password, server=server, database=database)
        
        engine = create_engine(connection_string)
        connection = engine.connect()
        print("Connection successful!")
        return connection
    except SQLAlchemyError as e:
        print("Error while connecting to database: {}".format(e))
        return None

def list_all_tables(connection):
    try:
        query = text("""
            SELECT TABLE_SCHEMA, TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE'
        """)
        result = connection.execute(query)
        tables = result.fetchall()

        print("Tables in the database:")
        for schema, table in tables:
            print("{}.{}".format(schema, table))

        table_count = len(tables)
        print("\nTotal number of tables: {}".format(table_count))
    except SQLAlchemyError as e:
        print("Error while listing tables: {}".format(e))

# Replace these variables with your actual credentials
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Attempt to connect
conn = connect_to_mssql(server, database, username, password)

# List all tables and count them if the connection was successful
if conn:
    list_all_tables(conn)
    conn.close()
