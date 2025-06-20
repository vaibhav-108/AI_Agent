from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

import os 
os.environ["OPENAI_API_KEY"] =  os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

## Create a senior blog content researcher


model = ChatOpenAI(model="nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
                 api_key=OPENAI_API_KEY,
                 openai_api_base="https://openrouter.ai/api/v1")

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=model
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)