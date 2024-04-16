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

#! Description:
# * This will handle a message inside the server and return the same message back to the user

#! Reason:
# * I needed to check the functionality and get an understanding of the payload.


env = dotenv_values(".env")


class Greeting(APIView):

    def post(self, request):

        # Load your environment variables containing the Slack token
        slack_token = env.get("SLACK_TOKEN")
        client = WebClient(token=slack_token)
        bot_id = client.api_call("auth.test")["user_id"]

        # Parse the request payload
        payload = request.data
        event = payload.get("event", {})

        # Extract the necessary data from the event
        event_type = event.get("type")
        channel_id = event.get("channel")
        user_id = event.get("user")
        user_message = event.get("text")

        # * Returns challenge token back to slack when connecting events functionality to the bot(required).
        if "challenge" in payload:
            return Response(payload["challenge"], status=HTTP_200_OK)

        console_print = print(f"EVENT INFO: {request.data}\n\n~~~~~~~~~~~~~~~~~~~\n\n")

        # * FUNCTION: Greet Users.
        if event_type == "member_joined_channel":
            welcome_message = f"Hello, <@{user_id}>!, 🎉 I hope you enjoy your time here. Feel free to ask any questions to "
            client.chat_postMessage(channel=channel_id, text=welcome_message)
            return console_print, Response(status=HTTP_201_CREATED)

        # * FUNCTION: Reply to users.
        if user_id != str(bot_id):
            # TODO CHANGE message in text argument
            client.chat_postMessage(channel=channel_id, text=user_message)
            return Response(status=HTTP_201_CREATED)

        return Response(status=HTTP_200_OK)
