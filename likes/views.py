from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from ss_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
