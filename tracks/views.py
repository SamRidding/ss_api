from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Track
from .serializers import TrackSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class TrackList(APIView):
    serializer_class = TrackSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(
            tracks, many=True, context={'request': request}
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
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TrackSerializer

    def get_object(self, pk):
        try:
            track = Track.objects.get(pk=pk)
            self.check_object_permissions(self.request, track)
            return track
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackSerializer(
            track, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackSerializer(
            track, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        track = self.get_object(pk)
        track.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
