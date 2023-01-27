from list.models import List, ListTrack
from mbtrack.models import MBTrack
from rest_framework import serializers

class ListTrackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.PrimaryKeyRelatedField(queryset=MBTrack.objects.all())
    artist = serializers.PrimaryKeyRelatedField(queryset=MBTrack.objects.all())
    length = serializers.PrimaryKeyRelatedField(queryset=MBTrack.objects.all())
    list = serializers.PrimaryKeyRelatedField(read_only=True)
    track = serializers.PrimaryKeyRelatedField(read_only=True)
    position = serializers.IntegerField()

    class Meta:
        model = ListTrack
        #fields = ('id', 'list', 'mbtrack', 'position', 'name','artist','length')
        #fields = ('id', 'list', 'name','artist','length')
        fields = ('id', 'list', 'track', 'name','artist','length', 'position')

    def create(self, validated_data):
        return ListTrack.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.list = validated_data.get('list', instance.list)
        instance.track = validated_data.get('track', instance.mbtrack)
        instance.position = validated_data.get('position', instance.position)


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    note = serializers.CharField(required=False, allow_blank=True, max_length=200)
    owner = serializers.StringRelatedField()
    public = serializers.BooleanField()
    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    mbtracks = ListTrackSerializer(many=True)

    class Meta:
        model = List
        fields = ('id', 'name', 'note', 'owner', 'public', 'updated_at', 'created_at', 'mbtracks')

    def create(self, validated_data):
        return List.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.note = validated_data.get('note', instance.note)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.public = validated_data.get('public', instance.public)
        instance.save()
        return instance