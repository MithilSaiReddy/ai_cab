#!/usr/bin/env python
import sys
import warnings
import chainlit as cl


from datetime import datetime

from crew import AiCab


import logging

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

class IgnoreTracerProviderFilter(logging.Filter):
    def filter(self, record):
        return record.getMessage() != 'Overriding of current TracerProvider is not allowed'
        
logging.getLogger('opentelemetry.trace').addFilter(IgnoreTracerProviderFilter())



@cl.on_chat_start
async def on_chat_start():
	await cl.Message(
		content = "REY Langa how are you 🍑️"
	).send()




# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information



def run():
    """
    Run the crew.
    """
   # inputs = {
    #    'topic': input("'Your Topic'"),
    #    'current_year': str(datetime.now().year)
    #}
    #inputs = input("Enter the Topic You want to get news About")
    
    try:
       result =  AiCab().crew().kickoff
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


@cl.on_message
async def on_message(message):
	message_content = message.content
	
	result =  AiCab().crew().kickoff()
	await cl.Message(
		content = result.raw
	).send()

