import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict   # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@function_tool("get_shahid_data")
def get_shahid_data() -> str:
    """
    Fetches Shahid Ali's profile data from GitHub API but shows LinkedIn URL instead of GitHub URL.
    """
    url = "https://api.github.com/users/shahidali54"
    linkedin_url = "www.linkedin.com/in/shahid-ali-64676a2ba" 

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            info = f"""
👨‍💻 Name: {data.get('name')}
📝 Bio: {data.get('bio')}
📍 Location: {data.get('location')}
�� Email: {data.get('email')}
��� GitHub Profile: {data.get('html_url')}
🔗 LinkedIn Profile: {linkedin_url}
            """
            return info
        else:
            return f"Error fetching data: Status code {response.status_code}"
    except Exception as e:
        return f"Error fetching data: {str(e)}"


# Agent Configuration
agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent designed to provide friendly interactions and information about Shahid Ali.

Your responsibilities:
1. Greet users warmly when they say hello (respond with 'Salam from Shahid Ali')
2. Say goodbye appropriately when users leave (respond with 'Allah Hafiz from Shahid Ali')
3. When users request information about Shahid Ali, use the get_shahid_data tool to retrieve and share his profile information
4. For any questions not related to greetings or Shahid Ali, politely explain: 'I'm only able to provide greetings and information about Shahid Ali. I can't answer other questions at this time.'

Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
    model=model,
    tools=[get_shahid_data],
)


# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    print(f"Provider: {provider_id}")
    print(f"User data: {raw_user_data}")
    return default_user


# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you today?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    # Add user message to history
    history.append({"role": "user", "content": message.content})

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
