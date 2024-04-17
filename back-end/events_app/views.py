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
from openai import OpenAI
from .models import Members
from .serializers import MemberSerializer

#! Description:
# * This will handle all events inside the organizations slack channel and respond accordingly.

# *      - Greet Users
# *      - Respond to user questions with ChatGPT from @bot mentions


# TODO CHANGE message in text argument

env = dotenv_values(".env")


class Greeting(APIView):

    def post(self, request):

        # Load your environment variables containing the Slack token
        slack_token = env.get("SLACK_TOKEN")
        client = WebClient(token=slack_token)
        bot_id = client.api_call("auth.test")["user_id"]
        ai_client = OpenAI(api_key=env.get("OPENAI_API_KEY"))

        # Parse the request payload
        payload = request.data
        event = payload.get("event", {})

        # Extract the necessary data from the event
        event_type = event.get("type")
        channel_id = event.get("channel")
        user_id = event.get("user")
        user_message = event.get("text")

        #  Returns challenge token back to slack when connecting events functionality to the bot(required).
        if "challenge" in payload:
            return Response(payload["challenge"], status=HTTP_200_OK)

        # verifying data being sent to us for development.
        console_print = print(
            f"EVENT INFO: {request.data['event']}\n\n~~~~~~~~~~~~~~~~~~~\n\n"
        )

        # * Event: User Joins #general Channel upon entry to organization.
        if event_type == "member_joined_channel":
            try:
                # When users join the #general channel we grab details from Slack API.
                user_info = client.users_info(user=user_id)
                user = user_info["user"]

                # Save Details to database:
                Members.objects.update_or_create(
                    user_id=user_id, default={"username": user["name"]}
                )

                # Generate Message for users:
                welcome_message = f"Hello, <@{user_id}>!, 🎉 I hope you enjoy your time here. Feel free to ask any questions to  <@Adrian>.\n<Greet user with channel info> :)"
                # send message out to slack channel.
                client.chat_postMessage(channel=channel_id, text=welcome_message)

                return console_print, Response(status=HTTP_201_CREATED)
            except SlackApiError as e:
                print(f"Slack API Error: {e.response['error']}")

                return Response(status=HTTP_400_BAD_REQUEST)

        #! CHATGPT
        # * Event: listens to direct DM's from users.abs

        if event_type == "message" and user_id != bot_id:
            if f"<@{bot_id}>" in user_message:
                try:
                    completion = ai_client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {
                                "role": "assistant",
                                "content": "You are a helpful assistant. ",
                            },
                            {
                                "role": "user",
                                "content": user_message,  # Use the actual user message from Slack
                            },
                        ],
                    )

                    response_text = completion.choices[0].message.content

                    print(f"CHATGPT Response: \n\n{response_text}\n\n")

                    client.chat_postMessage(channel=channel_id, text=response_text)

                    return Response(status=HTTP_201_CREATED)
                except (
                    Exception
                ) as e:  # It's a good practice to handle potential exceptions
                    print(f"Error: {str(e)}")
                    return Response(status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_200_OK)
