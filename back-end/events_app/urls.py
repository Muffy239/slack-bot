from django.urls import path
from .views import Greeting

#* < NGROK_URL >/slack/event/greeting/
#* https://8dd0-2601-249-8700-b410-4c6f-7396-888-49c6.ngrok-free.app/slack/event/greeting/

urlpatterns = [
    path("greeting/", Greeting.as_view(), name ="greeting")
    
]
