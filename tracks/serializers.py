from rest_framework import serializers
from tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_img = serializers.ReadOnlyField(
        source='owner.profile_img.image.url'
        )

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Track
        fields = [
            'id', 'owner', 'title', 'audio',
            'image', 'content', 'status',
            'posted_at', 'edited_at', 'image',
            'is_owner', 'profile_id', 'profile_img'
        ]
