from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer
# Create your views here.




class GetDataListView(APIView):
    def get(self, request):
        raw_query = request.query_params.get('keys')
        if isinstance(raw_query, str):
            keys = raw_query.split(',')
            print(keys)
            queryset = Data.objects.filter(key__in =list( keys))            
        else:
            queryset = Data.objects.all()
        
        data = DataSerializer(queryset, many = True).data
        return Response (data = data, status=status.HTTP_200_OK)
        
            