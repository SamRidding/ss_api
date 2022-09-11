from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    audio = models.URLField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../defaultuserimg_mv93dr'
    )
    content = models.TextField(blank=True)
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=PUBLISHED
    )
    posted_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f'{self.id} {self.title}'
