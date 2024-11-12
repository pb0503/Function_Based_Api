from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view()
def first_view(request):
    msg='This is Our First View'
    return Response(data={"msg":msg})

@api_view(['GET','POST','PATCH'])
def second_view(request):
    if request.method=='GET':
        msg='REQUEST THOUGH GET METHOD'
    elif request.method=='POST':
        msg='REQUEST THOUGH POST METHOD'
    elif request.method=='PATCH':
         msg='REQUEST THOUGH PATCH METHOD'
    return Response(data={'msg':msg})

@api_view(['GET','POST'])
def third_view(request):
    msg='REQUEST THROUGH GET METHOD'
    if request.method=='POST':
        print(request.data)
        return Response(data=request.data)
    return Response(data={"msg":msg})
    