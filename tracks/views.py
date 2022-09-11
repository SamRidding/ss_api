from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Track
from .serializers import TrackSerializer


class TrackList(APIView):
    def get(self, request):
        posts = Track.objects.all()
        serializer = TrackSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)
