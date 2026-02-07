import logging
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import Ollama

logger = logging.getLogger(__name__)

def get_pandas_agent(df):
    logger.info("Creating Pandas DataFrame agent")

    llm = Ollama(
        model="llama3",
        temperature=0
    )

    agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        verbose=True,
        allow_dangerous_code=True,   
        agent_kwargs={
            "prefix": (
                "You are a careful data analyst.\n"
                "You are working with a pandas DataFrame called df.\n"
                "Use only the data in df.\n"
                "Do not guess values.\n"
                "If a question is ambiguous, ask for clarification.\n"
                "Always return computed results, not code.\n"
            )
        }
    )

    logger.info("Pandas agent created successfully")
    return agent
