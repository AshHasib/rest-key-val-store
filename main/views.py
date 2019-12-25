from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer
from background_task import background
import json
from .ttl_checker import update_ttl, update_all_ttl

class DataAPIView(APIView):

    def get(self, request):
        raw_query = request.query_params.get('keys')

        if isinstance(raw_query, str):
            keys = raw_query.split(',')
            queryset = Data.objects.filter(key__in =list(keys))   

        else:
            queryset = Data.objects.all()
            update_all_ttl()

        data = {}
        for q in queryset:
            data[q.key]=q.value
            update_ttl(q)

        return Response (data = data, status=status.HTTP_200_OK)
        
    def post(self, request):
        bytes_data= request.body
        json_data= json.loads(bytes_data.decode('utf-8'))

        counter = 0
        for k,v in json_data.items():
            #print(k)
            #print(v)
            data = Data(key=k, value=v)
            data.save()
            counter+=1
        return Response({'num_objects':counter, 'status':status.HTTP_201_CREATED})


    def patch(self, request):
        bytes_data= request.body
        json_data= json.loads(bytes_data.decode('utf-8'))

        key_list = list(json_data.keys())
        value_list=list(json_data.values())
        value_list.reverse()

        for key in key_list:

            try:
                data = Data.objects.get(key=key)
                data.value = json_data[key]
                update_ttl(data)

            except Exception as e:
                pass
        
        return Response(json_data, status = status.HTTP_200_OK)

