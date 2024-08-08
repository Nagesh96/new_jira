from sqlalchemy import create_engine
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

# Replace these variables with your actual credentials
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Attempt to connect
conn = connect_to_mssql(server, database, username, password)

# Don't forget to close the connection if it was successful
if conn:
    conn.close()
