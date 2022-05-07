from django.shortcuts import render
## For sending JSON Responses
from django.http import JsonResponse
## To serialize objects into json strings
from django.core.serializers import serialize
## To turn json strings into dictionaries
import json
## The Dog Model
from .models import Dog
## View class
from django.views import View
## GetBody
from .helpers import GetBody

# class for "/Dog" routes
class DogView(View):
    ## Route to get all Dogs
    def get(self, request):
        all = Dog.objects.all()
        serialized = serialize("json", all)
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)

    ## Route to create a Dog
    def post (self, request):
        body = GetBody(request)
        print(body)
        Dog = Dog.objects.create(name=body["name"], age=body["age"])
        finalData = json.loads(serialize("json", [Dog]))
        return JsonResponse(finalData, safe=False)
