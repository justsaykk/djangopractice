from django.shortcuts import render
from django.http import JsonResponse  # For Sending Json Responses
from django.views import View  # Allows our class to act as a view
from .helpers import GetBody


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


class SecondView(View):
    def get(self, request, param):
        # Grab query from url query
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

    def post(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

    def put(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})

    def delete(self, request, param):
        query = request.GET.get("query", "no query")
        return JsonResponse({"param": param, "query": query})


class ThirdView(View):
    def post(self, request):
        return JsonResponse(GetBody(request))
