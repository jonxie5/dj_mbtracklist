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
from mbtrack.models import MBTrack
from mbtrack.serializers import MBTrackSerializer

class MBTrackViewSet(viewsets.ModelViewSet):
    queryset = MBTrack.objects.all()
    serializer_class = MBTrackSerializer
    permission_classes = [permissions.IsAuthenticated]

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mbtrack/index.html'

    def get(self, request):
        # TODO: pagination
        queryset = MBTrack.objects.all()[:25]
        return Response({'mbtracks': queryset})

@api_view(['GET', 'POST'])
def mbtrack_list(request):
    if request.method == 'GET':
        mbtracks = MBTrack.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            mbtracks = mbtracks.filter(name__icontains=name)

        mbtracks_serializer = MBTrackSerializer(mbtracks, many=True,  context={'request': request})
        return JsonResponse(mbtracks_serializer.data, safe=False)

    elif request.method == 'POST':
        mbtrack_data = JSONParser().parse(request)
        mbtrack_serializer = MBTrackSerializer(data=mbtrack_data)
        if mbtrack_serializer.is_valid():
            mbtrack_serializer.save()
            return JsonResponse(mbtrack_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(mbtrack_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def mbtrack_detail(request, pk):
    pass
    try:
        mbtrack = MBTrack.objects.get(pk=pk)
    except MBTrack.DoesNotExist:
        return JsonResponse({'message': 'The track does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mbtrack_serializer = MBTrackSerializer(mbtrack)
        return JsonResponse(mbtrack_serializer.data)

    elif request.method == 'PUT':
        mbtrack_data = JSONParser().parse(request)
        mbtrack_serializer = MBTrackSerializer(mbtrack, data=mbtrack_data)
        if mbtrack_serializer.is_valid():
            mbtrack_serializer.save()
            return JsonResponse(mbtrack_serializer.data)
        return JsonResponse(mbtrack_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)