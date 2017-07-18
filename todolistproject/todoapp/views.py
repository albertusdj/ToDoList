from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from .models import ToDoList
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request) :
    return render(request, 'index.html')

def get_init_data(request) :
    data = serializers.serialize('json', ToDoList.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_new(request) :
    print(request.body.decode('utf-8'))
    jsondata = json.loads(request.body.decode('utf-8'))
    tempActivity = jsondata['activity']
    tempDone = jsondata['done']
    
    tempObj = ToDoList(activity=tempActivity, done=tempDone)
    tempObj.save()
    return HttpResponse('posted')

@csrf_exempt
def delete_object(request) :
    jsondata = json.loads(request.body.decode('utf-8'))
 
    for item in jsondata :
        tempActivity = item['activity']
        ListOfObjectToBeDeleted = ToDoList.objects.filter(activity=tempActivity)
        ObjectToBeDeleted = ListOfObjectToBeDeleted[0]
        ObjectToBeDeleted.delete()

    return HttpResponse('deleted')
