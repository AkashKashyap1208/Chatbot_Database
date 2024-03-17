import mysql.connector

# Replace these values with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Root@123',
    'database': 'Furniture_Shop'
}

try:
    # Create a connection
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print(f"Connected to MySQL database: {db_config['database']}")

        # Your code for executing queries goes here

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection in the 'finally' block to ensure it always happens
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")



import os
from langchain.agents import create_sql_agent
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits import SQLDatabaseToolkit
# from langchain.sql_database import SQLDatabase
from langchain_openai import OpenAI
from langchain.agents import AgentExecutor
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate


# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = "your open ai key"

# Create SQL database connection
db = SQLDatabase.from_uri("mysql://user:Password@localhost/Furniture_Shop")

# Create SQLDatabaseToolkit with an OpenAI language model
llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create SQL agent executor
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Example user input (replace this with the user's actual question)
user_question = "how many items do we have?"

# Execute a query based on the user input
query_result = agent_executor.invoke({"input": user_question})

# Print or process the query result
print(query_result)
          
