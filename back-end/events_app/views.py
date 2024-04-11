from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from slack_sdk.signature import SignatureVerifier
from slack_sdk import WebClient
from dotenv import dotenv_values
from slack_sdk.errors import SlackApiError


env = dotenv_values(".env")

#! Description:
#* This will handle a message inside the server and return the same message back to the user

#! Reason:
#* I needed to check the functionality and get an understanding of the payload. 

class Greeting(APIView):

    def post(self, request):
        # Load your environment variables containing the Slack token
        slack_token = env.get('SLACK_TOKEN')
        client = WebClient(token=slack_token)
        bot_id = client.api_call("auth.test")['user_id']
        
        # Parse the request payload
        payload = request.data
        event = payload.get('event', {})
        
        # Extract the necessary data from the event
        channel_id = event.get('channel')
        user_id = event.get('user')
        message = event.get('text')
        name = event.get('name')
        
        if 'challenge' in payload:
            return Response(payload['challenge'])
        
            print(payload)
            print(f"\n\n BOT ID -> {bot_id}")
            print(f"\n\n BOT ID TYPE -> {type(bot_id)}")
            print(f"\n\n USERNAME TYPE-> {type(user_id)}")
            print(f" USERNAME -> {user_id}")
            
        if  user_id != str(bot_id):
            client.chat_postMessage(channel=channel_id, text=message)
            return Response(status=HTTP_201_CREATED)
