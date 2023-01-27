from django.db import models
from mbtrack.models import MBTrack

class List(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    note = models.CharField(max_length=200, blank=False, default='')
    public = models.BooleanField(default=False)
    tracks = models.ManyToManyField(MBTrack, through='ListTrack')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ListTrack(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, blank=False, related_name='related_tracks')
    track = models.ForeignKey(MBTrack, on_delete=models.CASCADE, blank=False, related_name='related_list')
    position = models.SmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)