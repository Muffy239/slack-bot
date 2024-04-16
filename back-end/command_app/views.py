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
# * Create functionality for creating a poll message for the channel


#! Voting Functionality:

# * Yes or No (ONLY)


class Poll(APIView):

    def post(self, request):
        slack_token = env.get("SLACK_TOKEN")
        client = WebClient(token=slack_token)
        payload = request.data

        # * Variables needed from request.
        channel_id = payload.get("channel_id")
        user_id = payload.get("user_id")
        user_message = payload.get("text")

        try:

            # * Format message for chat and add reactions for users to respond to.
            message = f"Creator: <@{user_id}>\n\n Poll: {user_message}\n"
            response = client.chat_postMessage(channel=channel_id, text=message)

            # * add reactions to message for users to vote. (below)
            timestamp = response.get("ts")
            client.reactions_add(
                channel=channel_id,
                name="thumbsup",
                timestamp=timestamp,
            )

            client.reactions_add(
                channel=channel_id,
                name="thumbsdown",
                timestamp=timestamp,
            )

            return Response(status=HTTP_201_CREATED)

        except SlackApiError as e:

            print(f"Slack API Error: {e.response['error']}")

            return Response(status=HTTP_400_BAD_REQUEST)
