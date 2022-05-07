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

# class for "/Dog/<id>" routes
class DogViewID(View):
    ## Function to show 1 Dog
    def get (self, request, id):
        ## get the Dog
        Dog = Dog.objects.get(id=id)
        ## serilize then turn into dictionary
        finalData = json.loads(serialize("json", [Dog]))
        ## send json response
        return JsonResponse(finalData, safe=False)

    ## Function for updating Dog
    def put (self, request, id):
        ## get the body
        body = GetBody(request)
        ##update Dog
        ## ** is like JS spread operator
        Dog.objects.filter(id=id).update(**body)
        ## query for Dog
        Dog = Dog.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [Dog]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, id):
        ## query the Dog
        Dog = Dog.objects.get(id=id)
        ## delete the Dog
        Dog.delete()
        ## serilize and dict updated Dog
        finalData = json.loads(serialize("json", [Dog]))
        ##send json response
        return JsonResponse(finalData, safe=False)