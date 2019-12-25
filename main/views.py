from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer
from background_task import background
import json
from .ttl_checker import update_ttl

class GetDataListView(APIView):

    def get(self, request):
        raw_query = request.query_params.get('keys')
        if isinstance(raw_query, str):
            keys = raw_query.split(',')
            queryset = Data.objects.filter(key__in =list(keys))            
        else:
            queryset = Data.objects.all()

        data = {}
        for q in queryset:
            data[q.key]=q.value

        return Response (data = data, status=status.HTTP_200_OK)
        
    def post(self, request):

        a= request.body
        json_data= json.loads(a.decode('utf-8'))

        counter = 0
        for k,v in json_data.items():
            #print(k)
            #print(v)
            data = Data(key=k, value=v)
            data.save()
            counter+=1
        return Response({'num_objects':counter, 'status':status.HTTP_201_CREATED})


    def patch(self, request):
        
        a= request.body
        json_data= json.loads(a.decode('utf-8'))

        key_list = list(json_data.keys())
        value_list=list(json_data.values())
        value_list.reverse()

        dataset = Data.objects.filter(key__in= key_list)

        for data in dataset:
            data.value = value_list.pop()
            update_ttl(data)
        
        return Response(json_data)

