import slack 
import os
from pathlib import Path
from dotenv import dotenv_values


env = dotenv_values(".env")
# * utilize env.get("<VARIABLE_NAME>") to grab variables from .env file

client = slack.WebClient(token=env.get("SLACK_TOKEN"))


#* This is how to send a message out to chat @ specific channel
client.chat_postMessage(channel='#test', text="Hello World!")

