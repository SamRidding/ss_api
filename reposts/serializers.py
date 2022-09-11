from django.db import IntegrityError
from rest_framework import serializers
from reposts.models import Repost


class RepostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Repost
        fields = ['id', 'owner', 'track', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicated repost'
            })
