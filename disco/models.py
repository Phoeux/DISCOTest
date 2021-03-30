from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class SoftDeleteMixin(models.Model):
    deleted = models.DateTimeField(blank=True, null=True)
    hard_deleted = models.DateTimeField()

    def delete(self, *args, **kwargs):
        self.deleted = now()
        self.save(update_fields=['deleted'])

    class Meta:
        abstract = True


class Track(models.Model):
    title = models.CharField(max_length=20)
    track_comment = models.ForeignKey('TrackComment', on_delete=models.CASCADE, related_name='track')


class Playlist(models.Model):
    title = models.CharField(max_length=20)
    number_of_tracks = models.PositiveIntegerField(default=0)
    version = models.ForeignKey('PlaylistVersion', on_delete=models.CASCADE)


class PlaylistVersion(models.Model):
    version = models.FloatField(default=0)


class TrackComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='track_comment')
    text = models.TextField(max_length=250)
