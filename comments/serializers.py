from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_img = serializers.ReadOnlyField(
        source='owner.profile_img.image.url'
        )
    posted_at = serializers.SerializerMethodField()
    edited_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_posted_at(self, obj):
        return naturaltime(obj.posted_at)

    def get_edited_at(self, obj):
        return naturaltime(obj.edited_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'track', 'content', 'posted_at',
            'edited_at', 'is_owner', 'profile_id', 'profile_img'
        ]


class CommentDetailSerializer(CommentSerializer):
    track = serializers.ReadOnlyField(source='track.id')
