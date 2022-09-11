from django.db import models
from django.contrib.auth.models import User
from tracks.models import Track


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(
        Track, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'track']

    def __str__(self):
        return f'{self.owner} {self.track}'
