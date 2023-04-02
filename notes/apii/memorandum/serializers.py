from rest_framework import serializers

from memorandum.models import Note



class NoteModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "text", "author", "created_at"]