from django.db import models

class MBTrack(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    artist = models.CharField(max_length=200, blank=False, default='')
    length = models.IntegerField(default=0)
    track_mbid = models.UUIDField(unique=True)
    recording_mbid = models.UUIDField()
    known = models.BooleanField(default=False)

    def __str__(self):
        return self.name
