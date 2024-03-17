import os
import streamlit as st
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import OpenAI
from langchain.agents import AgentExecutor
from langchain_community.utilities import SQLDatabase

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = " "

# Create SQL database connection
db = SQLDatabase.from_uri("mysql://user:password@localhost/Demo_db")

# Create SQLDatabaseToolkit with an OpenAI language model
llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create SQL agent executor
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Streamlit app
def main():
    st.title("Chatbot with Streamlit")

    # Get user input
    user_question = st.text_input("Ask a question:")

    # Execute a query based on user input
    if user_question:
        query_result = agent_executor.invoke({"input": user_question})
        st.markdown(f"**Bot Response:** {query_result}")

if __name__ == "__main__":
    main()
