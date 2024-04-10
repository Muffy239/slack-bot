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


# Create your views here.

#* Working as intended. 
class Greeting(APIView):
    def post(self, request):
        if 'challenge' in request.data:
            print('\n\nAPI RESPONSE : ', request.data, '\n\n')
            return Response(request.data['challenge'], status=HTTP_200_OK)
            
        return Response(status=HTTP_200_OK)