from django.urls import path
from .views import Poll

# * < NGROK_URL >/slack/chatbot/response/
# *

urlpatterns = [path("response/", Poll.as_view(), name="chatbot")]
