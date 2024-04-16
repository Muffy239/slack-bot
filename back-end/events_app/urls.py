from django.urls import path
from .views import Greeting

# * < NGROK_URL >/slack/event/event_handling/



urlpatterns = [
    path("event_handling/", Greeting.as_view(), name="event_handling")
    ]
