from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tools import tool
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
)

news_researcher = Agent(
    role="Senior Researcher",
    goal="Discover new state of the art technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "One of the best in the bussiness, proactively find new discoveries"
        "Eager to change the world with ground breaking discoveries in {topic}."
    ),
    tools=[tool],
    llm=llm,
    allow_delevation=True
)

content_writer = Agent(
    role="Senior Content Writer",
    goal="Write a content that can astonish everyone for the provided topic of: {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "One of the best proffesionals when it comes in summarizing complex topics,"
        "brining new discoveries in to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delevation=False
)
