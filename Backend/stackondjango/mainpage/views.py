from django.shortcuts import render
from django.http import JsonResponse
from mainpage import serializers
from mainpage.serializers import CollectionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection
import json
import pandas as pd
import joblib

model=joblib.load('stackonmodel.pkl')

def resultJson(request):
    data = json.loads(request.body)
    dataFrame = pd.DataFrame({'x':data}).transpose()
    result = model.predict(dataFrame)
    result = float(result)
    return JsonResponse({'result':result})


@api_view(['GET', 'POST'])
def collection_list(request, format=None):

    if request.method == 'GET':
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return JsonResponse({"collections": serializer.data})

    if request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, id, format=None):

    try:
        collection = Collection.objects.get(pk=id)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)