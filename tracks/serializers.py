from rest_framework import serializers
from tracks.models import Track
from likes.models import Like
from reposts.models import Repost


class TrackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_img = serializers.ReadOnlyField(
        source='owner.profile_img.image.url'
        )
    like_id = serializers.SerializerMethodField()
    repost_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, track=obj
            ).first()
            return like.id if like else None
        return None

    def get_repost_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            repost = Repost.objects.filter(
                owner=user, track=obj
            ).first()
            return repost.id if repost else None
        return None

    class Meta:
        model = Track
        fields = [
            'id', 'owner', 'title', 'audio',
            'image', 'content', 'status',
            'posted_at', 'edited_at', 'image',
            'is_owner', 'profile_id', 'profile_img',
            'like_id', 'repost_id', 'likes_count',
            'comments_count'
        ]
