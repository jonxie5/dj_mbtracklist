from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from list.models import List, ListTrack
from list.serializers import ListSerializer, ListTrackSerializer

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list/index.html'

    def get(self, request):
        # TODO: pagination
        queryset = List.objects.all()[:25]
        return Response({'lists': queryset})

class detailList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list/list_detail.html'

    def get(self, request, pk):
        try:
            list = List.objects.get(pk=pk)
        except List.DoesNotExist:
            return JsonResponse({'message': 'The list does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response({'list': list})

class listTracksByListPK(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list/list_tracks.html'

    def get(self, request, pk):
        try:
            list = List.objects.get(pk=pk)
        except List.DoesNotExist:
            return JsonResponse({'message': 'The list tracks does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response({'tracks': list.tracks})

@api_view(['GET', 'PUT'])
def list_detail(request, pk):
    try:
        list = List.objects.get(pk=pk)
    except List.DoesNotExist:
        return JsonResponse({'message': 'The list does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        list_serializer = ListSerializer(list)
        return JsonResponse(list_serializer.data)

    elif request.method == 'PUT':
        list_data = JSONParser().parse(request)
        list_serializer = ListSerializer(list, data=list_data)
        if list_serializer.is_valid():
            list_serializer.save()
            return JsonResponse(list_serializer.data)
        return JsonResponse(list_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)