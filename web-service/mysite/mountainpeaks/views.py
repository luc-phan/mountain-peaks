from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Peak
from .serializers import PeakSerializer

# Create your views here.

class PeakViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows peaks to be viewed or edited.
    """
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        box = self.request.query_params.get('box')
        if box:
            lat0, lat1, lon0, lon1 = box.split(',')
            queryset = Peak.objects.filter(
                lat__gte=lat0,
                lat__lte=lat1,
                lon__gte=lon0,
                lon__lte=lon1
            )
        else:
            queryset = Peak.objects.all()
        serializer = PeakSerializer(queryset, many=True)
        return Response(serializer.data)

def docs(request):
    return render(request, 'mountainpeaks/docs.html')

def mapview(request):
    return render(request, 'mountainpeaks/mapview.html')
