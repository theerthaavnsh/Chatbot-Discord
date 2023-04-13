import os
import openai
import discord
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API
openai.api_key = "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"

# Set up Discord bot
TOKEN ="MTA5NjAzOTYzMTkxNDUzNzA4MA.G9dJEI.508WGlJTGkTZdbztyCee0t7p2kBoVVnvnRBUP0"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def gpt3_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message["content"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        prompt = message.content.replace(f'<@!{client.user.id}>', '').strip()
        response = await gpt3_response(prompt)
        await message.channel.send(response)

client.run(TOKEN)