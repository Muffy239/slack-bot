from django.urls import path
from .views import Greeting

#* < NGROK_URL >/slack/event/greeting/


urlpatterns = [
    path("greeting/", Greeting.as_view(), name ="greeting")
    
]
