from sqlalchemy import create_engine, inspect
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

def list_tables(connection):
    try:
        inspector = inspect(connection)
        tables = inspector.get_table_names()
        print("Tables in the database:")
        for table in tables:
            print(table)
    except SQLAlchemyError as e:
        print("Error while listing tables: {}".format(e))

# Replace these variables with your actual credentials
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Attempt to connect
conn = connect_to_mssql(server, database, username, password)

# List tables if the connection was successful
if conn:
    list_tables(conn)
    conn.close()
