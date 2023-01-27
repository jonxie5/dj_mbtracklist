from mbtrack.models import MBTrack
from rest_framework import serializers

class MBTrackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    length = serializers.IntegerField(read_only=True)
    artist = serializers.CharField(read_only=True)
    track_mbid = serializers.UUIDField(read_only=True)
    recording_mbid = serializers.UUIDField(read_only=True)
    known = serializers.BooleanField()

    class Meta:
        model = MBTrack
        fields = ('id','name','length','artist','track_mbid','recording_mbid','known')

    def create(self, validated_data):
        return MBTrack.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.known = validated_data.get('known',instance.known)
        instance.save()
        return instance
