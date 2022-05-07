from django.shortcuts import render
from django.http import JsonResponse  # For Sending Json Responses
from django.views import View  # Allows our class to act as a view


class FirstView(View):
    # since the methods name is "get" it will run on "get" requests
    def get(self, request):
        return JsonResponse({"hello": "world", "method": request.method})

    # since the methods name is "post" it will run on "post" requests
    def post(self, request):
        return JsonResponse({"hello": "world", "method": request.method})

    # since the methods name is "put" it will run on "put" requests
    def put(self, request):
        return JsonResponse({"hello": "world", "method": request.method})

    # since the methods name is "delete" it will run on "delete" requests
    def delete(self, request):
        return JsonResponse({"hello": "world", "method": request.method})
