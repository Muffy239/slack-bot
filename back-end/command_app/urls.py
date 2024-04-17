from django.urls import path
from .views import Poll

#* < NGROK_URL >/slack/slash_command/poll/

urlpatterns = [
    path("poll/",Poll.as_view(), name="command")
]
