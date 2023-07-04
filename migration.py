import pymysql
import json
import os

# Connect to the MySQL database
connection_string= {
    "host":os.getenv('host'),
    "port":os.getenv('port'),
    "user":os.getenv('user'),
    "password":os.getenv('password'),
    "database":os.getenv('database'),
    "table":os.getenv('table')
}
db = pymysql.connect(host=connection_string["host"],user=connection_string["user"],password=connection_string["password"], port=connection_string["port"])

# Create a new database //this should be in try but who cares (:)
database_name = database=connection_string["database"]
cursor = db.cursor()
cursor.execute("DROP DATABASE chatbot;")
print("initiated schema")
cursor.execute("CREATE DATABASE {}".format(database_name))
print("schema chatbot created successfully")
print("closing connection")
db.close()

# Create a new tables  //this should be in try but who cares (:)
db = pymysql.connect(host=connection_string["host"],user=connection_string["user"],password=connection_string["password"], database=connection_string["database"], port=connection_string["port"])
cursor_table = db.cursor()
print("reopened connection")
create_table_query = """
CREATE TABLE {} (
    tag VARCHAR(600),
    patterns TEXT(2000),
    responses TEXT(16000)
)
""".format(connection_string["table"])
cursor_table.execute(create_table_query)
# Commit the changes and close the connection
db.commit()

def insert_to_table(cursor_table):
    print("attempting to insert records")
    with open("intent.json", "r") as file:
        intents_data = json.load(file)
    # Insert intents, patterns, and responses into the database
    for intent_data in intents_data['intents']:
        # Extract tag, patterns, and responses from the intent_data
        tag = intent_data['intent']
        patterns = ', '.join([f'"{pattern}"' for pattern in intent_data['text']])
        responses = ', '.join([f'"{response}"' for response in intent_data['responses']])

        # Insert the intent into the database
        insert_intent_query = 'INSERT INTO intents (tag, patterns, responses) VALUES (%s, %s, %s)'
        cursor_table.execute(insert_intent_query, (tag, patterns, responses))
    # Commit the changes to the database
    db.commit()
insert_to_table(cursor_table)
db.close()
