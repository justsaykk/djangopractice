from django.db import models

# Create your models here.
#The Model class we will inherit from
from django.db import models

#new model class
class Dog(models.Model):
    # define a string field of max 100 characters
    name = models.CharField(max_length=100)
    # define a age that is an integer
    age = models.IntegerField()

# class for "/turtle/<id>" routes
class TurtleViewID(View):
    ## Function to show 1 Turtle
    def get (self, request, id):
        ## get the turtle
        turtle = Turtle.objects.get(id=id)
        ## serilize then turn into dictionary
        finalData = json.loads(serialize("json", [turtle]))
        ## send json response
        return JsonResponse(finalData, safe=False)

    ## Function for updating turtle
    def put (self, request, id):
        ## get the body
        body = GetBody(request)
        ##update turtle
        ## ** is like JS spread operator
        Turtle.objects.filter(id=id).update(**body)
        ## query for turtle
        turtle = Turtle.objects.get(id=id)
        ## serialize and make dict
        finalData = json.loads(serialize("json", [turtle]))
        ## return json data
        return JsonResponse(finalData, safe=False)

    def delete (self, request, id):
        ## query the turtle
        turtle = Turtle.objects.get(id=id)
        ## delete the turtle
        turtle.delete()
        ## serilize and dict updated turtle
        finalData = json.loads(serialize("json", [turtle]))
        ##send json response
        return JsonResponse(finalData, safe=False)