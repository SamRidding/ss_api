from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Track
from .serializers import TrackSerializer


class TrackList(APIView):
    serializer_class = TrackSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Track.objects.all()
        serializer = TrackSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TrackSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TrackDetail(APIView):
    