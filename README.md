# Chatbot-Discord
The code provided sets up a Discord bot that uses the OpenAI API to generate responses to prompts. Here's a brief overview of the code:

The required modules are imported: os, openai, discord, and dotenv.
The .env file is loaded using load_dotenv().
The OpenAI API key is set using openai.api_key.
The Discord bot token is set using TOKEN.
A discord.Client object is created with the default intents and the message content intent enabled.
An async function gpt3_response(prompt) is defined that uses the OpenAI API to generate a response to a given prompt.
The on_message event is defined to handle incoming messages. If the message is not from the bot itself, the bot is mentioned, and the message contains a prompt, the prompt is sent to the gpt3_response function and the resulting response is sent back to the channel using message.channel.send().
