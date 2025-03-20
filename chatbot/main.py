# Import the chainlit library and alias it as 'cl'
import chainlit as cl

# Decorator to handle incoming messages
@cl.on_message

# Define an async function that takes a message parameter
async def main(message: cl.Message):

    # Create a response string using the message content
    response = f"you said: {message.content}"

     # Send the response message back to the user
    await cl.Message(content=response).send()