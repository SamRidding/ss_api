from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from ss_api.permissions import IsOwnerOrReadOnly
from reposts.models import Repost
from reposts.serializers import RepostSerializer


class RepostList(generics.ListCreateAPIView):
    serializer_class = RepostSerializer
    queryset = Repost.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RepostDetail(generics.RetrieveDestroyAPIView):
    serializer_class = RepostSerializer
    queryset = Repost.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
